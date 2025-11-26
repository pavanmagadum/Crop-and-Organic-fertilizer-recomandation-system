Climate-Aware Crop & Organic Fertilizer Recommendation System - Final Project
--------------------------------------------------------------------------
Quick start:
1. Create a Python venv:
   python -m venv venv
   venv\Scripts\activate
2. Install dependencies:
   pip install -r requirements.txt
3. Initialize community DB (optional):
   python -c "from community import db as cdb; cdb.init_db()"
4. Run the app:
   streamlit run app/app.py
Notes:
- For real-time weather, set OpenWeatherMap API key in the sidebar.
- For YouTube tutorial search, pytube is used by default (no API key required).
- Models are trained on synthetic data. Replace data/crop_data.csv with real data for production.
