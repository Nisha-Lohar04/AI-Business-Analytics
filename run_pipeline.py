import subprocess
import sys


STEPS = [
    ("Validate data", "src/validate_data.py"),
    ("Build AI context", "src/build_ai_context.py"),
    ("Clean data", "src/clean_data.py"),
    ("Load database", "src/load_database.py"),
    ("Export Power BI data", "src/export_powerbi_data.py"),
    ("Export trend analysis", "src/export_trends.py"),
    ("Export top products", "src/export_top_products.py"),
    ("Export data quality", "src/export_quality.py"),
    ("Generate business insights", "src/generate_business_insights.py"),
]


def run_step(name, script):
    print("\n" + "=" * 60)
    print(f"STEP: {name}")
    print("=" * 60)

    result = subprocess.run(
        [sys.executable, script],
        capture_output=True,
        text=True
    )

    if result.stdout:
        print(result.stdout)

    if result.returncode != 0:
        if result.stderr:
            print(result.stderr)

        print(f"\nPipeline stopped: {name} failed.")
        sys.exit(result.returncode)


def main():
    print("=" * 60)
    print("AI BUSINESS ANALYTICS PIPELINE")
    print("=" * 60)

    for name, script in STEPS:
        run_step(name, script)

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)
    print("\nGenerated outputs:")
    print("- SQLite database: data/business_analytics.db")
    print("- Power BI datasets: dashboard/data/")
    print("- Business insights: reports/business_insights.md")


if __name__ == "__main__":
    main()