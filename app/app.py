import streamlit as st, joblib, pandas as pd, os, json
from src.conversion import convert_non_to_org, fetch_tutorials_pytube, predict_fertilizer_simple, build_search_queries
import streamlit.components.v1 as components
from src.weather_api import fetch_weather
from community import db as cdb
from src.pdf_utils import generate_preparation_pdf
import sys
from pathlib import Path
# add project root (two levels up if app is in app/)
proj_root = Path(__file__).resolve().parents[1]
if str(proj_root) not in sys.path:
    sys.path.insert(0, str(proj_root))

st.set_page_config(page_title='Climate Aware Crop & Organic Fertilizer', layout='wide')
st.markdown('<style>body{background:linear-gradient(180deg,#f7fff4,#ffffff);} .big{font-size:26px;font-weight:600;}</style>',unsafe_allow_html=True)
st.title('🌾 Climate-Aware Crop & Organic Fertilizer Recommendation System')
# Sidebar settings (removed unused API key inputs)
# Navigation: replace generic Settings with clear page navigation
page = st.sidebar.radio('Navigate', ['Home', 'Prediction', 'Preparation', 'Community'], index=1)

# Keep OpenWeather API key input tucked under auth (optional)
OPENWEATHER_KEY = None

# initialize user in session state (auth UI rendered on Community page)
if 'user' not in st.session_state:
    st.session_state['user'] = None
# Page rendering: Home, Prediction, Preparation, Community
st.markdown('''<style>
.card{background:#fff;border-radius:8px;padding:16px;margin-bottom:12px;box-shadow:0 2px 6px rgba(0,0,0,0.06);} 
.feature{display:inline-block;padding:10px 14px;margin:6px;border-radius:6px;background:#f1fff2;color:#0b6b2e}
.sidebar .stRadio>div{padding:6px}
</style>''', unsafe_allow_html=True)

if page == 'Home':
    st.header('Welcome to Climate-Aware Farming')
    st.markdown('''
    This demo helps farmers choose appropriate crops and simple organic fertilizer preparations based on local soil and climate inputs.
    - Predict crop suitability
    - Convert common fertilizers to organic alternatives
    - Download step-by-step preparation PDF
    - Ask experts and get verified answers
    ''')
    st.markdown('<div class="card"> <h3>Quick Actions</h3> <div class="feature">Prediction</div> <div class="feature">Preparation</div> <div class="feature">Community</div> </div>', unsafe_allow_html=True)
    st.markdown('### Demo Checklist')
    st.markdown('''
    - Activate venv and run the app
    - Login as `farmer1` / `secret123` and `expert1` / `secret123`
    - Try Prediction → Prepare → Ask Expert flows
    ''')

elif page == 'Prediction':
    col1, col2 = st.columns([2,1])
    with col1:
        st.subheader('Crop & Fertilizer Recommendation')
        with st.form('input_form'):
            region = st.selectbox('Region', ['North','South','East','West','Central'])
            soil = st.selectbox('Soil Type', ['Loamy','Sandy','Clayey','Silty'])
            N = st.number_input('Nitrogen (N)', min_value=0.0, value=300.0)
            P = st.number_input('Phosphorus (P)', min_value=0.0, value=50.0)
            K = st.number_input('Potassium (K)', min_value=0.0, value=150.0)
            pH = st.number_input('Soil pH', min_value=3.0, max_value=9.0, value=6.5, format='%.2f')
            temp = st.number_input('Temperature (°C) (optional)', value=25.0)
            humidity = st.number_input('Humidity (%) (optional)', value=70.0)
            rainfall = st.number_input('Rainfall (mm annual) (optional)', value=800.0)
            submitted = st.form_submit_button('Run Prediction')
        if submitted:
            st.info('Running predictions...')
            try:
                crop_bundle = joblib.load('crop_model.joblib'); artifacts = joblib.load('artifacts.joblib')
            except Exception as e:
                st.error('Model files missing.'); st.stop()
            enc = artifacts['encoders']; scaler = artifacts['scaler']; crop_model = crop_bundle['model']
            df = pd.DataFrame([{'region':region,'soil_type':soil,'N':N,'P':P,'K':K,'pH':pH,'temperature':temp,'humidity':humidity,'rainfall':rainfall}])
            for c,le in enc.items():
                df[c] = le.transform(df[c].astype(str))
            X = df[['region','soil_type','N','P','K','pH','temperature','humidity','rainfall']].values
            Xs = scaler.transform(X)
            crop_pred = crop_model.predict(Xs)[0]
            st.success(f'🌱 Recommended Crop: {crop_pred}')
            nf = None
            try:
                fert_bundle = joblib.load('fert_model.joblib')
                fert_model = fert_bundle['model']; fert_le = fert_bundle['le']; cols = fert_bundle['columns']
                row = df.copy(); row = pd.get_dummies(row, columns=['region','soil_type'], drop_first=True)
                for c in cols:
                    if c not in row.columns: row[c]=0
                Xf = row[cols].values; nf = fert_le.inverse_transform([fert_model.predict(Xf)[0]])[0]
                st.info(f'🧪 Predicted Non-Organic Fertilizer: {nf}')
            except Exception:
                # fallback heuristic predictor
                st.warning('Fertilizer model not available; using heuristic fallback')
                nf = predict_fertilizer_simple(N, P, K, pH, crop_pred)
                st.info(f'🧪 Heuristic Predicted Non-Organic Fertilizer: {nf}')
            if nf:
                conv = convert_non_to_org(nf)
                # persist last result so actions survive reruns
                st.session_state['last_result'] = {
                    'crop_pred': crop_pred,
                    'nf': nf,
                    'conv': conv,
                    'input': {'region': region, 'soil': soil, 'N': N, 'P': P, 'K': K, 'pH': pH, 'temperature': temp, 'humidity': humidity, 'rainfall': rainfall}
                }
                st.success(f'🍃 Organic Equivalent: {conv.get("organic")}')
                st.write('Notes:', conv.get('notes'))
    with col2:
        st.markdown('<div class="card"><h4>Last Result</h4>', unsafe_allow_html=True)
        if 'last_result' in st.session_state:
            lr = st.session_state['last_result']
            st.markdown(f"**Crop:** {lr.get('crop_pred')}  ")
            st.markdown(f"**Non-organic:** {lr.get('nf')}")
            st.markdown(f"**Organic Equivalent:** {lr.get('conv',{}).get('organic')}")
        else:
            st.write('No prediction yet. Run a prediction to see quick actions here.')
        st.markdown('</div>', unsafe_allow_html=True)

elif page == 'Preparation':
    st.subheader('Preparation Steps & Tutorials')
    if 'last_result' not in st.session_state:
        st.info('No saved prediction. Go to Prediction and run a prediction first.')
    else:
        lr = st.session_state['last_result']
        conv = lr.get('conv', {})
        st.success(f"🍃 Last Recommended Organic Equivalent: {conv.get('organic')}")
        st.write('Notes:', conv.get('notes'))
        st.markdown('### Preparation')
        prep = conv.get('preparation_steps') or []
        if isinstance(prep, list) and prep:
            for i, step in enumerate(prep, start=1):
                st.markdown(f"**{i}.** {step}")
            prep_text = '\n'.join([f"{i}. {s}" for i, s in enumerate(prep, start=1)])
            st.download_button('Download Preparation', prep_text, file_name=f"preparation_{conv.get('organic','fert')}.txt")
            try:
                pdf_bytes = generate_preparation_pdf(conv.get('organic') or 'preparation', prep)
            except Exception:
                pdf_bytes = None
            if pdf_bytes:
                st.download_button('Download Preparation PDF', data=pdf_bytes, file_name=f"preparation_{conv.get('organic','fert')}.pdf", mime='application/pdf')
        else:
            st.write('No preparation steps available.')
        if st.button('Show Tutorials'):
            queries = build_search_queries(conv.get('organic'))
            vids = []
            seen_links = set()
            max_total = 8
            for q in queries:
                if len(vids) >= max_total:
                    break
                try:
                    results = fetch_tutorials_pytube(q, max_results=4)
                except Exception:
                    results = []
                for r in results:
                    link = r.get('link')
                    if not link or link in seen_links:
                        continue
                    vids.append(r); seen_links.add(link)
                    if len(vids) >= max_total:
                        break
            if not vids:
                st.info('No tutorial videos found for this organic fertilizer.')
            else:
                for i, v in enumerate(vids[:3], start=1):
                    st.markdown(f"**{i}. {v.get('title')}**")
                    try:
                        st.video(v.get('link'))
                    except Exception:
                        st.write(v.get('link'))

elif page == 'Community':
    st.subheader('Community & Experts')
    st.markdown('Initialize DB if first run and view posts.')
    # Authentication UI moved here so it is visible only on Community page
    st.markdown('---')
    auth_mode = st.selectbox('Mode', ['Guest','Login','Register'], key='community_auth_mode')
    if auth_mode == 'Login':
        username = st.text_input('Username', key='community_login_user')
        password = st.text_input('Password', type='password', key='community_login_pw')
        if st.button('Login', key='community_login_btn'):
            u = cdb.authenticate(username, password)
            if u:
                st.session_state['user'] = u
                st.success(f"Logged in as {u['username']} ({u['role']})")
            else:
                st.error('Login failed')
    elif auth_mode == 'Register':
        r_user = st.text_input('New username', key='community_reg_user')
        r_pw = st.text_input('New password', type='password', key='community_reg_pw')
        r_role = st.selectbox('Role', ['farmer','expert'], key='community_reg_role')
        if st.button('Register', key='community_reg_btn'):
            ok = cdb.create_user(r_user, r_pw, role=r_role)
            if ok:
                st.success('Registered. You can now login.')
            else:
                st.error('Registration failed (username may be taken).')
    else:
        if st.button('Logout', key='community_logout_btn'):
            st.session_state['user'] = None
            st.info('Logged out')

    if st.button('Init Community DB'):
        cdb.init_db(); st.success('Community DB initialized.')
    user = st.session_state.get('user')
    if user:
        st.markdown(f"**Signed in:** {user.get('username')} ({user.get('role')})")
        if user.get('role') == 'farmer':
            st.markdown('### Farmer Menu')
            if st.button('View My Prediction History'):
                rows = cdb.get_history(user.get('username'))
                if rows:
                    for r in rows:
                        st.markdown(f"**{r[3]}**")
                        st.write('Input:', r[1])
                        st.write('Result:', r[2])
                else:
                    st.info('No history found.')
            if st.button('View My Bookmarks'):
                bms = cdb.get_bookmarks(user.get('username'))
                if bms:
                    for b in bms:
                        st.markdown(f"- [{b[1]}]({b[2]})")
                else:
                    st.info('No bookmarks yet.')
        elif user.get('role') == 'expert':
            st.markdown('### Expert Menu')
            if st.button('View Questions'):
                qs = cdb.list_questions()
                if qs:
                    for q in qs:
                        st.markdown(f"**{q[1]}** by {q[3]} ({q[5]})")
                        st.write(q[2])
                        if q[4]:
                            st.markdown(f"Attachment: {q[4]}")
                        ans = cdb.get_answers(q[0])
                        if ans:
                            st.markdown('Answers:')
                            for a in ans:
                                aid = a[0]
                                content = a[1]
                                expert_name = a[2]
                                created = a[3]
                                verified = a[4]
                                st.markdown(f"- {content} (by {expert_name}) [{'verified' if verified else 'unverified'}]")
                                if user.get('role') == 'expert':
                                    if st.button(f'Verify Answer {aid}', key=f'verify_{aid}'):
                                        cdb.verify_answer(aid)
                                        st.success('Answer verified.')
                        with st.form(key=f'ans_{q[0]}'):
                            ans_txt = st.text_area('Your answer')
                            submit_ans = st.form_submit_button('Submit Answer')
                            if submit_ans and ans_txt:
                                cdb.create_answer(q[0], ans_txt, user.get('username'))
                                st.success('Answer submitted.')
            if st.button('Upload fertilizer_mapping (CSV)'):
                uploaded = st.file_uploader('Upload CSV', type=['csv'])
                if uploaded:
                    content = uploaded.getvalue()
                    with open('data/fertilizer_mapping.csv','wb') as f:
                        f.write(content)
                    st.success('fertilizer_mapping.csv updated')

            # Experts can conduct (schedule) live tutorials/sessions for farmers
            st.markdown('---')
            st.markdown('### Conduct Tutorial / Schedule Session')
            if user.get('role') == 'expert':
                with st.form(key='create_session_form'):
                    s_title = st.text_input('Session title')
                    s_link = st.text_input('Session link (Zoom/YouTube/Meet)')
                    s_when = st.text_input('Scheduled time (ISO or human-readable)', value='YYYY-MM-DD HH:MM')
                    submit_sess = st.form_submit_button('Create Session')
                    if submit_sess and s_title and s_link:
                        if hasattr(cdb, 'create_session'):
                            cdb.create_session(s_title, s_link, s_when, user.get('username'))
                            st.success('Session scheduled and visible to farmers.')
                        else:
                            st.error('Session feature not available (db module missing create_session). Please re-run the app or contact the developer.')

    # Show upcoming sessions to FARMERS only (experts do not see the public listing here)
    if user and user.get('role') == 'farmer':
        st.markdown('---')
        st.markdown('### Upcoming Tutorials & Live Sessions')
        sessions = cdb.list_sessions()
        if sessions:
            for s in sessions:
                sid, stitle, slink, swhen, sexpert = s
                st.markdown(f"**{stitle}** — scheduled: {swhen} (by {sexpert})")
                st.markdown(f"Link: {slink}")
                cols = st.columns([1,1,4])
                with cols[0]:
                    if st.button('Join Session', key=f'join_{sid}'):
                        # open link in new tab using markdown
                        st.markdown(f"[Open session link]({slink})")
                with cols[1]:
                    if st.button('Bookmark Session', key=f'bm_{sid}'):
                        cdb.add_bookmark(user.get('username'), stitle, slink)
                        st.success('Bookmarked for later')
                with cols[2]:
                    st.write('')
        else:
            st.info('No upcoming sessions scheduled.')
    posts = cdb.list_posts()
    if posts:
        st.markdown('### Recent Posts')
        for p in posts:
            st.markdown(f'**{p[1]}** by {p[3]} ({p[4]})'); st.write(p[2])
    else:
        st.info('No posts found. Experts can add posts using community.create_post or via DB scripts.')

st.markdown('---')
st.subheader('F2C Marketplace (Coming Soon)')
st.markdown('Product cards and farmer storefront UI will be added in next phase.')
