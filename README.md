# AI Business Analytics & Insights Platform

End-to-end business analytics platform combining data validation, SQL analytics, Python analysis, Power BI reporting, anomaly detection, and AI-assisted business insights.

## Overview
This project transforms raw business data into validated datasets, analytical metrics, interactive dashboards, and an AI-generated business analysis report.

The workflow combines Python, SQL, Power BI, statistical analysis, and LLMs, with validation layers to keep analytical outputs grounded in the underlying data.

## Architecture

```text
Raw Business Data
        ↓
Data Validation
        ↓
Data Cleaning
        ↓
SQLite Database
        ↓
SQL Analytics ──────────┐
        ↓               │
Python Analytics        │
        ↓               │
Power BI Dashboard      │
                        ↓
              AI-Ready Business Context
                        ↓
               AI Business Analyst
                        ↓
                Report Validation

```

## Key Capabilities

- Data quality validation and cleaning
- SQL-based business analytics
- Revenue, order, product, category, region, and customer-segment analysis
- Monthly trend and growth analysis
- Statistical anomaly detection
- Power BI dashboard generation
- AI-ready structured business context
- LLM-powered business analysis
- Automated validation of AI-generated reports
- End-to-end pipeline automation

## Data Quality

The pipeline intentionally introduces common data-quality issues to demonstrate validation and cleaning.

| Metric | Result |
|---|---:|
| Raw order records | 10,012 |
| Clean order records | 9,987 |
| Duplicate order IDs | 12 |
| Missing customer IDs | 7 |
| Invalid discounts | 4 |
| Invalid quantities | 2 |
| Rows removed during cleaning | 25 |

## Business Analytics

The cleaned dataset is loaded into SQLite and analyzed using SQL and Python.

Key metrics include:

- **Completed Revenue:** ₹757.79M
- **Completed Orders:** 8,030
- **Average Monthly Revenue:** ₹37.89M
- **Highest Revenue Region:** West
- **Highest Revenue Category:** Industrial
- **Detected Revenue Anomalies:** 1

The analytics layer also calculates:

- Monthly revenue
- Month-over-month growth
- Moving averages
- Regional performance
- Category performance
- Customer-segment performance
- Top products

## Power BI Dashboard

The Power BI dashboard contains three analytical views:

### Executive Overview

- Total revenue
- Completed orders
- Average order value
- Monthly revenue trend
- Revenue by region
- Revenue by category
- Customer-segment performance

### Trends & Anomalies

- Revenue trend
- 3-month moving average
- Monthly revenue growth
- Revenue anomalies
- Top 10 products

### Data Quality

- Data volume
- Detected data-quality issues
- Cleaning results

## AI Business Analyst

The platform converts validated analytical outputs into a structured business context before sending them to the LLM.

The AI layer generates:

- Executive summaries
- Key business findings
- Regional and category observations
- Trend analysis
- Anomaly explanations
- Data-quality observations
- Investigation-oriented recommendations

The LLM is used as an **analysis and reporting layer**, while the underlying metrics are calculated deterministically through the data pipeline.

## AI Report Validation

AI-generated reports are automatically validated against the structured business context.

The validation layer checks the presence of **13 critical analytical values**, including:

- Total revenue
- Monthly revenue metrics
- Regional revenue
- Category revenue
- Detected anomaly values

This provides a validation step between AI-generated output and the underlying analytical results.

## Automated Pipeline

Run the complete workflow with:

```bash
python run_pipeline.py
```
Pipeline flow:

```text
Validate
→ Build AI Context
→ Clean
→ Load Database
→ Export Power BI Data
→ Export Trends
→ Export Top Products
→ Export Data Quality
→ Generate Business Insights
→ Generate AI Report
→ Validate AI Report
```

## Tech Stack

| Area | Technologies |
|---|---|
| Programming | Python, SQL |
| Data Analysis | Pandas, NumPy, Statistical Analysis |
| Database | SQLite |
| Data | CSV |
| Visualization | Microsoft Power BI |
| AI | Groq API, OpenAI-Compatible LLM |
| Development | Git, GitHub, VS Code |

## Project Structure

```text
AI-Business-Analytics/
│
├── data/                       # Raw and cleaned datasets
├── sql/                        # SQL analytics and views
├── src/                        # Validation, analytics and AI pipeline
├── dashboard/                  # Power BI dashboard and exported data
├── reports/                    # Generated analytical reports
├── docs/                       # Supporting documentation
│
├── run_pipeline.py             # End-to-end pipeline
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Nisha-Lohar04/AI-Business-Analytics.git
cd AI-Business-Analytics
```
### 2. Create a Virtual Environment

```bash
python -m venv .venv
```
### 3. Activate the Environment

Windows
```bash
.venv\Scripts\Activate.ps1
```
### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
### 5. Configure Environment Variables

Create a .env file in the project root:
```bash
GROQ_API_KEY=your_api_key
```
### 6. Run the Pipeline
```bash
python run_pipeline.py
```
### Outcome
The project demonstrates an end-to-end workflow for data-driven business analysis and AI-assisted decision support, combining validated data processing, SQL analytics, statistical analysis, Power BI reporting, and a grounded LLM layer.
```bash
Data → Validation → Analytics → Visualization → AI Insights → Validation
```
