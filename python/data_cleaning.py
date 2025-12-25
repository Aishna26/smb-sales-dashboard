import pandas as pd

# 1. Load raw sales data
sales = pd.read_csv("data/raw/sales.csv")

# 2. Fix missing quantity (assume 1 item sold if missing)
sales["quantity"] = sales["quantity"].fillna(1)

# 3. Standardize region names
sales["region"] = sales["region"].replace({
    "NY": "New York",
    "CA": "California"
})

# 4. Convert date column to proper date format
sales["date"] = pd.to_datetime(sales["date"])

# 5. Create total revenue column
sales["total_revenue"] = sales["quantity"] * sales["price"]

# 6. Save cleaned data
sales.to_csv("data/processed/clean_sales.csv", index=False)

print("Data cleaning completed successfully.")
