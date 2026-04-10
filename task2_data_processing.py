# PRANESH.S
# Task 2: Clean data

import pandas as pd
import glob
import os

# Get latest JSON file
files = glob.glob("data/trends_*.json")
latest_file = max(files, key=os.path.getctime)

# Load data
df = pd.read_json(latest_file)
print(f"Loaded {len(df)} stories from {latest_file}")

# Remove duplicates
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Remove missing values
df = df.dropna(subset=["post_id","title","score"])
print(f"After removing nulls: {len(df)}")

# Convert types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low score
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Clean title
df["title"] = df["title"].str.strip()

# Save CSV
df.to_csv("data/trends_clean.csv", index=False)

print(f"\nSaved {len(df)} rows to data/trends_clean.csv\n")
print("Stories per category:")
print(df["category"].value_counts())