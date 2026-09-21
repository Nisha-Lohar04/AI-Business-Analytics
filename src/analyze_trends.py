import sqlite3
import pandas as pd

DB_PATH = "data/business_analytics.db"

connection = sqlite3.connect(DB_PATH)

# Load monthly revenue
df = pd.read_sql_query("""
    SELECT *
    FROM vw_monthly_revenue
    ORDER BY month;
""", connection)

# Calculate month-over-month growth
df["mom_growth_pct"] = df["revenue"].pct_change() * 100

# Calculate rolling average
df["rolling_3_month_avg"] = df["revenue"].rolling(3).mean()

# Detect revenue anomalies using z-score
mean = df["revenue"].mean()
std = df["revenue"].std()

df["z_score"] = (df["revenue"] - mean) / std
df["anomaly"] = df["z_score"].abs() > 2

print("\n========== TREND & ANOMALY ANALYSIS ==========\n")

print("Monthly Revenue Analysis:")
print(
    df[
        [
            "month",
            "revenue",
            "mom_growth_pct",
            "rolling_3_month_avg",
            "anomaly"
        ]
    ].round(2).to_string(index=False)
)

print("\n========== ANOMALIES ==========\n")

anomalies = df[df["anomaly"]]

if anomalies.empty:
    print("No significant revenue anomalies detected.")
else:
    print(anomalies[["month", "revenue", "z_score"]].round(2).to_string(index=False))

print("\n========== TOP GROWTH MONTHS ==========\n")

growth = df.dropna(subset=["mom_growth_pct"])
print(
    growth.nlargest(5, "mom_growth_pct")[
        ["month", "mom_growth_pct"]
    ].round(2).to_string(index=False)
)

connection.close()