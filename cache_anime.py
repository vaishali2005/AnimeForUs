import time
from fetch_data import *

# Cache storage
anime_cache = {
    'trending': {'data': [], 'time': 0},
    'top': {'data': [], 'time': 0},
    'popular': {'data': [], 'time': 0},
    'recent': {'data': [], 'time': 0}
}

CACHE_DURATION = 3600  # 1 hour

def get_cached_anime(cache_key, fetch_function):
    """Get anime data from cache or fetch if expired"""
    
    current_time = time.time()
    cache = anime_cache[cache_key]
    
    # If cache is still valid, return it
    if cache['data'] and (current_time - cache['time']) < CACHE_DURATION:
        return cache['data']
    
    # Otherwise fetch fresh data
    print(f"Fetching fresh {cache_key} data...")
    data = fetch_function()
    
    if data:  # Only cache if successful
        cache['data'] = data
        cache['time'] = current_time
    
    return data