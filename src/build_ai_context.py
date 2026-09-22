import json
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "dashboard" / "data"
REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(exist_ok=True)


def money(value):
    return f"₹{float(value):,.2f}"


# Load analytical datasets
monthly = pd.read_csv(DATA_DIR / "monthly_revenue.csv")
regions = pd.read_csv(DATA_DIR / "revenue_by_region.csv")
categories = pd.read_csv(DATA_DIR / "revenue_by_category.csv")
top_products = pd.read_csv(DATA_DIR / "top_products.csv")
trends = pd.read_csv(DATA_DIR / "trends_analysis.csv")
quality = pd.read_csv(DATA_DIR / "data_quality.csv")


# Normalize column names
monthly.columns = monthly.columns.str.lower().str.strip()
regions.columns = regions.columns.str.lower().str.strip()
categories.columns = categories.columns.str.lower().str.strip()
top_products.columns = top_products.columns.str.lower().str.strip()
trends.columns = trends.columns.str.lower().str.strip()
quality.columns = quality.columns.str.lower().str.strip()


# Identify key metrics
total_revenue = monthly["revenue"].sum()
highest_month = monthly.loc[monthly["revenue"].idxmax()]
lowest_month = monthly.loc[monthly["revenue"].idxmin()]

top_region = regions.loc[regions["revenue"].idxmax()]
top_category = categories.loc[categories["revenue"].idxmax()]

anomalies = []

if "anomaly" in trends.columns:
    for _, row in trends[trends["anomaly"] == True].iterrows():
        anomalies.append({
            "month": row.get("month"),
            "revenue": money(row.get("revenue", 0)),
            "z_score": round(float(row.get("z_score", 0)), 2)
        })


# Convert data-quality metrics to a dictionary
quality_metrics = {}

for _, row in quality.iterrows():
    quality_metrics[str(row["metric"])] = int(row["value"])


context = {
    "project": "AI Business Analytics & Insights Platform",
    "description": (
        "Business analytics system combining data validation, SQL analytics, "
        "Power BI reporting, statistical analysis, anomaly detection, and "
        "AI-ready business insight generation."
    ),
    "business_metrics": {
        "total_revenue": money(total_revenue),
        "months_analyzed": int(len(monthly)),
        "average_monthly_revenue": money(monthly["revenue"].mean()),
        "highest_month": {
            "month": str(highest_month["month"]),
            "revenue": money(highest_month["revenue"])
        },
        "lowest_month": {
            "month": str(lowest_month["month"]),
            "revenue": money(lowest_month["revenue"])
        }
    },
    "regional_performance": regions.to_dict(orient="records"),
    "category_performance": categories.to_dict(orient="records"),
    "top_products": top_products.head(10).to_dict(orient="records"),
    "anomalies": anomalies,
    "data_quality": quality_metrics,
    "ai_instructions": {
        "role": "Business Analyst",
        "objective": (
            "Explain the supplied business metrics clearly and identify "
            "actionable observations for business stakeholders."
        ),
        "rules": [
            "Use only the supplied data.",
            "Do not invent numerical values.",
            "Clearly distinguish observed facts from possible explanations.",
            "Highlight important trends, anomalies, and data-quality concerns.",
            "Provide concise, business-oriented recommendations."
        ]
    }
}


output = REPORT_DIR / "ai_business_context.json"

with open(output, "w", encoding="utf-8") as file:
    json.dump(context, file, indent=2, ensure_ascii=False)

print("AI-ready business context generated successfully.")
print(f"Context: {output}")