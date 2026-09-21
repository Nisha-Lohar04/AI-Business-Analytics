CREATE VIEW IF NOT EXISTS vw_top_products AS
SELECT
    p.product_id,
    p.product_name,
    p.category,
    ROUND(SUM(o.revenue), 2) AS revenue,
    SUM(o.quantity) AS units_sold
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
WHERE o.status = 'Completed'
GROUP BY
    p.product_id,
    p.product_name,
    p.category
ORDER BY revenue DESC;