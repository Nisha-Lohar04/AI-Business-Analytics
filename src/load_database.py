import pandas as pd
import sqlite3
from pathlib import Path

DB_PATH = "data/business_analytics.db"

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders_clean.csv")

# Calculate actual revenue using product price
orders = orders.merge(
    products[["product_id", "unit_price"]],
    on="product_id",
    how="left"
)

orders["revenue"] = (
    orders["quantity"]
    * orders["unit_price"]
    * (1 - orders["discount"])
)

# Connect to SQLite
connection = sqlite3.connect(DB_PATH)

# Load tables
customers.to_sql("customers", connection, if_exists="replace", index=False)
products.to_sql("products", connection, if_exists="replace", index=False)
orders.to_sql("orders", connection, if_exists="replace", index=False)

connection.close()

print("========== DATABASE CREATED ==========")
print(f"Customers: {len(customers)}")
print(f"Products: {len(products)}")
print(f"Orders: {len(orders)}")
print(f"Database: {Path(DB_PATH).resolve()}")