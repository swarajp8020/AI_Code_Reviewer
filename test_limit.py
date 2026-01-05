import requests
import time

# usage: python test_limit.py

url = "http://127.0.0.1:8000/review"
key = "SWARAJ_SECURE_2026"  # Ensure this matches your server.py token

headers = {"X-Service-Token": key}
data = {"code": "print('test')", "task": "fix_python"}

print("🥊 Starting Rate Limit Test (Limit: 5/min)...")

for i in range(1, 10):
    try:
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            print(f"Request {i}: ✅ Success")
        elif response.status_code == 429:
            print(f"Request {i}: 🛑 BLOCKED! (Rate Limit Working)")
            break # We proved it works!
        else:
            print(f"Request {i}: ⚠️ Error {response.status_code}")
            
    except Exception as e:
        print(f"Connection failed: {e}")

print("Test Complete.")