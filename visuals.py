import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folder for saving images
output_folder = "charts"
os.makedirs(output_folder, exist_ok=True)


# Load data
df = pd.read_csv("/Users/bhupendrasingh/Desktop/Smart Product Intelligence Dashboard/final_df.csv")

# ==============================
# GRAPH 1: Revenue by Source
# ==============================
grouped_df = df.groupby("source")["revenue"].sum().reset_index()

plt.figure()
plt.bar(grouped_df["source"], grouped_df["revenue"])

plt.xlabel("Source")
plt.ylabel("Total Revenue")
plt.title("API vs Scraped Data Revenue Comparison")

# Save graph
plt.savefig(os.path.join(output_folder, "revenue_by_source.png"))

# Show graph
plt.show()


# ==============================
# GRAPH 2: Price Distribution
# ==============================
plt.figure()
plt.hist(df["price"], bins=10)

plt.xlabel("Price")
plt.ylabel("Number of Products")
plt.title("Price Distribution of Products")

# Save graph
plt.savefig(os.path.join(output_folder, "price_distribution.png"))
# Show graph
plt.show()

# GRAPH 3: Rating vs Price (Scatter Plot)
# ==============================
plt.figure()
plt.scatter(df["rating"], df["price"])

plt.xlabel("Rating")
plt.ylabel("Price")
plt.title("Rating vs Price Relationship")

# Save graph
plt.savefig(os.path.join(output_folder, "rating_vs_price.png"))

# Show graph
plt.show()

# ==============================