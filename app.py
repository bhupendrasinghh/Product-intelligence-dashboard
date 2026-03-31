from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load data once (optimization)
df = pd.read_csv("data/final_df.csv")

# Pre-compute useful datasets
top_products = df.sort_values(by="revenue", ascending=False).head(5)
high_price = df.sort_values(by="price", ascending=False).head(5)

@app.route("/")
def home():
    table = df.to_html(classes="table table-bordered table-hover", index=False)

    insights = [
        f"Total Revenue: ₹{int(df['revenue'].sum())}",
        f"Average Price: ₹{round(df['price'].mean(), 2)}",
        f"Highest Revenue Product: {df.loc[df['revenue'].idxmax()]['title']}",
        f"Average Rating: {round(df['rating'].mean(), 2)}"
    ]

    return render_template(
        "index.html",
        table=table,
        insights=insights
    )

@app.route("/top-products")
def top():
    table = top_products.to_html(classes="table table-striped", index=False)
    return render_template("top.html", table=table)

@app.route("/high-price")
def expensive():
    table = high_price.to_html(classes="table table-striped", index=False)
    return render_template("top.html", table=table)

if __name__ == "__main__":
    app.run(debug=True)