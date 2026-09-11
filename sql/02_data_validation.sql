-- ======================================
-- Supermarket Sales Analysis
-- PostgreSQL Data Validation
-- ======================================


-- ======================================
-- 1. Row count
-- ======================================

SELECT COUNT(*) AS total_rows
FROM supermarket_sales;

-- ======================================
-- 2. Check primary key uniqueness
-- ======================================

SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT invoice_id) AS unique_invoice_ids
FROM supermarket_sales;

-- ======================================
-- 3. Check for NULL values
-- ======================================

SELECT
    COUNT(*) FILTER (WHERE invoice_id IS NULL) AS invoice_id_nulls,
    COUNT(*) FILTER (WHERE branch IS NULL) AS branch_nulls,
    COUNT(*) FILTER (WHERE city IS NULL) AS city_nulls,
    COUNT(*) FILTER (WHERE customer_type IS NULL) AS customer_type_nulls,
    COUNT(*) FILTER (WHERE gender IS NULL) AS gender_nulls,
    COUNT(*) FILTER (WHERE product_line IS NULL) AS product_line_nulls,
    COUNT(*) FILTER (WHERE unit_price IS NULL) AS unit_price_nulls,
    COUNT(*) FILTER (WHERE quantity IS NULL) AS quantity_nulls,
    COUNT(*) FILTER (WHERE tax IS NULL) AS tax_nulls,
    COUNT(*) FILTER (WHERE total IS NULL) AS total_nulls,
    COUNT(*) FILTER (WHERE date IS NULL) AS date_nulls,
    COUNT(*) FILTER (WHERE time IS NULL) AS time_nulls,
    COUNT(*) FILTER (WHERE payment IS NULL) AS payment_nulls,
    COUNT(*) FILTER (WHERE cogs IS NULL) AS cogs_nulls,
    COUNT(*) FILTER (WHERE gross_margin_percentage IS NULL) AS margin_nulls,
    COUNT(*) FILTER (WHERE gross_income IS NULL) AS income_nulls,
    COUNT(*) FILTER (WHERE rating IS NULL) AS rating_nulls
FROM supermarket_sales;

-- ======================================
-- 4. Business-rule validation
-- ======================================

SELECT
    COUNT(*) FILTER (WHERE quantity <= 0) AS invalid_quantity,
    COUNT(*) FILTER (WHERE unit_price <= 0) AS invalid_unit_price,
    COUNT(*) FILTER (WHERE total <= 0) AS invalid_total,
    COUNT(*) FILTER (
        WHERE rating < 0 OR rating > 10
    ) AS invalid_rating
FROM supermarket_sales;