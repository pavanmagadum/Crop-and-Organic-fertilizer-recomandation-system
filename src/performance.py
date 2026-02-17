"""
Performance optimization module for Climate-Aware Farming app
Includes caching, multi-threading, and performance monitoring
"""
import streamlit as st
import time
from functools import wraps
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

logger = logging.getLogger(__name__)

# Initialize thread pool for background tasks
executor = ThreadPoolExecutor(max_workers=20, thread_name_prefix="farm_worker_")

@st.cache_data
def cached_load_models(crop_model_path='crop_model.joblib', fert_model_path='fert_model.joblib'):
    """Cache model loading for better performance"""
    import joblib
    try:
        crop = joblib.load(crop_model_path)
        fert = joblib.load(fert_model_path)
        artifacts = joblib.load('artifacts.joblib')
        return crop, fert, artifacts
    except Exception as e:
        logger.error(f"Model loading error: {e}")
        return None, None, None

@st.cache_data
def cached_fetch_weather(region):
    """Cache weather data for regions"""
    # Placeholder - implement actual weather fetch
    return {"temp": 25, "humidity": 70, "rainfall": 200}

@st.cache_data(ttl=3600)  # Cache for 1 hour
def cached_get_crop_duration(crop_name):
    """Cache crop duration lookups"""
    CROP_DURATION = {
        'rice': 120, 'maize': 90, 'wheat': 120, 'chickpea': 100,
        'kidneybeans': 95, 'pigeonpeas': 150, 'soybean': 100,
    }
    return CROP_DURATION.get(crop_name.lower(), 90)

class PerformanceMonitor:
    """Monitor app performance metrics"""
    
    def __init__(self):
        self.metrics = {} if 'perf_metrics' not in st.session_state else st.session_state['perf_metrics']
        
    def start_timer(self, task_name):
        """Start measuring a task"""
        self.metrics[task_name] = time.time()
        
    def end_timer(self, task_name):
        """End measuring and return duration"""
        if task_name in self.metrics:
            duration = time.time() - self.metrics[task_name]
            logger.info(f"⏱️ {task_name}: {duration:.2f}s")
            return duration
        return 0
    
    def get_metrics(self):
        """Get all metrics"""
        return self.metrics
    
    def save_to_session(self):
        """Save metrics to session state"""
        st.session_state['perf_metrics'] = self.metrics

# Async task runner for background processing
def run_async_task(func, *args, **kwargs):
    """Run a function in a background thread"""
    return executor.submit(func, *args, **kwargs)

def run_parallel_tasks(tasks):
    """Run multiple tasks in parallel
    tasks: list of (func, args, kwargs) tuples
    """
    futures = [executor.submit(func, *args, **kwargs) for func, args, kwargs in tasks]
    results = []
    for future in as_completed(futures):
        try:
            results.append(future.result())
        except Exception as e:
            logger.error(f"Parallel task error: {e}")
            results.append(None)
    return results

# Performance decorator
def measure_performance(func):
    """Decorator to measure function performance"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        monitor = PerformanceMonitor()
        task_name = func.__name__
        monitor.start_timer(task_name)
        result = func(*args, **kwargs)
        duration = monitor.end_timer(task_name)
        monitor.save_to_session()
        return result
    return wrapper
