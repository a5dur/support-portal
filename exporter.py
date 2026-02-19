import requests
import json
import time
import os
import re
from requests.auth import HTTPBasicAuth
from markdownify import markdownify as md
from urllib.parse import urlparse

DOMAIN = "dathere.freshdesk.com"
API_KEY = "XyyXK4gzXY1hU6aWSAo"
AUTH = HTTPBasicAuth(API_KEY, "X")
BASE_URL = f"https://{DOMAIN}/api/v2/solutions"
EXPORT_DIR = "freshdesk_export"

def sanitize(name):
    """Make a string safe for use as a folder/file name."""
    return re.sub(r'[<>:"/\\|?*]', '-', name).strip()

def get_all(endpoint, params={}):
    results = []
    page = 1
    while True:
        res = requests.get(
            f"{BASE_URL}/{endpoint}",
            auth=AUTH,
            params={**params, "page": page, "per_page": 100}
        )
        if res.status_code == 429:
            print("Rate limited, waiting 60s...")
            time.sleep(60)
            continue
        data = res.json()
        if not data:
            break
        results.extend(data)
        page += 1
        time.sleep(0.5)
    return results

def download_image(url, save_dir):
    """Download an image and return the local relative path."""
    try:
        filename = sanitize(os.path.basename(urlparse(url).path))
        if not filename:
            filename = "image.png"
        local_path = os.path.join(save_dir, filename)
        if os.path.exists(local_path):
            return local_path  # skip if already downloaded

        res = requests.get(url, timeout=15)
        if res.status_code == 200:
            with open(local_path, "wb") as f:
                f.write(res.content)
            return local_path
    except Exception as e:
        print(f"    Failed to download image {url}: {e}")
    return url  # fallback to original URL if download fails

def process_images(html, images_dir):
    """Download all images in the HTML and rewrite src to local paths."""
    os.makedirs(images_dir, exist_ok=True)
    img_pattern = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)

    def replace_img(match):
        original_url = match.group(1)
        local_path = download_image(original_url, images_dir)
        # Make path relative to the article's markdown file
        rel_path = os.path.relpath(local_path, images_dir).replace("\\", "/")
        return match.group(0).replace(original_url, f"images/{rel_path}")

    return img_pattern.sub(replace_img, html)

def save_article(article, folder_path):
    title = article.get("title", "Untitled")
    html_body = article.get("description") or ""
    tags = article.get("tags", [])
    created_at = article.get("created_at", "")
    updated_at = article.get("updated_at", "")

    # Download images and rewrite HTML src paths
    images_dir = os.path.join(folder_path, "images")
    html_body = process_images(html_body, images_dir)

    # Convert HTML to Markdown
    markdown_body = md(html_body, heading_style="ATX", bullets="-")

    # Build the markdown file with frontmatter
    frontmatter = f"""---
title: "{title}"
tags: {json.dumps(tags)}
created_at: {created_at}
updated_at: {updated_at}
---

"""
    content = frontmatter + f"# {title}\n\n" + markdown_body

    filename = sanitize(title) + ".md"
    filepath = os.path.join(folder_path, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"      ✓ {filename}")

def export_all():
    os.makedirs(EXPORT_DIR, exist_ok=True)
    print("Fetching categories...\n")
    categories = get_all("categories")

    for category in categories:
        cat_id = category["id"]
        cat_name = sanitize(category["name"])
        print(f"📁 {cat_name}")

        cat_path = os.path.join(EXPORT_DIR, cat_name)
        os.makedirs(cat_path, exist_ok=True)

        folders = get_all(f"categories/{cat_id}/folders")

        for folder in folders:
            folder_id = folder["id"]
            folder_name = sanitize(folder["name"])
            print(f"  📂 {folder_name}")

            folder_path = os.path.join(cat_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            articles = get_all(f"folders/{folder_id}/articles")

            for article in articles:
                save_article(article, folder_path)

            time.sleep(0.3)

    print(f"\n✅ Export complete → ./{EXPORT_DIR}/")

export_all()