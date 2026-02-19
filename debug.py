import requests
from requests.auth import HTTPBasicAuth

DOMAIN = "dathere.freshdesk.com"
API_KEY = "XyyXK4gzXY1hU6aWSAo"
AUTH = HTTPBasicAuth(API_KEY, "X")

res = requests.get(
    f"https://{DOMAIN}/api/v2/solutions/categories",
    auth=AUTH
)

print("Status code:", res.status_code)
print("Response text:", res.text)