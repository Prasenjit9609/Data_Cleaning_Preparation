"""
SWYNEX Task 1 - Data Cleaning & Preparation
Dataset: 2,000-record educational retail dataset modeled on the UCI Online Retail schema.

Run:
    python scripts/clean_retail_data.py
"""
from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw_retail_2000.csv"
OUT = ROOT / "data" / "cleaned_retail_2000.csv"

df = pd.read_csv("data/raw_retail_2000.csv", dtype=str)

for c in df.columns:
    df[c] = df[c].astype("string").str.strip()

df["InvoiceNo"] = df["InvoiceNo"].str.upper().str.replace(r"\.0$", "", regex=True)
df["StockCode"] = df["StockCode"].str.upper().str.replace(r"\.0$", "", regex=True)

df["Quantity"] = df["Quantity"].str.replace(r"[^0-9\-]", "", regex=True).replace({"": pd.NA})
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median()).round().astype("Int64")

df["UnitPrice"] = df["UnitPrice"].str.replace("£","",regex=False).str.replace(",","." ,regex=False)
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
df["UnitPrice"] = df["UnitPrice"].fillna(df["UnitPrice"].median()).round(2)

df["CustomerID"] = pd.to_numeric(df["CustomerID"], errors="coerce")
df["CustomerID"] = df["CustomerID"].fillna(df["CustomerID"].median()).round().astype("Int64")

df["Description"] = df["Description"].astype("string").str.replace(r"\s+"," ",regex=True).str.upper()

country_map = {
    "UK":"United Kingdom","U.K.":"United Kingdom","ENGLAND":"United Kingdom",
    "UNITED KINGDOM":"United Kingdom","FRANCE":"France","GERMANY":"Germany",
    "SPAIN":"Spain","NETHERLANDS":"Netherlands","BELGIUM":"Belgium"
}
df["Country"] = df["Country"].astype("string").str.upper().str.strip().map(country_map).fillna(
    df["Country"].astype("string").str.title()
).fillna("Unknown")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce", dayfirst=False)
df["InvoiceDate"] = df["InvoiceDate"].fillna(pd.Timestamp("2011-01-01"))

df = df.drop_duplicates().reset_index(drop=True)

df.to_csv("data/cleaned_retail_2000.csv", index=False)
print("Cleaned file:", "data/cleaned_retail_2000.csv")
print("Rows:", len(df))
print("Missing cells:", int(df.isna().sum().sum()))
print("Duplicates:", int(df.duplicated().sum()))
