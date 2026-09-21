CREATE VIEW IF NOT EXISTS vw_revenue_by_region AS
SELECT
    c.region,
    ROUND(SUM(o.revenue), 2) AS revenue
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
WHERE o.status = 'Completed'
GROUP BY c.region;


CREATE VIEW IF NOT EXISTS vw_revenue_by_category AS
SELECT
    p.category,
    ROUND(SUM(o.revenue), 2) AS revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
WHERE o.status = 'Completed'
GROUP BY p.category;


CREATE VIEW IF NOT EXISTS vw_monthly_revenue AS
SELECT
    strftime('%Y-%m', order_date) AS month,
    ROUND(SUM(revenue), 2) AS revenue
FROM orders
WHERE status = 'Completed'
GROUP BY month;


CREATE VIEW IF NOT EXISTS vw_customer_segment_performance AS
SELECT
    c.segment,
    COUNT(DISTINCT o.customer_id) AS customers,
    COUNT(o.order_id) AS orders,
    ROUND(SUM(o.revenue), 2) AS revenue
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
WHERE o.status = 'Completed'
GROUP BY c.segment;