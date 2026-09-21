import sqlite3
import pandas as pd
import os

DB_PATH = "data/business_analytics.db"
OUTPUT_PATH = "dashboard/data/trends_analysis.csv"

os.makedirs("dashboard/data", exist_ok=True)

connection = sqlite3.connect(DB_PATH)

df = pd.read_sql_query("""
    SELECT *
    FROM vw_monthly_revenue
    ORDER BY month;
""", connection)

# Month-over-month growth
df["mom_growth_pct"] = df["revenue"].pct_change() * 100

# 3-month rolling average
df["rolling_3_month_avg"] = df["revenue"].rolling(3).mean()

# Z-score anomaly detection
mean = df["revenue"].mean()
std = df["revenue"].std()

df["z_score"] = (df["revenue"] - mean) / std
df["anomaly"] = df["z_score"].abs() > 2

df.to_csv(OUTPUT_PATH, index=False)

connection.close()

print(f"Exported: {OUTPUT_PATH}")
print(f"Rows: {len(df)}")