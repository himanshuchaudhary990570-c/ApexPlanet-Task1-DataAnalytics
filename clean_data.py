import pandas as pd

INPUT_FILE = "ApexPlanet_DataAnalytics_Dataset.xlsx"
OUTPUT_FILE = "cleaned_sales_dataset.csv"

df = pd.read_excel(INPUT_FILE, sheet_name="Sales_Dataset")

# Standardize dates and text fields
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
for col in ["City", "Gender", "Product", "Category"]:
    df[col] = df[col].astype("string").str.strip()
df["Gender"] = df["Gender"].str.title()
df["City"] = df["City"].replace("", pd.NA)

# Keep the first record for each Order_ID
df = df.drop_duplicates(subset=["Order_ID"], keep="first")

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median()).round().astype("Int64")
df["City"] = df["City"].fillna("Unknown")

# Recalculate sales amount
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Standardize date format and export
df["Order_Date"] = df["Order_Date"].dt.strftime("%Y-%m-%d")
df.to_csv(OUTPUT_FILE, index=False)
print(f"Cleaning complete. Saved {OUTPUT_FILE} with {len(df)} rows.")
