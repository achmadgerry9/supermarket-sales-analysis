-- ======================================
-- Supermarket Sales Analysis
-- SQL Analysis
-- ======================================

-- ======================================
-- 1. Overall Business Performance
-- ======================================

SELECT
    COUNT(*) AS total_transactions,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(total), 2) AS total_revenue,
    ROUND(SUM(gross_income), 2) AS total_gross_income,
    ROUND(AVG(total), 2) AS average_transaction_value,
    ROUND(AVG(gross_income), 2) AS average_gross_income_per_transaction
FROM supermarket_sales;

-- ======================================
-- 2. Branch breakdown
-- ======================================

SELECT
    branch,
    COUNT(*) AS total_transactions,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(total), 2) AS total_revenue,
    ROUND(SUM(gross_income), 2) AS total_gross_income,
    ROUND(AVG(total), 2) AS average_transaction_value
FROM supermarket_sales
GROUP BY branch
ORDER BY total_revenue DESC;

-- ======================================
-- 3. Product Line Performance
-- ======================================

SELECT
    product_line,
    COUNT(*) AS total_transactions,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(total), 2) AS total_revenue,
    ROUND(SUM(gross_income), 2) AS total_gross_income,
    ROUND(AVG(total), 2) AS average_transaction_value
FROM supermarket_sales
GROUP BY product_line
ORDER BY total_revenue DESC;

-- ======================================
-- 4. Branch Revenue Contribution
-- ======================================

SELECT
    branch,
    ROUND(SUM(total), 2) AS total_revenue,
    ROUND(
        SUM(total) * 100.0 /
        SUM(SUM(total)) OVER (),
        2
    ) AS revenue_percentage
FROM supermarket_sales
GROUP BY branch
ORDER BY total_revenue DESC;

-- ======================================
-- 5. Monthly Sales Performance
-- ======================================

SELECT
    DATE_TRUNC('month', date) AS month,
    COUNT(*) AS total_transactions,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(total), 2) AS total_revenue,
    ROUND(SUM(gross_income), 2) AS total_gross_income,
    ROUND(AVG(total), 2) AS average_transaction_value
FROM supermarket_sales
GROUP BY DATE_TRUNC('month', date)
ORDER BY month;

-- ======================================
-- 6. Customer Type Performance
-- ======================================

SELECT
    customer_type,
    COUNT(*) AS total_transactions,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(total), 2) AS total_revenue,
    ROUND(SUM(gross_income), 2) AS total_gross_income,
    ROUND(AVG(total), 2) AS average_transaction_value
FROM supermarket_sales
GROUP BY customer_type
ORDER BY total_revenue DESC;

-- ======================================
-- 7. Payment Method Performance
-- ======================================

SELECT
    payment,
    COUNT(*) AS total_transactions,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(total), 2) AS total_revenue,
    ROUND(SUM(gross_income), 2) AS total_gross_income,
    ROUND(AVG(total), 2) AS average_transaction_value
FROM supermarket_sales
GROUP BY payment
ORDER BY total_revenue DESC;

-- ======================================
-- 8. Product Line Profitability
-- ======================================

SELECT
    product_line,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(total), 2) AS total_revenue,
    ROUND(SUM(gross_income), 2) AS total_gross_income,
    ROUND(
        SUM(gross_income) * 100.0 / SUM(total),
        2
    ) AS gross_income_margin
FROM supermarket_sales
GROUP BY product_line
ORDER BY total_gross_income DESC;