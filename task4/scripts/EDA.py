from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT.parent / "Task1" / "data" / "cleaned_retail_2000.csv"

df = pd.read_csv(INPUT)
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
df["Sales"] = df["Quantity"] * df["UnitPrice"]
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)
df["DayOfWeek"] = df["InvoiceDate"].dt.day_name()

print("Records:", len(df))
print("Unique invoices:", df["InvoiceNo"].nunique())
print("Unique products:", df["StockCode"].nunique())
print("Unique customers:", df["CustomerID"].nunique())
print("Countries:", df["Country"].nunique())
print("Total sales:", df["Sales"].sum())
print("Negative-quantity lines:", (df["Quantity"] < 0).sum())

print("\nTop countries by sales:")
print(df.groupby("Country")["Sales"].sum().sort_values(ascending=False).head(10))

print("\nTop products by sales:")
print(df.groupby(["StockCode","Description"])["Sales"].sum().sort_values(ascending=False).head(10))
