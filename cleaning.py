import pandas as pd
df = pd.read_json("api_data.json")
df1 = pd.read_json("data.json")
# print(df.head(),df.info())
# print(df1.head(),df1.info())
# print(df1[["price","rating"]])
rating_map={
    "One":1,
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5
}
df1["price"]=df1["price"].str.replace("Â£","₹")
df1["rating"]=df1["rating"].map(rating_map)
# print(df1[["price","rating"]])

# print(df1.isnull())
# print(df.isnull(),df.info(),df.dtypes)
# print(df.columns)
# print(df1.columns)
df_copy = df.copy()
df1_copy = df1.copy()
df_copy=df_copy.drop(["id","description","category","image"] ,axis=1)
# print(df_copy.columns)
# print(df1_copy.columns)

merged_df=pd.concat([df_copy,df1_copy],axis=1)

# print(merged_df.columns)
# print(merged_df.head())
merged_df.to_csv("merged_data.csv", index=False)
# print(df_copy["title"].head())
# print(df1_copy["title"].head())

# Step 1: Rename columns properly

df_copy = df_copy[["title", "price", "rating"]]
df1_copy = df1_copy[["title", "price", "rating"]]

# Step 2: Add source column
df_copy["source"] = "API"
df1_copy["source"] = "BOOK"

# Step 3: Combine vertically
final_df = pd.concat([df_copy, df1_copy], axis=0)

# Step 4: Reset index
final_df.reset_index(drop=True, inplace=True)

print(final_df.head())

# Save
# final_df.to_csv("final_clean_data.csv", index=False)

import numpy as np
final_df["random_quantity"] = np.random.randint(300, 980, size=len(final_df))

# Create clean numeric revenue
# final_df["revenue"] = final_df["price"] * final_df["random_quantity"]

# Optional: create formatted currency column
# final_df["revenue_inr"] = "₹" + final_df["revenue"].astype(str)
final_df["price"]=final_df["price"].astype(str).str.replace("₹","").astype(float)
final_df["revenue"]=final_df["price"] * final_df["random_quantity"]
# final_df["revenue_inr"] = "₹" + final_df["revenue"].round(2).astype(str)

print(final_df[["random_quantity", "revenue"]].head())

# Save final merged clean dataset



from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/smart_dashboard")

conn = engine.connect()
print("Connected ✅")
# Fix API rating (dict → float)
final_df["rating"] = final_df["rating"].apply(
    lambda x: x["rate"] if isinstance(x, dict) else x
)
final_df.to_csv("final_df.csv", index=False)
print(final_df.info())
print(final_df.isnull().sum())
final_df.to_sql("products", con=engine, if_exists="replace", index=False)
