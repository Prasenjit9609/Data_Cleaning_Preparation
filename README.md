# SWYNEX — Data Cleaning & Preparation

## Task 1 — Data Cleaning & Preparation

This repository contains a **2,000-record retail transaction dataset** prepared for the **SWYNEX internship Task 1**.

The project demonstrates a complete data-cleaning and preparation workflow using **Python, Pandas, Excel, and CSV files**.

---

## 📊 Dataset Basis

The dataset structure follows the **UCI Online Retail** dataset.

The UCI Online Retail dataset represents transactions from a UK-based non-store online retailer and contains fields such as:

* `InvoiceNo`
* `StockCode`
* `Description`
* `Quantity`
* `InvoiceDate`
* `UnitPrice`
* `CustomerID`
* `Country`

The original UCI dataset contains **541,909 instances** and is licensed under **CC BY 4.0**.

### Official Source

* **UCI Dataset:** https://uci-ics-mlr-prod.aws.uci.edu/dataset/352/online%2Bretail
* **DOI:** https://doi.org/10.24432/C5BW33

### Important Note

The **2,000 records in this repository are an educational derived dataset** generated using the public dataset's schema and realistic retail values.

Artificial data-quality problems were deliberately inserted to demonstrate the data-cleaning process without redistributing the complete UCI dataset.

---

# 📁 Repository Structure

```text
SWYNEX-Data-Cleaning-Preparation/
│
├── data/
│   ├── raw_retail_2000.csv
│   └── cleaned_retail_2000.csv
│
├── excel/
│   └── SWYNEX_Data_Cleaning_2000.xlsx
│
├── scripts/
│   └── clean_retail_data.py
│
├── data_quality_report.csv
├── cleaning_summary.csv
├── cleaning_log.csv
├── requirements.txt
└── README.md
```

---

# ⚠️ Problems Deliberately Included in Raw Data

The raw **2,000-record dataset** contains several common real-world data-quality problems.

### Missing Values

Missing values were deliberately included in:

* Description
* CustomerID
* Country
* Quantity
* UnitPrice
* InvoiceDate

### Duplicate Records

The raw dataset contains **exact duplicate records**.

### Incorrect Data Types

Some numeric values were intentionally stored as text.

Examples:

```text
"five"
"ten"
"N/A"
"unknown"
```

### UnitPrice Formatting Problems

The `UnitPrice` column contains examples of:

* Currency symbols
* Comma decimal formatting
* Text-based numeric values

Example:

```text
£12.50
€15,75
$20.00
```

### ID Inconsistencies

Invoice and stock IDs contain mixed formats and data types.

### Date Inconsistencies

The `InvoiceDate` column contains mixed date formats.

### Country Inconsistencies

Examples include:

```text
UK
U.K.
uk
United kingdom
```

### Product Description Inconsistencies

Product descriptions contain:

* Extra spaces
* Different capitalization
* Inconsistent formatting

---

# 🧹 Cleaning Performed

## Python / Pandas

The following data-cleaning operations were performed using **Python and Pandas**.

### 1. Load Raw Dataset

The raw CSV file was loaded as strings so that data-type problems could be detected properly.

### 2. Remove Extra Whitespace

Leading and trailing spaces were removed from text fields.

### 3. Standardize InvoiceNo and StockCode

Invoice numbers and stock codes were cleaned and standardized.

### 4. Clean Quantity

The `Quantity` column was converted to numeric values.

Invalid entries were identified and replaced using the **median value**.

### 5. Clean UnitPrice

Currency symbols and formatting inconsistencies were removed.

The values were then converted into numeric format.

### 6. Clean CustomerID

Customer IDs were converted into numeric values.

Missing CustomerID values were filled using the **median value**.

### 7. Standardize Product Descriptions

Product descriptions were cleaned by:

* Removing unnecessary spaces
* Standardizing capitalization
* Improving consistency

### 8. Standardize Country Names

Country names were normalized.

For example:

```text
UK
U.K.
uk
United kingdom
```

were standardized to a consistent country representation.

### 9. Convert InvoiceDate

Mixed date formats were parsed and converted into a consistent datetime format.

### 10. Remove Duplicate Records

Exact duplicate records were identified and removed.

### 11. Export Cleaned Dataset

The final cleaned dataset was exported as:

```text
data/cleaned_retail_2000.csv
```

---

# 📊 Before vs After Summary

| Metric            | Before Cleaning | After Cleaning |
| ----------------- | --------------: | -------------: |
| Total Records     |           2,000 |          1,978 |
| Missing Cells     |             182 |              0 |
| Duplicate Records |              18 |              0 |
| Records Removed   |               — |             22 |

### Final Result

The final dataset contains:

**1,978 clean records**

with:

* No missing cells
* No exact duplicate records
* Standardized data types
* Standardized country names
* Standardized descriptions
* Consistent date format
* Clean numeric values

---

# 📑 Excel Workbook

The Excel workbook is available at:

```text
excel/SWYNEX_Data_Cleaning_2000.xlsx
```

It contains the following worksheets:

### `Raw_Data`

Original 2,000-record dataset containing the deliberately introduced data-quality problems.

### `Cleaned_Data`

Final cleaned dataset after applying the cleaning process.

### `Data_Quality_Report`

Contains:

* Missing-value checks
* Data-type checks
* Data-quality observations

### `Cleaning_Log`

Documents:

* Data-quality issue
* Cleaning action
* Result

### `Summary`

Contains before-and-after cleaning metrics.

---

# 🐍 Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Excel**
* **CSV**
* **Git**
* **GitHub**
