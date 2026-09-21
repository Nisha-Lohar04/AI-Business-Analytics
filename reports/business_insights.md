# AI Business Analytics — Business Insights

> Automated business intelligence report generated from validated transactional data using Python analytics.

## KPI Summary

| KPI | Value |
|---|---:|
| Total Revenue | ₹757,792,265.35 |
| Average Monthly Revenue | ₹37,889,613.27 |
| Highest Monthly Revenue | ₹41,618,124.22 |
| Lowest Monthly Revenue | ₹33,543,730.10 |
| Highest Revenue Region | West |
| Highest Revenue Category | Industrial |
| Detected Anomalies | 1 |
| Data Quality Issues | 25 |

## Executive Summary

- Total analyzed revenue was ₹757,792,265.35 across 20 months of data.
- The highest-revenue month was July 2025 with revenue of ₹41,618,124.22.
- West generated the highest regional revenue at ₹218,215,050.22, representing 28.8% of total revenue.
- Industrial was the highest-revenue category at ₹234,643,637.47, representing 31.0% of total revenue.
- The strongest month-over-month revenue growth occurred in May 2025 at 14.18%.
- The largest month-over-month revenue decline occurred in September 2025 at -10.73%.
- Moderate-severity anomaly detected in February 2025: revenue was below the historical average (z-score -2.14).
- Data-quality validation identified 25 issues before cleaning. The cleaning process reduced the raw dataset from 10,012 to 9,987 order records.

## Regional Performance

| Region | Revenue | Share |
|---|---:|---:|
| West | ₹218,215,050.22 | 28.8% |
| North | ₹192,599,106.68 | 25.4% |
| East | ₹187,053,926.51 | 24.7% |
| South | ₹159,924,181.94 | 21.1% |

## Category Performance

| Category | Revenue | Share |
|---|---:|---:|
| Industrial | ₹234,643,637.47 | 31.0% |
| Consumer | ₹205,088,972.83 | 27.1% |
| Food | ₹170,506,648.90 | 22.5% |
| Agriculture | ₹147,553,006.15 | 19.5% |

## Data Quality

| Metric | Count |
|---|---:|
| Raw Orders | 10,012 |
| Clean Orders | 9,987 |
| Duplicate Order IDs | 12 |
| Missing Customer IDs | 7 |
| Invalid Discounts | 4 |
| Invalid Quantities | 2 |

**Cleaning reduction:** 10,012 → 9,987 records (0.25% reduction).

## Recommended Actions

1. Investigate the period with the largest revenue decline to determine the underlying business drivers.
2. Monitor regional performance regularly and evaluate changes in regional contribution over time.
3. Track category-level revenue trends to identify growth opportunities and underperforming segments.
4. Monitor statistically significant anomalies as part of the regular reporting workflow.
5. Continue automated data-quality validation before business reporting and dashboard refreshes.
