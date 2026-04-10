# PRANESH.S
# Task 4: Visualization

import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/trends_analysed.csv")

# Create folder
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# Top 10
top10 = df.sort_values(by="score", ascending=False).head(10)

plt.figure()
plt.barh(top10["title"], top10["score"])
plt.title("Top 10 Stories")
plt.savefig("outputs/chart1.png")
plt.close()

# Category chart
counts = df["category"].value_counts()

plt.figure()
plt.bar(counts.index, counts.values)
plt.title("Stories per Category")
plt.savefig("outputs/chart2.png")
plt.close()

# Scatter
plt.figure()
plt.scatter(df["score"], df["num_comments"])
plt.title("Score vs Comments")
plt.savefig("outputs/chart3.png")
plt.close()

print("Charts saved")