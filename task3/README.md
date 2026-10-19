# SWYNEX Task 3: Interactive Retail Sales Dashboard

## 1. Project Overview

This project focuses on building an interactive retail sales dashboard using Tableau Public. The dashboard uses the cleaned retail dataset prepared in Task 1 and analyzed in Task 2.

The main objective is to visualize important business metrics, identify sales trends, compare country-level performance, and communicate useful business insights through interactive charts.

## 2. Objectives

- Build a professional interactive dashboard.
- Display important Key Performance Indicators (KPIs).
- Analyze monthly sales trends.
- Identify top-performing countries and products.
- Explore the relationship between quantity and unit price.
- Add interactive filters for data exploration.
- Identify possible transaction anomalies.

## 3. Tools and Technologies

- Tableau Public
- Microsoft Excel
- CSV Dataset
- GitHub

## 4. Dataset Information

Dataset: cleaned_retail_2000.csv

The dataset contains retail transaction records with the following fields:

| Column | Description |
|---|---|
| Invoice No | Invoice identification number |
| Stock Code | Product identification code |
| Description | Product description |
| Quantity | Number of units purchased or returned |
| Invoice Date | Transaction date |
| Unit Price | Price per unit |
| Customer ID | Customer identification number |
| Country | Country associated with the transaction |

## 5. Dashboard KPIs

The dashboard includes the following KPI cards:

1. Total Sales
2. Unique Invoices
3. Unique Customers
4. Unique Products
5. Total Quantity

### Total Sales Calculation

Total Sales = Quantity × Unit Price

In Tableau, the calculated field is:

    [Quantity] * [Unit Price]

Use SUM(Total Sales) to calculate the overall sales value.

## 6. Visualizations

The dashboard includes the following charts:

### 1. Monthly Sales Trend
A line chart showing how sales change over time.

### 2. Top Countries by Sales
A bar chart comparing sales across countries.

### 3. Top Products by Sales
A bar chart identifying products with the highest sales value.

### 4. Quantity vs Unit Price
A scatter plot exploring the relationship between transaction quantity and unit price.

## 7. Interactive Filters

The dashboard provides the following filters:

- Country
- Invoice Date
- Product Description

These filters allow users to explore selected countries, dates, and products.

## 8. Key Business Insights

The following insights should be completed using the actual Tableau results:

1. Country Performance:
   Identify the country with the highest total sales.

2. Product Performance:
   Identify the product generating the highest total sales value.

3. Monthly Sales Trend:
   Identify the month and year with the highest total sales.

4. Geographic Distribution:
   Compare sales performance across countries.

5. Transaction Analysis:
   Investigate negative quantities that may indicate returns or cancellations.

Note: All findings should be verified using the actual dataset and dashboard.

## 9. Dashboard Design

The dashboard combines KPI cards, charts, filters, and a business insights text box in a single interface.

The design aims to make important information easy to understand and explore.

## 10. Project Structure

    task3/
    |
    |-- README.md
    |-- cleaned_retail_2000.csv
    |-- SWYNEX_Task3_Interactive_Dashboard.twbx

## 11. Conclusion

This project demonstrates how Tableau Public can be used to transform cleaned retail transaction data into an interactive business intelligence dashboard.

The dashboard helps users understand sales performance, explore trends, compare countries and products, and investigate possible transaction anomalies.

## 12. Project Information

Program: SWYNEX Internship

Task: Task 3 - Interactive Dashboard

Tool: Tableau Public