import sqlite3
import pandas as pd

# 1. Load cleaned sales data
sales = pd.read_csv("data/processed/clean_sales.csv")

# 2. Create SQLite database
conn = sqlite3.connect("data/sales.db")

# 3. Load data into SQL table
sales.to_sql("sales", conn, if_exists="replace", index=False)

# 4. Run SQL queries
query_monthly = """
SELECT
    strftime('%Y-%m', date) AS month,
    SUM(total_revenue) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;
"""

query_region = """
SELECT
    region,
    SUM(total_revenue) AS revenue
FROM sales
GROUP BY region
ORDER BY revenue DESC;
"""

monthly_revenue = pd.read_sql(query_monthly, conn)
region_revenue = pd.read_sql(query_region, conn)

# 5. Save results for Excel
with pd.ExcelWriter("excel/dashboard_data.xlsx") as writer:
    monthly_revenue.to_excel(writer, sheet_name="Monthly Revenue", index=False)
    region_revenue.to_excel(writer, sheet_name="Revenue by Region", index=False)

conn.close()

print("SQL analysis completed successfully.")
