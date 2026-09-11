import pandas as pd

# =======================================
# 1. Load the raw dataset
# =======================================

file_path = "D:/Portfolio 2026/supermarket-sales-analysis/data/raw/supermarket_sales.csv"

df = pd.read_csv(file_path)

# =======================================
# 2. Basic dataset information
# =======================================

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nColumn names:")
print(df.columns.tolist())

# =======================================
# 3. Data types
# =======================================

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes)

# =======================================
# 4. Missing values
# =======================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing_values = df.isna().sum()

print(missing_values)

print(f"\nTotal missing values: {missing_values.sum()}")

# =======================================
# 5. Duplicate rows
# =======================================

print("\n" + "=" * 60)
print("DUPLICATES")
print("=" * 60)

duplicate_count = df.duplicated().sum()

print(f"Duplicated rows: {duplicate_count}")

# =======================================
# 6. Unique values in categorical columns
# =======================================

categorical_columns = [
    "Branch",
    "City",
    "Customer type",
    "Gender",
    "Product line",
    "Payment"
]

print("\n" + "=" * 60)
print("CATEGORICAL VARIABLES")
print("=" * 60)

for column in categorical_columns:
    print(f"\n{column}")
    print("-" * len(column))
    print(f"Unique values: {df[column].nunique()}")
    print(df[column].unique())

# =======================================
# 7. Descriptive statistics
# =======================================

print("\n" + "=" * 60)
print("NUMERICAL SUMMARY")
print("=" * 60)

print(df.describe())

# =======================================
# 8. Date range
# =======================================

print("\n" + "=" * 60)
print("DATE RANGE")
print("=" * 60)

dates = pd.to_datetime(df["Date"])

print(f"Earliest date: {dates.min().date()}")
print(f"Latest date: {dates.max().date()}")

# =======================================
# 9. Unique invoice IDs
# =======================================

print("\n" + "=" * 60)
print("INVOICE INFORMATION")
print("=" * 60)

print(f"Total rows: {len(df)}")
print(f"Unique Invoice IDs: {df['Invoice ID'].nunique()}")

# =======================================
# 10. Basic business observations
# =======================================

print("\n" + "=" * 60)
print("INITIAL OBSERVATIONS")
print("=" * 60)

print(f"Total revenue: {df['Total'].sum():,.2f}")
print(f"Total gross income: {df['gross income'].sum():,.2f}")
print(f"Total units sold: {df['Quantity'].sum():,}")
print(f"Average transaction value: {df['Total'].mean():,.2f}")
print(f"Average gross income per transaction: {df['gross income'].mean():,.2f}")