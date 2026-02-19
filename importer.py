import requests
import json
import time
from requests.auth import HTTPBasicAuth

DOMAIN = "dathere.freshdesk.com"
API_KEY = "XyyXK4gzXY1hU6aWSAo"
AUTH = HTTPBasicAuth(API_KEY, "X")
BASE_URL = f"https://{DOMAIN}/api/v2/solutions"

def get_all(endpoint, params={}):
    results = []
    page = 1
    while True:
        res = requests.get(
            f"{BASE_URL}/{endpoint}",
            auth=AUTH,
            params={**params, "page": page, "per_page": 100}
        )
        if res.status_code == 429:  # rate limited
            time.sleep(60)
            continue
        data = res.json()
        if not data:
            break
        results.extend(data)
        page += 1
        time.sleep(0.5)  # be polite to the API
    return results

def export_all():
    print("Fetching categories...")
    categories = get_all("categories")

    full_export = []

    for category in categories:
        cat_id = category["id"]
        print(f"  Category: {category['name']}")

        folders = get_all(f"categories/{cat_id}/folders")

        category_data = {
            "category": category["name"],
            "folders": []
        }

        for folder in folders:
            folder_id = folder["id"]
            print(f"    Folder: {folder['name']}")

            articles = get_all(f"folders/{folder_id}/articles")

            category_data["folders"].append({
                "folder": folder["name"],
                "articles": [
                    {
                        "title": a.get("title"),
                        "body_html": a.get("description"),
                        "tags": a.get("tags", []),
                        "status": a.get("status"),
                        "created_at": a.get("created_at"),
                        "updated_at": a.get("updated_at"),
                    }
                    for a in articles
                ]
            })

        full_export.append(category_data)

    with open("freshdesk_export.json", "w", encoding="utf-8") as f:
        json.dump(full_export, f, indent=2, ensure_ascii=False)

    print("\nExport complete → freshdesk_export.json")

export_all()