-- Total revenue by month
SELECT
    strftime('%Y-%m', date) AS month,
    SUM(total_revenue) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;

-- Revenue by region
SELECT
    region,
    SUM(total_revenue) AS revenue
FROM sales
GROUP BY region
ORDER BY revenue DESC;

-- Top products by revenue
SELECT
    product,
    SUM(total_revenue) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;
