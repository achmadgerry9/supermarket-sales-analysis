import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# =======================================
# Supermarket Sales Analysis
# Python Analysis
# =======================================

# Load cleaned data
PROJECT_ROOT = Path(__file__).resolve().parents[1]

CLEANED_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "cleaned"
    / "supermarket_sales_cleaned.csv"
)

OUTPUTS_DIR = PROJECT_ROOT / "outputs"

df = pd.read_csv(CLEANED_DATA_PATH)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Basic check
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nDate range:")
print(df["date"].min())
print(df["date"].max())

print("\nRevenue:", round(df["total"].sum(), 2))
print("Gross income:", round(df["gross_income"].sum(), 2))

# =======================================
# Customer Type Performance
# =======================================

customer_performance = (
    df.groupby("customer_type")
    .agg(
        total_transaction=("invoice_id", "count"),
        total_units_sold=("quantity", "sum"),
        total_revenue=("total", "sum"),
        total_gross_income=("gross_income", "sum"),
        average_transaction_value=("total", "mean")
    )
    .reset_index()
)

customer_performance["total_revenue"] = (
    customer_performance["total_revenue"].round(2)
)

customer_performance["total_gross_income"] = customer_performance["total_gross_income"].round(2)

customer_performance["average_transaction_value"] = (
    customer_performance["average_transaction_value"].round(2)
)

print("\nCustomer type performance:")
print(customer_performance)

customer_performance.to_csv(
    OUTPUTS_DIR / "customer_type_performance.csv",
    index=False
)

# =======================================
# Monthly Revenue
# =======================================

monthly_revenue = (
    df.groupby(df["date"].dt.to_period("M"))
    .agg(
        total_transactions=("invoice_id", "count"),
        total_units_sold=("quantity", "sum"),
        total_revenue=("total", "sum"),
        total_gross_income=("gross_income", "sum")
    ).reset_index()
)

monthly_revenue["date"] = monthly_revenue["date"].astype(str)

monthly_revenue["total_revenue"] = (
    monthly_revenue["total_revenue"].round(2)
)

monthly_revenue["total_gross_income"] = (
    monthly_revenue["total_gross_income"].round(2)
)

monthly_revenue["average_transaction_value"] = (
    monthly_revenue["total_revenue"] / monthly_revenue["total_transactions"]
).round(2)

print("\nMonthly revenue:")
print(monthly_revenue)

monthly_revenue.to_csv(
    OUTPUTS_DIR / "monthly_revenue.csv",
    index=False
)

# Create chart
plt.figure(figsize=(8, 5))

plt.plot(
    monthly_revenue["date"],
    monthly_revenue["total_revenue"],
    marker="o"
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()

# =======================================
# Branch Performance
# =======================================

branch_performance = (
    df.groupby("branch")
    .agg(
        total_transactions=("invoice_id", "count"),
        total_revenue=("total", "sum"),
        average_transaction_value=("total", "mean")
    )
    .reset_index()
    .sort_values("total_revenue", ascending=False)
)

branch_performance["total_revenue"] = branch_performance["total_revenue"].round(2)
branch_performance["average_transaction_value"] = (
    branch_performance["average_transaction_value"].round(2)
)

print("\nBranch performance:")
print(branch_performance)

branch_performance.to_csv(
    OUTPUTS_DIR / "branch_performance.csv",
    index=False
)

# Revenue chart
plt.figure(figsize=(8, 5))

plt.bar(
    branch_performance["branch"],
    branch_performance["total_revenue"]
)

plt.title("Revenue by Branch")
plt.xlabel("Branch")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()

# Revenue difference between top and bottom branch
top_branch = branch_performance.iloc[0]
bottom_branch = branch_performance.iloc[-1]

revenue_difference = (
    top_branch["total_revenue"] - bottom_branch["total_revenue"]
)

print(
    f"\nRevenue difference between "
    f"{top_branch['branch']} and {bottom_branch['branch']}: "
    f"{revenue_difference:.2f}"
)

# =======================================
# Product Line Performance
# =======================================

product_performance = (
    df.groupby("product_line")
    .agg(
        total_transactions=("invoice_id", "count"),
        total_units_sold=("quantity", "sum"),
        total_revenue=("total", "sum"),
        total_gross_income=("gross_income", "sum")
    )
    .reset_index()
    .sort_values("total_revenue", ascending=True)
)

product_performance["total_revenue"] = (
    product_performance["total_revenue"].round(2)
)

print("\nProduct line performance:")
print(product_performance)

product_performance.to_csv(
    OUTPUTS_DIR / "product_line_performance.csv",
    index=False
)

# Revenue chart
plt.figure(figsize=(9,5))

plt.barh(
    product_performance["product_line"],
    product_performance["total_revenue"]
)

plt.title("Revenue by Product Line")
plt.xlabel("Revenue")
plt.ylabel("Product Line")

plt.tight_layout()
plt.show()

# =======================================
# Payment Method Performance
# =======================================

payment_performance = (
    df.groupby("payment")
    .agg(
        total_transactions=("invoice_id", "count"),
        total_units_sold=("quantity", "sum"),
        total_revenue=("total", "sum"),
        total_gross_income=("gross_income", "sum"),
        average_transaction_value=("total", "mean")
    )
    .reset_index()
    .sort_values("total_revenue", ascending=False)
)

payment_performance["total_revenue"] = (
    payment_performance["total_revenue"].round(2)
)

payment_performance["total_gross_income"] = (
    payment_performance["total_gross_income"].round(2)
)

payment_performance["average_transaction_value"] = (
    payment_performance["average_transaction_value"].round(2)
)

print("\nPayment performance:")
print(payment_performance)

payment_performance.to_csv(
    OUTPUTS_DIR / "payment_performance.csv",
    index=False
)

# =======================================
# Transaction Volume vs Revenue
# =======================================

plt.figure(figsize=(8, 5))

plt.scatter(
    product_performance["total_transactions"],
    product_performance["total_revenue"]
)

plt.title("Transaction Volume vs Revenue by Product Line")
plt.xlabel("Number of Transactions")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()

# =======================================
# Average Transaction Value by Product Line
# =======================================

product_atv = (
    df.groupby("product_line")["total"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

print("\nAverage transaction value by product line:")
print(product_atv)