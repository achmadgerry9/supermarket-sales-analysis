-- ======================================
-- Supermarket Sales Analysis
-- PostgreSQL Schema
-- ======================================

CREATE TABLE supermarket_sales (
    invoice_id VARCHAR(20) PRIMARY KEY,

    branch CHAR(1) NOT NULL,
    city VARCHAR(50) NOT NULL,

    customer_type VARCHAR(20) NOT NULL,
    gender VARCHAR(10) NOT NULL,

    product_line VARCHAR(50) NOT NULL,

    unit_price NUMERIC(10,2) NOT NULL,
    quantity INTEGER NOT NULL,

    tax NUMERIC(10,4) NOT NULL,
    total NUMERIC(10,4) NOT NULL,

    date DATE NOT NULL,
    time TIME NOT NULL,

    payment VARCHAR(20) NOT NULL,

    cogs NUMERIC(10,2) NOT NULL,
    gross_margin_percentage NUMERIC(10,7) NOT NULL,
    gross_income NUMERIC(10,4) NOT NULL,

    rating NUMERIC(3,1) NOT NULL
);