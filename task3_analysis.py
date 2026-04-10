# PRANESH.S
# Task 3: Analysis


import pandas as pd
import numpy as np

df = pd.read_csv("data/trends_clean.csv")

print(f"Loaded data: {df.shape}\n")
print(df.head())

# Averages
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score   : {avg_score:.0f}")
print(f"Average comments: {avg_comments:.0f}")

# NumPy stats
scores = df["score"].values

print("\n--- NumPy Stats ---")
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Std:", np.std(scores))
print("Max:", np.max(scores))
print("Min:", np.min(scores))

# Category analysis
print("\nMost stories in:", df["category"].value_counts().idxmax())

# Most commented story
top = df.loc[df["num_comments"].idxmax()]
print("Most commented:", top["title"], "-", top["num_comments"])

# New columns
df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > avg_score

# Save
df.to_csv("data/trends_analysed.csv", index=False)

print("\nSaved to data/trends_analysed.csv")