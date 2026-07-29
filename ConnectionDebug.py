import requests

print("Testing raw HTTPS request to FastF1 data endpoints...")
try:
    # Test connection to Ergast/FastF1 endpoint with a strict 3s timeout
    res = requests.get("https://ergast.com/api/f1/2021.json", timeout=3)
    print("Ergast Response Code:", res.status_code)
except Exception as e:
    print("Network/SSL Error caught:", e)


import os
import fastf1

# 1. Enable logging so you can see progress
fastf1.set_log_level('INFO')

# 2. Setup cache safely
cache_dir = 'data_cache'
os.makedirs(cache_dir, exist_ok=True)
fastf1.Cache.enable_cache(cache_dir)

# 3. Get session and print metadata
session = fastf1.get_session(2021, 7, 'Q')

print(f"Session Loaded: {session.name}")
print(f"Grand Prix: {session.event['EventName']}")
print(f"Location: {session.event['Location']}")