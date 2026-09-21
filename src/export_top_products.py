import sqlite3
import pandas as pd
import os

DB_PATH = "data/business_analytics.db"
OUTPUT_PATH = "dashboard/data/top_products.csv"

os.makedirs("dashboard/data", exist_ok=True)

connection = sqlite3.connect(DB_PATH)

df = pd.read_sql_query("""
    SELECT *
    FROM vw_top_products
    LIMIT 10;
""", connection)

df.to_csv(OUTPUT_PATH, index=False)

connection.close()

print(f"Exported: {OUTPUT_PATH}")
print(f"Rows: {len(df)}")
print("\nTop products:")
print(df.to_string(index=False))