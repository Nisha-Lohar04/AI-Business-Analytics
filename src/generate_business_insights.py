import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "dashboard" / "data"
REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(exist_ok=True)

# ============================================================
# LOAD DATA
# ============================================================

monthly = pd.read_csv(DATA_DIR / "monthly_revenue.csv")
region = pd.read_csv(DATA_DIR / "revenue_by_region.csv")
category = pd.read_csv(DATA_DIR / "revenue_by_category.csv")
quality = pd.read_csv(DATA_DIR / "data_quality.csv")

# ============================================================
# PREPARE DATA
# ============================================================

monthly["month"] = pd.to_datetime(monthly["month"])
monthly = monthly.sort_values("month").reset_index(drop=True)

monthly["mom_growth_pct"] = monthly["revenue"].pct_change() * 100

# ============================================================
# KPI ANALYSIS
# ============================================================

total_revenue = region["revenue"].sum()

total_months = len(monthly)

average_monthly_revenue = monthly["revenue"].mean()

highest_month = monthly.loc[monthly["revenue"].idxmax()]
lowest_month = monthly.loc[monthly["revenue"].idxmin()]

highest_growth = monthly.loc[
    monthly["mom_growth_pct"].idxmax()
]

largest_decline = monthly.loc[
    monthly["mom_growth_pct"].idxmin()
]

# ============================================================
# REGIONAL ANALYSIS
# ============================================================

top_region = region.loc[
    region["revenue"].idxmax()
]

region_share = (
    top_region["revenue"] / total_revenue
) * 100

region_sorted = region.sort_values(
    "revenue",
    ascending=False
)

# ============================================================
# CATEGORY ANALYSIS
# ============================================================

top_category = category.loc[
    category["revenue"].idxmax()
]

category_share = (
    top_category["revenue"] / total_revenue
) * 100

category_sorted = category.sort_values(
    "revenue",
    ascending=False
)

# ============================================================
# ANOMALY DETECTION
# ============================================================

mean_revenue = monthly["revenue"].mean()
std_revenue = monthly["revenue"].std()

monthly["z_score"] = (
    monthly["revenue"] - mean_revenue
) / std_revenue

anomalies = monthly[
    monthly["z_score"].abs() > 2
].copy()

# ============================================================
# DATA QUALITY ANALYSIS
# ============================================================

quality_metrics = {
    row["metric"]: int(row["value"])
    for _, row in quality.iterrows()
}

raw_orders = quality_metrics.get("Raw Orders", 0)
clean_orders = quality_metrics.get("Clean Orders", 0)

duplicate_orders = quality_metrics.get(
    "Duplicate Order IDs", 0
)

missing_customers = quality_metrics.get(
    "Missing Customer IDs", 0
)

invalid_discounts = quality_metrics.get(
    "Invalid Discounts", 0
)

invalid_quantities = quality_metrics.get(
    "Invalid Quantities", 0
)

total_quality_issues = (
    duplicate_orders
    + missing_customers
    + invalid_discounts
    + invalid_quantities
)

cleaning_reduction = (
    ((raw_orders - clean_orders) / raw_orders) * 100
    if raw_orders
    else 0
)

# ============================================================
# BUSINESS INSIGHTS
# ============================================================

insights = []

insights.append(
    f"Total analyzed revenue was "
    f"₹{total_revenue:,.2f} across "
    f"{total_months} months of data."
)

insights.append(
    f"The highest-revenue month was "
    f"{highest_month['month'].strftime('%B %Y')} "
    f"with revenue of ₹{highest_month['revenue']:,.2f}."
)

insights.append(
    f"{top_region['region']} generated the highest regional revenue "
    f"at ₹{top_region['revenue']:,.2f}, representing "
    f"{region_share:.1f}% of total revenue."
)

insights.append(
    f"{top_category['category']} was the highest-revenue category "
    f"at ₹{top_category['revenue']:,.2f}, representing "
    f"{category_share:.1f}% of total revenue."
)

insights.append(
    f"The strongest month-over-month revenue growth occurred in "
    f"{highest_growth['month'].strftime('%B %Y')} "
    f"at {highest_growth['mom_growth_pct']:.2f}%."
)

insights.append(
    f"The largest month-over-month revenue decline occurred in "
    f"{largest_decline['month'].strftime('%B %Y')} "
    f"at {largest_decline['mom_growth_pct']:.2f}%."
)

# ============================================================
# ANOMALY INSIGHTS
# ============================================================

if len(anomalies) > 0:

    for _, row in anomalies.iterrows():

        direction = (
            "above"
            if row["z_score"] > 0
            else "below"
        )

        severity = (
            "High"
            if abs(row["z_score"]) >= 3
            else "Moderate"
        )

        insights.append(
            f"{severity}-severity anomaly detected in "
            f"{row['month'].strftime('%B %Y')}: revenue was "
            f"{direction} the historical average "
            f"(z-score {row['z_score']:.2f})."
        )

else:

    insights.append(
        "No statistically significant monthly revenue anomalies "
        "were detected using the |z-score| > 2 threshold."
    )

# ============================================================
# DATA QUALITY INSIGHT
# ============================================================

if total_quality_issues > 0:

    insights.append(
        f"Data-quality validation identified "
        f"{total_quality_issues} issues before cleaning. "
        f"The cleaning process reduced the raw dataset from "
        f"{raw_orders:,} to {clean_orders:,} order records."
    )

# ============================================================
# GENERATE REPORT
# ============================================================

report_path = REPORTS_DIR / "business_insights.md"

with open(report_path, "w", encoding="utf-8") as f:

    f.write("# AI Business Analytics — Business Insights\n\n")

    f.write(
        "> Automated business intelligence report generated "
        "from validated transactional data using Python analytics.\n\n"
    )

    # --------------------------------------------------------
    # KPI SUMMARY
    # --------------------------------------------------------

    f.write("## KPI Summary\n\n")

    f.write("| KPI | Value |\n")
    f.write("|---|---:|\n")

    f.write(
        f"| Total Revenue | ₹{total_revenue:,.2f} |\n"
    )

    f.write(
        f"| Average Monthly Revenue | "
        f"₹{average_monthly_revenue:,.2f} |\n"
    )

    f.write(
        f"| Highest Monthly Revenue | "
        f"₹{highest_month['revenue']:,.2f} |\n"
    )

    f.write(
        f"| Lowest Monthly Revenue | "
        f"₹{lowest_month['revenue']:,.2f} |\n"
    )

    f.write(
        f"| Highest Revenue Region | "
        f"{top_region['region']} |\n"
    )

    f.write(
        f"| Highest Revenue Category | "
        f"{top_category['category']} |\n"
    )

    f.write(
        f"| Detected Anomalies | "
        f"{len(anomalies)} |\n"
    )

    f.write(
        f"| Data Quality Issues | "
        f"{total_quality_issues} |\n\n"
    )

    # --------------------------------------------------------
    # EXECUTIVE SUMMARY
    # --------------------------------------------------------

    f.write("## Executive Summary\n\n")

    for insight in insights:
        f.write(f"- {insight}\n")

    # --------------------------------------------------------
    # REGIONAL PERFORMANCE
    # --------------------------------------------------------

    f.write("\n## Regional Performance\n\n")

    f.write("| Region | Revenue | Share |\n")
    f.write("|---|---:|---:|\n")

    for _, row in region_sorted.iterrows():

        share = (
            row["revenue"] / total_revenue
        ) * 100

        f.write(
            f"| {row['region']} | "
            f"₹{row['revenue']:,.2f} | "
            f"{share:.1f}% |\n"
        )

    # --------------------------------------------------------
    # CATEGORY PERFORMANCE
    # --------------------------------------------------------

    f.write("\n## Category Performance\n\n")

    f.write("| Category | Revenue | Share |\n")
    f.write("|---|---:|---:|\n")

    for _, row in category_sorted.iterrows():

        share = (
            row["revenue"] / total_revenue
        ) * 100

        f.write(
            f"| {row['category']} | "
            f"₹{row['revenue']:,.2f} | "
            f"{share:.1f}% |\n"
        )

    # --------------------------------------------------------
    # DATA QUALITY
    # --------------------------------------------------------

    f.write("\n## Data Quality\n\n")

    f.write("| Metric | Count |\n")
    f.write("|---|---:|\n")

    for metric, value in quality_metrics.items():

        f.write(
            f"| {metric} | {value:,} |\n"
        )

    f.write(
        f"\n**Cleaning reduction:** "
        f"{raw_orders:,} → {clean_orders:,} records "
        f"({cleaning_reduction:.2f}% reduction).\n"
    )

    # --------------------------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------------------------

    f.write("\n## Recommended Actions\n\n")

    f.write(
        "1. Investigate the period with the largest revenue decline "
        "to determine the underlying business drivers.\n"
    )

    f.write(
        "2. Monitor regional performance regularly and evaluate "
        "changes in regional contribution over time.\n"
    )

    f.write(
        "3. Track category-level revenue trends to identify "
        "growth opportunities and underperforming segments.\n"
    )

    f.write(
        "4. Monitor statistically significant anomalies as part "
        "of the regular reporting workflow.\n"
    )

    f.write(
        "5. Continue automated data-quality validation before "
        "business reporting and dashboard refreshes.\n"
    )

print("Business insights generated successfully.")
print(f"Report: {report_path}")