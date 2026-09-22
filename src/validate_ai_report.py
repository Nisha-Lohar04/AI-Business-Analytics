import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

CONTEXT_FILE = BASE_DIR / "reports" / "ai_business_context.json"
REPORT_FILE = BASE_DIR / "reports" / "ai_business_insights.md"


def extract_numbers(text):
    """Return normalized numeric strings found in text."""
    return re.findall(r"\d[\d,]*\.\d{2}", text)


def validate_report():
    with open(CONTEXT_FILE, "r", encoding="utf-8") as file:
        context = json.load(file)

    with open(REPORT_FILE, "r", encoding="utf-8") as file:
        report = file.read()

    expected_values = []

    metrics = context["business_metrics"]

    expected_values.append(metrics["total_revenue"])
    expected_values.append(metrics["average_monthly_revenue"])
    expected_values.append(metrics["highest_month"]["revenue"])
    expected_values.append(metrics["lowest_month"]["revenue"])

    for row in context["regional_performance"]:
        expected_values.append(f'₹{float(row["revenue"]):,.2f}')

    for row in context["category_performance"]:
        expected_values.append(f'₹{float(row["revenue"]):,.2f}')

    for anomaly in context["anomalies"]:
        expected_values.append(anomaly["revenue"])

    missing = []

    for value in expected_values:
        if value.replace("₹", "") not in report:
            missing.append(value)

    print("\n========== AI REPORT VALIDATION ==========")

    if missing:
        print("VALIDATION FAILED")
        print("\nMissing expected values:")

        for value in missing:
            print(f"  ✗ {value}")

        raise SystemExit(1)

    print("VALIDATION PASSED")
    print(f"Checked {len(expected_values)} critical values.")
    print("All expected analytical values are present in the AI report.")
    print("==========================================\n")


if __name__ == "__main__":
    validate_report()