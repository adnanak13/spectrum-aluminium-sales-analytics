# Spectrum Aluminium Sales Analytics

An end-to-end sales analytics portfolio project using **Python, MySQL, and Power BI** to explore a synthetic aluminium sales dataset for the financial year **April 2025–March 2026**.

> **Dataset notice:** The data in this repository is synthetic and created for learning and portfolio demonstration. It is not actual company or customer records.

## Project Overview

This project analyses sales transactions to understand revenue, gross profit, product performance, regional performance, customer segments, sales representatives, sales channels, discounts, and overdue invoices.

### Tools Used

- **Python** — data validation, aggregation, summary exports, and chart generation
- **Pandas** — data manipulation and analysis
- **Matplotlib** — visualisations
- **MySQL 8+** — relational table design and SQL-based analysis
- **Power BI Desktop** — interactive dashboard exploration

## Repository Structure

Organise the files in GitHub using the following structure. Rename the uploaded files to the clean filenames shown below, if necessary.

```text
spectrum-aluminium-sales-analytics/
├── data/
│   └── spectrum_aluminium_sales_apr2025_mar2026.csv
├── outputs/
│   └── (generated CSV summaries and PNG charts)
├── analysis.py
├── analysis_queries.sql
├── requirements.txt
├── .gitignore
├── Spectrum Sales.pbix
└── README.md
```

The Python script expects the CSV at `data/spectrum_aluminium_sales_apr2025_mar2026.csv`. Make sure the folder and filename match this path before running the script.

## Dataset

- **Rows:** 600 sales transactions
- **Columns:** 21
- **Period:** April 2025 to March 2026
- **Currency:** Saudi Riyal (SAR)

Important fields include:

| Field | Description |
|---|---|
| `Invoice_ID` | Unique invoice identifier |
| `Invoice_Date` | Date of the transaction |
| `Customer_Name` / `Customer_Segment` | Customer and segment information |
| `City` | Sales city |
| `Product_Name` / `Product_Category` | Product and category details |
| `Quantity` / `Unit` | Quantity sold and unit of measure |
| `Unit_Price_SAR` | Unit selling price |
| `Discount_Percent` | Discount applied |
| `Sales_Revenue_SAR` | Sales revenue in SAR |
| `Total_Cost_SAR` | Total cost in SAR |
| `Gross_Profit_SAR` | Gross profit in SAR |
| `Gross_Margin_Percent` | Gross margin percentage recorded in the dataset |
| `Payment_Method` / `Payment_Status` | Payment details |
| `Sales_Representative` | Representative associated with the sale |
| `Sales_Channel` | Sales channel |

## Questions Explored

The project is designed to help investigate:

1. How does sales revenue and gross profit change month by month?
2. Which products and product categories generate the most revenue and profit?
3. Which cities contribute the most revenue?
4. Which customers and customer segments perform best?
5. How do sales representatives and sales channels compare?
6. How does discount level relate to gross margin?
7. How many invoices are overdue, and how much revenue is associated with them?

## Python Analysis

The Python script validates that key columns are present, reports the dataset size and date range, checks missing cells and duplicate invoice IDs, creates monthly and performance summaries, and saves charts.

### Setup

Install Python 3.10 or later, then open a terminal in the repository folder.

1. (Recommended) Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Confirm the dataset is saved at:

   ```text
   data/spectrum_aluminium_sales_apr2025_mar2026.csv
   ```

4. Run the analysis:

   ```bash
   python analysis.py
   ```

### Generated Outputs

When the script runs successfully, it creates an `outputs/` folder containing summary CSV files:

- `monthly_sales.csv`
- `product_performance.csv`
- `city_performance.csv`
- `category_margin.csv`
- `customer_rankings.csv`
- `segment_profit.csv`
- `sales_rep_performance.csv`
- `channel_performance.csv`
- `discount_analysis.csv`

It also generates these PNG charts:

- `monthly_sales_revenue.png`
- `product_revenue.png`
- `discount_vs_margin.png`

The script prints a data overview and a summary of revenue associated with overdue invoices in the terminal.

## MySQL Analysis

The SQL script is intended for **MySQL 8+**. It creates the `spectrum_sales` database and the `sales_data` table schema. The supplied SQL file also contains insert statements for the synthetic transaction data.

### How to Run

1. Install and open MySQL Server and a SQL client such as MySQL Workbench.
2. Open `analysis_queries.sql`.
3. Review the script and confirm that you are using a practice database.
4. Execute the script in MySQL Workbench or another MySQL client.
5. Check that the `spectrum_sales` database and `sales_data` table were created and populated.

If you prefer to import the CSV separately, import it into a table named `sales_data` with column types matching the SQL schema. Avoid loading the same records twice unless you understand how the script's primary key and duplicate-key handling work.

> **Note:** The SQL file contains data insertion statements. Review it before running, especially if you have changed the table schema or already imported the CSV.

## Power BI Dashboard

The repository includes a Power BI report file (`Spectrum Sales.pbix`).

To explore it:

1. Install **Power BI Desktop**.
2. Open `Spectrum Sales.pbix`.
3. Review the report pages, visuals, filters, and data model.
4. If Power BI requests a data source, update the source path to the CSV location in your repository.
5. Refresh the data and verify the KPI values and visuals before publishing or sharing the report.

The Power BI file is included as a project deliverable; check its data-source settings and refresh status on your own computer before relying on the displayed results.

Suggested dashboard components include KPI cards for revenue, gross profit, gross margin, and invoice count; monthly revenue trends; product and city comparisons; sales representative and channel performance; payment-status analysis; and slicers for date, city, product, customer segment, and sales channel.

## Key Metric Definitions

- **Total Sales Revenue:** Sum of `Sales_Revenue_SAR`
- **Total Gross Profit:** Sum of `Gross_Profit_SAR`
- **Weighted Gross Margin:** Total gross profit divided by total sales revenue, multiplied by 100
- **Invoice Count:** Distinct count of `Invoice_ID`
- **Overdue Revenue:** Sum of `Sales_Revenue_SAR` for records where `Payment_Status` is `Overdue`

For an overall gross margin, use the weighted calculation above rather than taking a simple average of row-level margin percentages.

## Data Quality and Limitations

- This is a synthetic practice dataset; findings are illustrative and should not be treated as verified business performance.
- The Python script checks for required columns, missing cells, and duplicate invoice IDs.
- Confirm that the revenue, cost, profit, and margin fields are internally consistent before using the results for decisions.
- Results depend on the data and on the current data-source settings in the Power BI file.

## Future Improvements

- Add automated data-quality tests and validation rules.
- Create additional SQL views and KPI queries.
- Add year-over-year comparisons when multiple years of data are available.
- Improve the Power BI model with a dedicated date table and documented DAX measures.
- Automate analysis and report refreshes.

## Skills Demonstrated

`Python` · `Pandas` · `Data Cleaning` · `Exploratory Data Analysis` · `Matplotlib` · `MySQL` · `SQL Aggregations` · `Power BI` · `Business Intelligence` · `Data Visualisation`

---

**Author:** Adnan Ahmad Khan

**Project:** Spectrum Aluminium Sales Analytics  
**Purpose:** Data analytics learning and portfolio demonstration
