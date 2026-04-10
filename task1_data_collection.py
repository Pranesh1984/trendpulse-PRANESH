# PRANESH.S
# Task 1: Fetch data from HackerNews API

import requests
import time
import json
import os
from datetime import datetime

# API URLs
top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Header
headers = {"User-Agent": "TrendPulse/1.0"}

# Categories with keywords
categories = {
    "technology": ["ai","software","tech","code","computer","data","cloud","api","gpu","llm"],
    "worldnews": ["war","government","country","president","election","climate","attack","global"],
    "sports": ["nfl","nba","fifa","sport","game","team","player","league","championship"],
    "science": ["research","study","space","physics","biology","discovery","nasa","genome"],
    "entertainment": ["movie","film","music","netflix","game","book","show","award","streaming"]
}

# Function to detect category
def get_category(title):
    title = title.lower()
    for cat, words in categories.items():
        for word in words:
            if word in title:
                return cat
    return None

# Fetch top story IDs
try:
    ids = requests.get(top_url, headers=headers).json()[:500]
except:
    ids = []

data = []
count = {c: 0 for c in categories}

# Loop through categories
for cat in categories:
    for i in ids:
        if count[cat] >= 25:
            break

        try:
            story = requests.get(item_url.format(i), headers=headers).json()
        except:
            continue

        if not story or "title" not in story:
            continue

        if get_category(story["title"]) == cat:
            data.append({
                "post_id": story.get("id"),
                "title": story.get("title"),
                "category": cat,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", "unknown"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            count[cat] += 1

    time.sleep(2)  # required

# Create folder
if not os.path.exists("data"):
    os.makedirs("data")

# Save file
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(data, f, indent=4)

print(f"Collected {len(data)} stories. Saved to {filename}")