from sqlalchemy import create_engine
import pandas as pd
import numpy as np
engine = create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/smart_dashboard")

def get_data():
    query = "SELECT * FROM products"
    df = pd.read_sql(query, con=engine)
    return df

def top_products():
    query="""
    SELECT title, revenue
    FROM products
    ORDER BY revenue DESC
    LIMIT 10
    """
    return pd.read_sql(query, engine)
def revenue_by_source():
    query = """
    SELECT source, SUM(revenue) as total_revenue
    FROM products
    GROUP BY source
    """
    return pd.read_sql(query, engine)

def avg_rating():
    query = """
    SELECT source, AVG(rating) as avg_rating
    FROM products
    GROUP BY source
    """
    return pd.read_sql(query, engine)