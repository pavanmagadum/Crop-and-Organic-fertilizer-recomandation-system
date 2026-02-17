"""
Keep-alive module to prevent Streamlit app from sleeping
Automatically pings the app every 5 minutes
"""
import requests
import threading
import time
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class AppKeepAlive:
    """Keeps the app alive by sending periodic pings"""
    
    def __init__(self, app_url, interval=300):
        """
        app_url: URL of the Streamlit app (e.g., https://myapp.railway.app)
        interval: Time between pings in seconds (default: 300 = 5 minutes)
        """
        self.app_url = app_url
        self.interval = interval
        self.running = False
        self.thread = None
    
    def start(self):
        """Start the keep-alive service"""
        if self.running:
            logger.warning("Keep-alive already running")
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._ping_loop, daemon=True)
        self.thread.start()
        logger.info(f"Keep-alive started for {self.app_url}")
    
    def stop(self):
        """Stop the keep-alive service"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=5)
        logger.info("Keep-alive stopped")
    
    def _ping_loop(self):
        """Continuous ping loop"""
        while self.running:
            try:
                response = requests.get(self.app_url, timeout=10)
                if response.status_code == 200:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    logger.debug(f"✅ Keep-alive ping successful at {timestamp}")
                else:
                    logger.warning(f"⚠️ Ping returned status {response.status_code}")
            except requests.exceptions.RequestException as e:
                logger.error(f"❌ Keep-alive ping failed: {e}")
            
            # Sleep before next ping
            time.sleep(self.interval)
    
    @staticmethod
    def create_uptime_robot_url(app_url):
        """Generate UptimeRobot integration (alternative method)
        
        Steps:
        1. Go to https://uptimerobot.com
        2. Create new monitor
        3. Add your app URL
        4. Set interval to 5 minutes
        """
        return f"https://uptimerobot.com (monitor: {app_url})"

# Usage in Streamlit app:
# if 'keep_alive' not in st.session_state:
#     keep_alive = AppKeepAlive(os.getenv('APP_URL', 'http://localhost:8502'))
#     keep_alive.start()
#     st.session_state['keep_alive'] = keep_alive
