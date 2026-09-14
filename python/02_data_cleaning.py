import pandas as pd
from pathlib import Path

# =======================================
# 1. Load raw data
# =======================================
PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "supermarket_sales.csv"
)

CLEANED_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "cleaned"
    / "supermarket_sales_cleaned.csv"
)

df = pd.read_csv(RAW_DATA_PATH)

print("Original shape:", df.shape)

# =======================================
# 2. Standardize column names
# =======================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("%", "pct")
)

df = df.rename(columns={"tax_5pct": "tax"})

print(df.columns)

# =======================================
# 3. Convert date and time
# =======================================

df["date"] = pd.to_datetime(df["date"])

df["time"] = pd.to_datetime(df["time"], format="%H:%M").dt.time

# =======================================
# 4. Validate numeric columns
# =======================================

numeric_columns = [
    "unit_price",
    "quantity",
    "tax",
    "total",
    "cogs",
    "gross_margin_percentage",
    "gross_income",
    "rating"
]

print("\nNumeric data types:")
print(df[numeric_columns].dtypes)

# =======================================
# 5. Validate categorical columns
# =======================================

categorical_columns = [
    "branch",
    "city",
    "customer_type",
    "gender",
    "product_line",
    "payment"
]

print("\nCategorical values:")

for column in categorical_columns:
    print(f"\n{column}")
    print(df[column].unique())

# =======================================
# 6. Business-rule validation
# =======================================


invalid_quantity = (df["quantity"] <= 0).sum()

print("\nInvalid quantity:", invalid_quantity)

invalid_unit_price = (df["unit_price"] <= 0).sum()

print("Invalid unit price:", invalid_unit_price)

invalid_total = (df["total"] <= 0).sum()

print("Invalid total:", invalid_total)

invalid_rating = (
    (df["rating"] < 0) |
    (df["rating"] > 10)).sum()

print("Invalid rating:", invalid_rating)

# =======================================
# 7. Missing values and duplicates
# =======================================

missing_values = df.isna().sum().sum()
duplicate_rows = df.duplicated().sum()

print("\nMissing values:", missing_values)
print("Duplicate rows:", duplicate_rows)

# =======================================
# 8. Validate calculated fields
# =======================================

expected_cogs = df["unit_price"] * df["quantity"]

cogs_mismatches = (
    (df["cogs"] - expected_cogs).abs() > 0.000001
).sum()

print("\nCalculated field validation:")
print("COGS mismatches:", cogs_mismatches)

expected_total = df["cogs"] + df["tax"]

total_mismatches = (
    (df["total"] - expected_total).abs() > 0.000001
).sum()

print("Total mismatches:", total_mismatches)

# =======================================
# 9. Save cleaned data
# =======================================

validation_passed = (
    invalid_quantity == 0
    and invalid_unit_price == 0
    and invalid_total == 0
    and invalid_rating == 0
    and missing_values == 0
    and duplicate_rows == 0
    and cogs_mismatches == 0
    and total_mismatches == 0
)

if validation_passed:
    output_path = CLEANED_DATA_PATH

    df.to_csv(output_path, index=False)

    print("\nValidation passed.")
    print("\nCleaned data saved to:")
    print(output_path)
    print("Final shape:", df.shape)

else:
    print("\nValidation failed.")
    print("Cleaned data was NOT saved.")