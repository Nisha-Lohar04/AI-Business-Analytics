import sqlite3
import pandas as pd

DB_PATH = "data/business_analytics.db"

connection = sqlite3.connect(DB_PATH)

# Load business metrics
region_df = pd.read_sql_query("""
    SELECT * FROM vw_revenue_by_region
    ORDER BY revenue DESC;
""", connection)

category_df = pd.read_sql_query("""
    SELECT * FROM vw_revenue_by_category
    ORDER BY revenue DESC;
""", connection)

monthly_df = pd.read_sql_query("""
    SELECT * FROM vw_monthly_revenue
    ORDER BY month;
""", connection)

connection.close()

print("\n========== AI BUSINESS INSIGHTS ==========\n")

# Revenue overview
total_revenue = monthly_df["revenue"].sum()
print(f"Total completed revenue: ₹{total_revenue:,.2f}")

# Top region
top_region = region_df.iloc[0]
print(
    f"Top-performing region: {top_region['region']} "
    f"with ₹{top_region['revenue']:,.2f} revenue."
)

# Top category
top_category = category_df.iloc[0]
print(
    f"Top-performing category: {top_category['category']} "
    f"with ₹{top_category['revenue']:,.2f} revenue."
)

# Best growth month
monthly_df["mom_growth_pct"] = monthly_df["revenue"].pct_change() * 100
best_growth = monthly_df.iloc[monthly_df["mom_growth_pct"].idxmax()]

print(
    f"Highest month-over-month growth: {best_growth['month']} "
    f"at {best_growth['mom_growth_pct']:.2f}%."
)

# Largest decline
largest_decline = monthly_df.iloc[monthly_df["mom_growth_pct"].idxmin()]

print(
    f"Largest month-over-month decline: {largest_decline['month']} "
    f"at {largest_decline['mom_growth_pct']:.2f}%."
)

# Anomaly detection
mean = monthly_df["revenue"].mean()
std = monthly_df["revenue"].std()

monthly_df["z_score"] = (
    monthly_df["revenue"] - mean
) / std

anomalies = monthly_df[monthly_df["z_score"].abs() > 2]

if not anomalies.empty:
    print("\nPotential revenue anomalies:")
    for _, row in anomalies.iterrows():
        print(
            f"- {row['month']}: ₹{row['revenue']:,.2f} "
            f"(z-score: {row['z_score']:.2f})"
        )
else:
    print("\nNo significant revenue anomalies detected.")

print("\n==========================================")