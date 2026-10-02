# SWYNEX Task 2 - Exploratory Data Analysis

## Objective

Use the cleaned dataset from SWYNEX Task 1 to calculate statistics, identify trends/patterns/anomalies, create charts, and document at least five useful insights.

## Dataset

- Cleaned records analyzed: **1,978**
- Unique invoices: **721**
- Unique products: **41**
- Unique customers: **1,643**
- Countries represented: **16**

## Analysis performed

1. Descriptive statistics for Quantity, UnitPrice and Sales.
2. Sales by country.
3. Top products by sales.
4. Monthly sales trend.
5. Sales by day of week.
6. Unit-price distribution.
7. Quantity vs UnitPrice relationship.
8. Negative-quantity transaction lines as a return/cancellation indicator.
9. IQR-based quantity outlier screening.

## Five+ useful insights

- The dataset contains 1,978 cleaned transaction lines covering 721 unique invoices, 41 unique products, 1,643 customers and 16 countries.
- United Kingdom has the highest total sales in this sample at 364,295.96, representing 70.4% of total sales.
- The highest-sales month in the cleaned sample is 2011-05, with total sales of 50,078.08.
- The product with the highest total sales in this sample is REGENCY CAKESTAND 3 TIER (StockCode 22423), with sales of 53,937.90.
- Tuesday has the highest total sales among weekdays represented in the sample, at 95,014.69.
- There are 62 transaction lines with negative quantity. These are retained as a separate anomaly/return indicator rather than automatically deleted.
- The quantity IQR rule identifies 175 rows outside the 1.5×IQR bounds. These are potential high-volume/low-volume anomalies and should be investigated rather than automatically removed.

**Important:** Negative quantities are treated as a business/anomaly signal rather than automatically deleted because they can represent returns or cancellations in retail transaction data. The IQR result is a screening rule; flagged rows should be investigated before removal.

## Charts

- `charts/top_countries_sales.png`
- `charts/top_products_sales.png`
- `charts/monthly_sales_trend.png`
- `charts/unit_price_distribution.png`
- `charts/quantity_vs_unit_price.png`

## Excel workbook

`SWYNEX_Task2_EDA_Analysis.xlsx` contains:

- KPI_Summary
- Numeric_Statistics
- Country_Analysis
- Top_Products
- Monthly_Trend
- Day_Analysis
- Insights

## Run the Python analysis

Install dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python scripts/eda_analysis.py
```

## LinkedIn video structure

1. Introduce SWYNEX Task 2.
2. Show the cleaned Task 1 dataset.
3. Show KPI/statistical analysis.
4. Show country and product charts.
5. Show monthly trend.
6. Explain at least five findings.
7. Mention the anomaly/return analysis.
8. Show the GitHub repository.

Suggested closing:

> "This EDA helped me understand the distribution, trends, product performance, country contribution and potential anomalies in the cleaned retail dataset."

## Submission

Submit:
1. GitHub repository URL containing this project.
2. LinkedIn post URL containing the Task 2 video explanation.
