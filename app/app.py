import streamlit as st, joblib, pandas as pd, os, json
import sys
from pathlib import Path
# add project root (two levels up if app is in app/) so `src` imports resolve
proj_root = Path(__file__).resolve().parents[1]
if str(proj_root) not in sys.path:
    sys.path.insert(0, str(proj_root))

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

# Compatibility helper: set query params in a Streamlit-version-safe way
def set_query_params_safe(**kwargs):
    """Set query params using the stable API when available, otherwise fall back.

    Preference order:
    1. `st.set_query_params` (stable API)
    2. `st.experimental_set_query_params` (older API)
    3. As a last resort, write values into `st.session_state` so UI can react.
    """
    try:
        # new stable API
        if hasattr(st, 'set_query_params'):
            st.set_query_params(**kwargs)
            return
    except Exception:
        pass
    # Try assigning to st.query_params when available (newer Streamlit versions)
    try:
        if hasattr(st, 'query_params'):
            try:
                # construct a mapping; Streamlit may expect lists for values
                qp = {k: (v if isinstance(v, (list, tuple)) else [v]) for k, v in kwargs.items()}
                st.query_params = qp
                return
            except Exception:
                # assignment may not be supported in some builds; continue to next fallback
                pass
    except Exception:
        pass
    try:
        # older experimental API (may be removed in some versions)
        if hasattr(st, 'experimental_set_query_params'):
            st.experimental_set_query_params(**kwargs)
            return
    except Exception:
        pass
    # final fallback: update session state so the app can observe navigation intent
    for k, v in kwargs.items():
        st.session_state[k] = v

st.set_page_config(page_title='Climate Aware Crop & Organic Fertilizer', layout='wide')
# Simple custom theme + CSS for cards, buttons and backgrounds
st.markdown('''
<style>
    :root{--primary-green:#1f8f3f;--card-bg:#fbfbf6;--muted:#6b6b6b}
    body{background:linear-gradient(180deg,#fbfff7,#ffffff);}
    .main-title{font-size:28px;font-weight:700;margin-bottom:4px}
    .subtitle{color:var(--muted);margin-top:0;margin-bottom:18px}
    .app-card{background:var(--card-bg);border-radius:12px;padding:18px;margin-bottom:12px;box-shadow:0 6px 18px rgba(15,15,15,0.06);border:1px solid rgba(0,0,0,0.03)}
    .result-card{border-left:6px solid var(--primary-green);padding:14px;border-radius:8px;background:#ffffff}
    .section-title{font-size:16px;font-weight:600;color:var(--primary-green);margin-bottom:8px}
    .small-muted{color:#666;font-size:13px}
    .stButton>button{background:var(--primary-green)!important;border-radius:8px;color:white}
    h2.stHeading{font-size:20px}
</style>
''', unsafe_allow_html=True)
st.title('🌾 Climate‑Aware Crop & Organic Fertilizer Recommendation System', anchor=False)
st.markdown('<div class="subtitle">Quickly predict suitable crops and organic fertilizer equivalents using local soil and climate inputs.</div>', unsafe_allow_html=True)
# Sidebar settings (removed unused API key inputs)
# Navigation: replace generic Settings with clear page navigation
page = st.sidebar.radio('Navigate', ['Home', 'Prediction', 'Preparation', 'Community'], index=1)

# Keep OpenWeather API key input tucked under auth (optional)
OPENWEATHER_KEY = None

# initialize user in session state (auth UI rendered on Community page)
if 'user' not in st.session_state:
    st.session_state['user'] = None
# Page rendering: Home, Prediction, Preparation, Community
st.markdown('''
<style>
    .feature{display:inline-block;padding:10px 14px;margin:6px;border-radius:6px;background:#f1fff2;color:#0b6b2e}
    .sidebar .stRadio>div{padding:6px}
</style>
''', unsafe_allow_html=True)

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
    # Two-column layout: left for inputs (grouped), right for a Result card
    left, right = st.columns([2, 1], gap='large')

    # LEFT: Inputs grouped into cards
    with left:
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        st.subheader('Crop & Fertilizer Recommendation')
        st.markdown('<div class="small-muted">Fill the form and run prediction to see results on the right.</div>', unsafe_allow_html=True)
        with st.form('input_form'):
            # Location & Soil
            st.markdown('<div class="section-title">Location & Soil</div>', unsafe_allow_html=True)
            cols = st.columns(2)
            with cols[0]:
                region = st.selectbox('Region', ['North','South','East','West','Central'])
            with cols[1]:
                soil = st.selectbox('Soil Type', ['Loamy','Sandy','Clayey','Silty'])

            st.markdown('<hr/>', unsafe_allow_html=True)
            # Soil Nutrients
            st.markdown('<div class="section-title">Soil Nutrients (NPK)</div>', unsafe_allow_html=True)
            ncols = st.columns(3)
            with ncols[0]:
                N = st.number_input('Nitrogen (N)', min_value=0.0, value=100.0)
            with ncols[1]:
                P = st.number_input('Phosphorus (P)', min_value=0.0, value=50.0)
            with ncols[2]:
                K = st.number_input('Potassium (K)', min_value=0.0, value=150.0)

            st.markdown('<hr/>', unsafe_allow_html=True)
            # Climate Conditions
            st.markdown('<div class="section-title">Climate Conditions</div>', unsafe_allow_html=True)
            ccols = st.columns(4)
            with ccols[0]:
                pH = st.number_input('Soil pH', min_value=3.0, max_value=9.0, value=6.5, format='%.2f')
            with ccols[1]:
                temp = st.number_input('Temperature (°C)', value=25.0)
            with ccols[2]:
                humidity = st.number_input('Humidity (%)', value=70.0)
            with ccols[3]:
                rainfall = st.number_input('Rainfall (mm annual)', value=800.0)

            st.markdown('<div style="height:8px"></div>', unsafe_allow_html=True)
            submitted = st.form_submit_button('Run Prediction')
        st.markdown('</div>', unsafe_allow_html=True)

        # Keep prediction logic intact; only change UI presentation
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

            nf = None
            used_fert_model = False
            try:
                fert_bundle = joblib.load('fert_model.joblib')
                fert_model = fert_bundle['model']; fert_le = fert_bundle['le']; cols = fert_bundle['columns']
                row = df.copy(); row = pd.get_dummies(row, columns=['region','soil_type'], drop_first=True)
                for c in cols:
                    if c not in row.columns: row[c]=0
                Xf = row[cols].values
                try:
                    nf = fert_le.inverse_transform([fert_model.predict(Xf)[0]])[0]
                    used_fert_model = True
                    # If the trained fertilizer model only knows a very small set of classes,
                    # it's probably undertrained; prefer the heuristic to provide richer suggestions.
                    try:
                        num_classes = len(getattr(fert_le, 'classes_', []))
                    except Exception:
                        num_classes = 0
                    if num_classes <= 2:
                        # model appears limited; use heuristic instead
                        nf = predict_fertilizer_simple(N, P, K, pH, crop_pred)
                        used_fert_model = False
                        st.warning(f'Fertilizer model appears limited (only {num_classes} classes). Using heuristic suggestion instead.')
                except Exception:
                    # model prediction failed; fall back to heuristic
                    nf = predict_fertilizer_simple(N, P, K, pH, crop_pred)
                    used_fert_model = False
            except Exception:
                # fallback heuristic predictor if model file missing
                nf = predict_fertilizer_simple(N, P, K, pH, crop_pred)
                used_fert_model = False

            if nf:
                conv = convert_non_to_org(nf)
                # persist last result so actions survive reruns
                st.session_state['last_result'] = {
                    'crop_pred': crop_pred,
                    'nf': nf,
                    'conv': conv,
                    'input': {'region': region, 'soil': soil, 'N': N, 'P': P, 'K': K, 'pH': pH, 'temperature': temp, 'humidity': humidity, 'rainfall': rainfall}
                    , 'used_fert_model': used_fert_model
                }
                st.success('Prediction saved. See results on the right.')

    # RIGHT: Result card
    with right:
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<h4 style="margin-top:0">Result</h4>', unsafe_allow_html=True)
        if 'last_result' in st.session_state:
            lr = st.session_state['last_result']
            # Big crop title
            st.markdown(f"<h2 style='margin:6px 0 4px 0'>{lr.get('crop_pred')}</h2>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-weight:600;color:#2d6b2f;margin-bottom:8px'>Suggested fertilizer: {lr.get('nf')}</div>", unsafe_allow_html=True)
            # show source of recommendation
            src = 'Model' if lr.get('used_fert_model') else 'Heuristic'
            st.markdown(f"**Source:** {src}")
            conv = lr.get('conv', {})
            org = conv.get('organic') or ''
            st.markdown(f"**Organic equivalent:** {org}")
            # Why this recommendation (use small bullets from existing output variables)
            st.markdown('**Why this recommendation?**')
            reasons = []
            inp = lr.get('input', {})
            reasons.append(f"Soil type: {inp.get('soil')}")
            reasons.append(f"pH: {inp.get('pH')}")
            reasons.append(f"N-P-K: {inp.get('N')}-{inp.get('P')}-{inp.get('K')}")
            reasons.append(f"Temperature/Humidity: {inp.get('temperature')}°C / {inp.get('humidity')}%")
            for r in reasons:
                st.markdown(f"- {r}")
            notes = conv.get('notes')
            if notes:
                st.markdown('**Notes:**')
                st.markdown(notes)
            # Small action buttons
            st.markdown('<div style="margin-top:8px">', unsafe_allow_html=True)
            if st.button('Open Preparation'):
                # navigate to Preparation page by setting query params in a Streamlit-version-safe way
                set_query_params_safe(page='Preparation')
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="small-muted">Run prediction to see recommended crop and fertilizer here.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
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
            # Prefer a PDF download when we can generate it; otherwise offer a TXT fallback.
            pdf_bytes = None
            try:
                pdf_bytes = generate_preparation_pdf(conv.get('organic') or 'preparation', prep)
            except Exception:
                pdf_bytes = None
            if pdf_bytes:
                st.download_button('Download Preparation (PDF)', data=pdf_bytes, file_name=f"preparation_{conv.get('organic','fert')}.pdf", mime='application/pdf')
            else:
                st.download_button('Download Preparation (TXT)', prep_text, file_name=f"preparation_{conv.get('organic','fert')}.txt")
        else:
            st.write('No preparation steps available.')
        if st.button('Show Tutorials'):
            base_queries = build_search_queries(conv.get('organic'))
            # Preferred languages: Kannada first, then Hindi, then English
            languages = ['Kannada', 'Hindi', 'English']
            # include native script variants for better matching
            lang_variants = {
                'Kannada': ['Kannada', 'ಕನ್ನಡ'],
                'Hindi': ['Hindi', 'हिंदी'],
                'English': ['English']
            }
            results_by_lang = {lang: [] for lang in languages}
            seen_links = set()
            # For each language in preference order, try the base queries with language tag
            for lang in languages:
                variants = lang_variants.get(lang, [lang])
                for q in base_queries:
                    if len(results_by_lang[lang]) >= 3:
                        break
                    for vtag in variants:
                        search_q = f"{q} {vtag}"
                        try:
                            res = fetch_tutorials_pytube(search_q, max_results=4)
                        except Exception:
                            res = []
                        for r in res:
                            link = r.get('link')
                            if not link or link in seen_links:
                                continue
                            results_by_lang[lang].append(r)
                            seen_links.add(link)
                            if len(results_by_lang[lang]) >= 3:
                                break
                    # stop early if we have 3 videos for this language
                    if len(results_by_lang[lang]) >= 3:
                        break

            # If none found at all, show a message
            total_found = sum(len(v) for v in results_by_lang.values())
            if total_found == 0:
                st.info('No tutorial videos found for this organic fertilizer in Kannada/Hindi/English.')
            else:
                st.markdown('### Tutorial Videos (preferred: Kannada → Hindi → English)')
                for lang in languages:
                    vids = results_by_lang.get(lang, [])
                    if not vids:
                        continue
                    st.markdown(f"#### {lang}")
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

