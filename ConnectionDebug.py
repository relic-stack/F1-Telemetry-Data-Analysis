import requests

print("Starting...")
r = requests.get("https://livetiming.formula1.com")
print(r.status_code)
print(requests.get("https://api.github.com").status_code)