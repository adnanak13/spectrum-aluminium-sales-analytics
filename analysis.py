"""
Spectrum Aluminium Sales Analytics
Financial year: April 2025–March 2026
NOTE: This is a synthetic practice dataset, not actual company records.
Run from this folder: python analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "spectrum_aluminium_sales_apr2025_mar2026.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Invoice_Date"])

# Basic validation
required = [
    "Invoice_ID", "Invoice_Date", "Customer_Name", "Customer_Segment", "City",
    "Product_Name", "Product_Category", "Quantity", "Discount_Percent",
    "Sales_Revenue_SAR", "Total_Cost_SAR", "Gross_Profit_SAR",
    "Payment_Status", "Sales_Representative", "Sales_Channel"
]
missing_columns = sorted(set(required) - set(df.columns))
if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

print("DATA OVERVIEW")
print(f"Rows: {len(df):,}; columns: {len(df.columns)}")
print(f"Date range: {df['Invoice_Date'].min().date()} to {df['Invoice_Date'].max().date()}")
print(f"Missing cells: {int(df.isna().sum().sum())}")
print(f"Duplicate invoice IDs: {int(df['Invoice_ID'].duplicated().sum())}")

# Derive month and weighted margin (do not average row margins for total margin)
df["Month"] = df["Invoice_Date"].dt.to_period("M").astype(str)
df["Gross_Margin_Calculated_Percent"] = (
    df["Gross_Profit_SAR"] / df["Sales_Revenue_SAR"] * 100
)

def save_summary(series_or_df, filename):
    series_or_df.to_csv(OUT / filename, encoding="utf-8-sig")
    print(f"\n{filename}\n", series_or_df.head(10).to_string())

monthly = df.groupby("Month", as_index=False).agg(
    Sales_Revenue_SAR=("Sales_Revenue_SAR", "sum"),
    Gross_Profit_SAR=("Gross_Profit_SAR", "sum"),
    Invoice_Count=("Invoice_ID", "nunique")
).sort_values("Month")
monthly["Gross_Margin_Percent"] = monthly["Gross_Profit_SAR"] / monthly["Sales_Revenue_SAR"] * 100
save_summary(monthly, "monthly_sales.csv")

product = df.groupby("Product_Name", as_index=False).agg(
    Sales_Revenue_SAR=("Sales_Revenue_SAR", "sum"),
    Gross_Profit_SAR=("Gross_Profit_SAR", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Sales_Revenue_SAR", ascending=False)
product["Gross_Margin_Percent"] = product["Gross_Profit_SAR"] / product["Sales_Revenue_SAR"] * 100
save_summary(product, "product_performance.csv")

city = df.groupby("City", as_index=False).agg(
    Sales_Revenue_SAR=("Sales_Revenue_SAR", "sum"),
    Gross_Profit_SAR=("Gross_Profit_SAR", "sum")
).sort_values("Sales_Revenue_SAR", ascending=False)
save_summary(city, "city_performance.csv")

category = df.groupby("Product_Category", as_index=False).agg(
    Sales_Revenue_SAR=("Sales_Revenue_SAR", "sum"),
    Gross_Profit_SAR=("Gross_Profit_SAR", "sum")
)
category["Gross_Margin_Percent"] = category["Gross_Profit_SAR"] / category["Sales_Revenue_SAR"] * 100
category = category.sort_values("Gross_Margin_Percent", ascending=False)
save_summary(category, "category_margin.csv")

customer = df.groupby(["Customer_ID", "Customer_Name"], as_index=False).agg(
    Sales_Revenue_SAR=("Sales_Revenue_SAR", "sum"),
    Gross_Profit_SAR=("Gross_Profit_SAR", "sum"),
    Invoice_Count=("Invoice_ID", "nunique")
).sort_values("Sales_Revenue_SAR", ascending=False)
save_summary(customer, "customer_rankings.csv")

segment = df.groupby("Customer_Segment", as_index=False).agg(
    Sales_Revenue_SAR=("Sales_Revenue_SAR", "sum"),
    Gross_Profit_SAR=("Gross_Profit_SAR", "sum")
).sort_values("Gross_Profit_SAR", ascending=False)
save_summary(segment, "segment_profit.csv")

overdue = df[df["Payment_Status"].str.strip().str.lower() == "overdue"]
print(f"\nRevenue linked to overdue invoices (SAR): {overdue['Sales_Revenue_SAR'].sum():,.2f}")
print(f"Number of overdue invoices: {overdue['Invoice_ID'].nunique():,}")

rep = df.groupby("Sales_Representative", as_index=False).agg(
    Sales_Revenue_SAR=("Sales_Revenue_SAR", "sum"),
    Gross_Profit_SAR=("Gross_Profit_SAR", "sum"),
    Invoice_Count=("Invoice_ID", "nunique")
).sort_values("Sales_Revenue_SAR", ascending=False)
save_summary(rep, "sales_rep_performance.csv")

channel = df.groupby("Sales_Channel", as_index=False).agg(
    Sales_Revenue_SAR=("Sales_Revenue_SAR", "sum"),
    Gross_Profit_SAR=("Gross_Profit_SAR", "sum"),
    Invoice_Count=("Invoice_ID", "nunique")
).sort_values("Sales_Revenue_SAR", ascending=False)
save_summary(channel, "channel_performance.csv")

discount = df.groupby("Discount_Percent", as_index=False).agg(
    Transactions=("Invoice_ID", "nunique"),
    Sales_Revenue_SAR=("Sales_Revenue_SAR", "sum"),
    Gross_Profit_SAR=("Gross_Profit_SAR", "sum")
)
discount["Gross_Margin_Percent"] = discount["Gross_Profit_SAR"] / discount["Sales_Revenue_SAR"] * 100
save_summary(discount, "discount_analysis.csv")

# Chart 1: monthly revenue
plt.figure(figsize=(11, 5))
plt.bar(monthly["Month"], monthly["Sales_Revenue_SAR"])
plt.title("Monthly Sales Revenue (SAR)")
plt.xlabel("Month")
plt.ylabel("Sales Revenue (SAR)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUT / "monthly_sales_revenue.png", dpi=160)
plt.close()

# Chart 2: product revenue
top_products = product.sort_values("Sales_Revenue_SAR", ascending=True)
plt.figure(figsize=(10, 6))
plt.barh(top_products["Product_Name"], top_products["Sales_Revenue_SAR"])
plt.title("Sales Revenue by Aluminium Product")
plt.xlabel("Sales Revenue (SAR)")
plt.tight_layout()
plt.savefig(OUT / "product_revenue.png", dpi=160)
plt.close()

# Chart 3: discount vs weighted gross margin
plt.figure(figsize=(8, 5))
plt.plot(discount["Discount_Percent"], discount["Gross_Margin_Percent"], marker="o")
plt.title("Discount Level vs Gross Margin")
plt.xlabel("Discount (%)")
plt.ylabel("Gross Margin (%)")
plt.tight_layout()
plt.savefig(OUT / "discount_vs_margin.png", dpi=160)
plt.close()

print(f"\nDone. CSV summaries and charts are saved in: {OUT}")
