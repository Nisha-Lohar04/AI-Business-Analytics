import sqlite3
import pandas as pd
import os

DB_PATH = "data/business_analytics.db"
OUTPUT_DIR = "dashboard/data"

os.makedirs(OUTPUT_DIR, exist_ok=True)

connection = sqlite3.connect(DB_PATH)

exports = {
    "revenue_by_region": "SELECT * FROM vw_revenue_by_region",
    "revenue_by_category": "SELECT * FROM vw_revenue_by_category",
    "monthly_revenue": "SELECT * FROM vw_monthly_revenue",
    "customer_segment_performance": "SELECT * FROM vw_customer_segment_performance",
}

for filename, query in exports.items():
    df = pd.read_sql_query(query, connection)
    path = f"{OUTPUT_DIR}/{filename}.csv"
    df.to_csv(path, index=False)
    print(f"Exported: {path}")

connection.close()

print("\nPower BI datasets exported successfully.")