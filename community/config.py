"""
Database configuration for both local and cloud deployments
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Detect environment
IS_STREAMLIT_CLOUD = os.path.exists('/home/appuser')  # Streamlit Cloud uses /home/appuser path
DATABASE_TYPE = os.getenv('DATABASE_TYPE', 'sqlite')

# Database configuration based on environment
if IS_STREAMLIT_CLOUD:
    # Streamlit Cloud: Use persistent directory or cloud database
    # Option 1: Use persistent directory (if configured in Streamlit Cloud)
    DB_PATH = '/app/.streamlit/community.db'  # Persistent storage
    
    # Option 2: Use a cloud database (recommended for production)
    # DATABASE_TYPE = 'postgresql'
    # DATABASE_URL = os.getenv('DATABASE_URL')  # Set in Streamlit Cloud secrets
else:
    # Local environment: Use SQLite
    DB_PATH = 'community/community.db'

print(f"[INFO] Environment: {'Streamlit Cloud' if IS_STREAMLIT_CLOUD else 'Local'}")
print(f"[INFO] Database Type: {DATABASE_TYPE}")
print(f"[INFO] Database Path: {DB_PATH}")
