-- 1. Total Revenue
SELECT
    ROUND(SUM(revenue), 2) AS total_revenue
FROM orders
WHERE status = 'Completed';


-- 2. Total Orders
SELECT
    COUNT(*) AS total_orders
FROM orders
WHERE status = 'Completed';


-- 3. Revenue by Region
SELECT
    c.region,
    ROUND(SUM(o.revenue), 2) AS revenue
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
WHERE o.status = 'Completed'
GROUP BY c.region
ORDER BY revenue DESC;


-- 4. Revenue by Product Category
SELECT
    p.category,
    ROUND(SUM(o.revenue), 2) AS revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
WHERE o.status = 'Completed'
GROUP BY p.category
ORDER BY revenue DESC;


-- 5. Monthly Revenue
SELECT
    strftime('%Y-%m', o.order_date) AS month,
    ROUND(SUM(o.revenue), 2) AS revenue
FROM orders o
WHERE o.status = 'Completed'
GROUP BY month
ORDER BY month;


-- 6. Top 10 Products
SELECT
    p.product_name,
    p.category,
    ROUND(SUM(o.revenue), 2) AS revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
WHERE o.status = 'Completed'
GROUP BY p.product_id, p.product_name, p.category
ORDER BY revenue DESC
LIMIT 10;


-- 7. Customer Segment Performance
SELECT
    c.segment,
    COUNT(DISTINCT c.customer_id) AS customers,
    ROUND(SUM(o.revenue), 2) AS revenue
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
WHERE o.status = 'Completed'
GROUP BY c.segment
ORDER BY revenue DESC;


-- 8. Average Order Value
SELECT
    ROUND(AVG(revenue), 2) AS average_order_value
FROM orders
WHERE status = 'Completed';