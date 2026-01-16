# Database Persistence Guide: Local vs Streamlit Cloud

## Problem Explained

### Local Development (Terminal) ✅
- Database: `community/community.db` (local file system)
- **User data is SAVED** because the file persists
- Every app reload keeps the data

### Streamlit Cloud ❌
- Streamlit Cloud has **ephemeral file system**
- Any files created get **deleted when app restarts**
- User data is **NOT SAVED** between sessions

---

## Solution: Configure Database for Both Environments

### Step 1: For Local Development (Current Setup)
No changes needed! Your local SQLite database will continue working.

**Verify:**
```bash
cd c:\Users\sw\Desktop\climate_aware_final_project
# Check if database exists
dir community\community.db
```

---

### Step 2: For Streamlit Cloud Deployment (Choose ONE option)

#### Option A: Use Persistent Storage (Recommended for Testing)
1. In Streamlit Cloud dashboard, enable "Persistent storage" in app settings
2. Database will be saved at `/app/.streamlit/community.db`
3. This is already configured in `community/config.py`

**Steps to deploy:**
```bash
# 1. Push to GitHub
git add .
git commit -m "Add cloud database configuration"
git push

# 2. Go to https://streamlit.io/cloud
# 3. Deploy your repository
# 4. In app settings, enable "Persistent storage"
```

#### Option B: Use Cloud Database (Best for Production)
Use PostgreSQL, MySQL, or Supabase:

**Example with Supabase PostgreSQL:**

1. **Create Supabase account** (free): https://supabase.com
2. **Get connection string**
3. **Add to Streamlit Cloud Secrets:**
   - Go to app settings → Secrets
   - Add:
   ```toml
   DATABASE_TYPE = "postgresql"
   DATABASE_URL = "postgresql://user:password@host:5432/dbname"
   ```

4. **Install PostgreSQL driver:**
   ```bash
   pip install psycopg2-binary
   ```

5. **Update requirements.txt:**
   ```
   psycopg2-binary>=2.9.0
   ```

---

## How to Test

### Test 1: Verify Local Database
```bash
# 1. Start app locally
cd c:\Users\sw\Desktop\climate_aware_final_project
venv\Scripts\streamlit run app\app.py

# 2. Register a new user
# Go to http://localhost:8504 → Community → Sign Up
# Create test user: testuser123 / password123

# 3. Login as admin
# Go to http://localhost:8504/?admin=true
# Username: admin, Password: Admin@2025

# 4. Check User Management tab
# You should see testuser123 in the list ✅
```

### Test 2: Verify Admin Dashboard Shows Users
```bash
# After registering users, check:
# 1. 👥 User Management tab shows all users
# 2. Last login timestamp is updated
# 3. Click 🔄 Refresh Users to reload
```

---

## Environment Variables

### Local (.env file)
```
ADMIN_PASSWORD=Admin@2025
DATABASE_TYPE=sqlite
```

### Streamlit Cloud (secrets.toml)
```toml
ADMIN_PASSWORD = "Admin@2025"
DATABASE_TYPE = "postgresql"
DATABASE_URL = "postgresql://user:pass@host:5432/db"
```

---

## Troubleshooting

### Users not showing in admin dashboard?

**Check 1:** Restart the app
```bash
# Press Ctrl+C to stop
# Run again
venv\Scripts\streamlit run app\app.py
```

**Check 2:** Check if database file exists
```bash
# Local path
dir community\community.db
```

**Check 3:** Check database initialization
```bash
# The app now auto-initializes on startup (line 35 of app.py)
cdb.init_db()
```

**Check 4:** Verify user registration worked
- Go to Community → Sign Up
- Fill all fields (username, password, role)
- Click "Sign Up"
- Should see success message

**Check 5:** Verify authentication
- Go to Community → Login (not admin)
- Use the credentials you registered
- If login works, data is saved ✅

---

## Summary Table

| Feature | Local | Cloud (Persistent) | Cloud (PostgreSQL) |
|---------|-------|-------------------|-------------------|
| User Registration | ✅ | ✅ | ✅ |
| Data Persistence | ✅ | ✅ (with setup) | ✅ |
| Admin Dashboard | ✅ | ✅ (with setup) | ✅ |
| Last Login Tracking | ✅ | ✅ (with setup) | ✅ |
| Cost | Free | Free | Free (basic) |
| Complexity | Low | Medium | High |

---

## Next Steps

1. **Test locally** first with the refresh button
2. **Verify users are saved** by restarting the app
3. **When deploying to cloud**, choose your storage option
4. **Add persistent storage** or PostgreSQL before deploying

---

## Need Help?

If users are still not showing:
1. Check the browser console for errors (F12)
2. Check Streamlit logs in terminal
3. Try the 🔄 Refresh Users button
4. Create a new test user and immediately check admin dashboard
