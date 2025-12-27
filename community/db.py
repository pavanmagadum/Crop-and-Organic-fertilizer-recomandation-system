import sqlite3, hashlib, os, datetime
DB_PATH = 'community/community.db'
def init_db(path=DB_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, role TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY, title TEXT, content TEXT, author TEXT, created_at TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS sessions(id INTEGER PRIMARY KEY, title TEXT, link TEXT, scheduled_at TEXT, expert TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS comments(id INTEGER PRIMARY KEY, post_id INTEGER, user TEXT, content TEXT, created_at TEXT)''')
    # history: store predictions saved by farmers
    c.execute('''CREATE TABLE IF NOT EXISTS history(id INTEGER PRIMARY KEY, username TEXT, input_json TEXT, result_json TEXT, created_at TEXT)''')
    # bookmarks: store saved tutorial links
    c.execute('''CREATE TABLE IF NOT EXISTS bookmarks(id INTEGER PRIMARY KEY, username TEXT, title TEXT, link TEXT, created_at TEXT)''')
    # questions and answers
    c.execute('''CREATE TABLE IF NOT EXISTS questions(id INTEGER PRIMARY KEY, title TEXT, content TEXT, author TEXT, attachment_path TEXT, created_at TEXT, views INTEGER DEFAULT 0, saves INTEGER DEFAULT 0)''')
    c.execute('''CREATE TABLE IF NOT EXISTS answers(id INTEGER PRIMARY KEY, question_id INTEGER, content TEXT, expert TEXT, created_at TEXT, verified INTEGER DEFAULT 0)''')
    conn.commit(); conn.close()
def hash_pass(pw): return hashlib.sha256(pw.encode()).hexdigest()
def create_user(username, password, role='farmer', path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    try:
        c.execute('INSERT INTO users(username,password,role) VALUES (?,?,?)',(username,hash_pass(password),role))
        conn.commit(); return True
    except Exception as e:
        return False
    finally:
        conn.close()
def authenticate(username, password, path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('SELECT password, role FROM users WHERE username=?',(username,))
    row = c.fetchone()
    conn.close()
    if not row: return None
    stored, role = row
    if stored == hash_pass(password): return {'username':username,'role':role}
    return None
def create_post(title, content, author, path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('INSERT INTO posts(title,content,author,created_at) VALUES (?,?,?,?)',(title,content,author,datetime.datetime.now().isoformat()))
    conn.commit(); conn.close(); return True
def list_posts(path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('SELECT id,title,content,author,created_at FROM posts ORDER BY id DESC')
    rows = c.fetchall(); conn.close(); return rows

def save_history(username, input_json, result_json, path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('INSERT INTO history(username,input_json,result_json,created_at) VALUES (?,?,?,?)',(username,input_json,result_json,datetime.datetime.now().isoformat()))
    conn.commit(); conn.close(); return True

def get_history(username, path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('SELECT id,input_json,result_json,created_at FROM history WHERE username=? ORDER BY id DESC',(username,))
    rows = c.fetchall(); conn.close(); return rows

def add_bookmark(username, title, link, path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('INSERT INTO bookmarks(username,title,link,created_at) VALUES (?,?,?,?)',(username,title,link,datetime.datetime.now().isoformat()))
    conn.commit(); conn.close(); return True

def get_bookmarks(username, path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('SELECT id,title,link,created_at FROM bookmarks WHERE username=? ORDER BY id DESC',(username,))
    rows = c.fetchall(); conn.close(); return rows

def create_question(title, content, author, attachment_path=None, path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('INSERT INTO questions(title,content,author,attachment_path,created_at) VALUES (?,?,?,?,?)',(title,content,author,attachment_path,datetime.datetime.now().isoformat()))
    conn.commit(); conn.close(); return True

def list_questions(path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('SELECT id,title,content,author,attachment_path,created_at,views,saves FROM questions ORDER BY id DESC')
    rows = c.fetchall(); conn.close(); return rows

def create_answer(question_id, content, expert, path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('INSERT INTO answers(question_id,content,expert,created_at) VALUES (?,?,?,?)',(question_id,content,expert,datetime.datetime.now().isoformat()))
    conn.commit(); conn.close(); return True

def get_answers(question_id, path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('SELECT id,content,expert,created_at,verified FROM answers WHERE question_id=? ORDER BY id',(question_id,))
    rows = c.fetchall(); conn.close(); return rows

def verify_answer(answer_id, verified=1, path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('UPDATE answers SET verified=? WHERE id=?',(verified,answer_id))
    conn.commit(); conn.close(); return True

def simple_analytics(path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM users'); users = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM posts'); posts = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM questions'); questions = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM history'); histories = c.fetchone()[0]
    conn.close()
    return {'users':users,'posts':posts,'questions':questions,'histories':histories}

def create_session(title, link, scheduled_at, expert, path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('INSERT INTO sessions(title,link,scheduled_at,expert) VALUES (?,?,?,?)',(title,link,scheduled_at,expert))
    conn.commit(); conn.close(); return True

def list_sessions(path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('SELECT id,title,link,scheduled_at,expert FROM sessions ORDER BY scheduled_at')
    rows = c.fetchall(); conn.close(); return rows

def get_session(session_id, path=DB_PATH):
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('SELECT id,title,link,scheduled_at,expert FROM sessions WHERE id=?',(session_id,))
    row = c.fetchone(); conn.close(); return row

# ============================================
# ADMIN FUNCTIONS
# ============================================

def authenticate_admin(username, password, admin_password_env):
    """Authenticate admin using environment variable password"""
    if username == 'admin' and password == admin_password_env:
        return {'username': 'admin', 'role': 'admin'}
    return None

def get_all_users(path=DB_PATH):
    """Get all registered users (for admin dashboard)"""
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('SELECT id, username, role FROM users ORDER BY id DESC')
    rows = c.fetchall(); conn.close(); return rows

def delete_user(username, path=DB_PATH):
    """Delete a user (admin only)"""
    conn = sqlite3.connect(path); c = conn.cursor()
    try:
        c.execute('DELETE FROM users WHERE username=?', (username,))
        conn.commit(); return True
    except Exception as e:
        return False
    finally:
        conn.close()

def update_user_role(username, new_role, path=DB_PATH):
    """Update user role (admin only)"""
    conn = sqlite3.connect(path); c = conn.cursor()
    try:
        c.execute('UPDATE users SET role=? WHERE username=?', (new_role, username))
        conn.commit(); return True
    except Exception as e:
        return False
    finally:
        conn.close()

def get_all_posts_admin(path=DB_PATH):
    """Get all posts with more details (admin view)"""
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('SELECT id, title, content, author, created_at FROM posts ORDER BY id DESC')
    rows = c.fetchall(); conn.close(); return rows

def delete_post(post_id, path=DB_PATH):
    """Delete a post (admin only)"""
    conn = sqlite3.connect(path); c = conn.cursor()
    try:
        c.execute('DELETE FROM posts WHERE id=?', (post_id,))
        conn.commit(); return True
    except Exception as e:
        return False
    finally:
        conn.close()

def get_all_questions_admin(path=DB_PATH):
    """Get all questions with details (admin view)"""
    conn = sqlite3.connect(path); c = conn.cursor()
    c.execute('SELECT id, title, content, author, created_at, views, saves FROM questions ORDER BY id DESC')
    rows = c.fetchall(); conn.close(); return rows

def delete_question(question_id, path=DB_PATH):
    """Delete a question (admin only)"""
    conn = sqlite3.connect(path); c = conn.cursor()
    try:
        c.execute('DELETE FROM questions WHERE id=?', (question_id,))
        c.execute('DELETE FROM answers WHERE question_id=?', (question_id,))
        conn.commit(); return True
    except Exception as e:
        return False
    finally:
        conn.close()
