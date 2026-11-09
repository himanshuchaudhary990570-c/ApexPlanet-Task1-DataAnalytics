# Task 1 – Data Immersion & Wrangling

## Dataset
ApexPlanet_DataAnalytics_Dataset.xlsx | Sheet: Sales_Dataset

- Raw rows: 1000
- Raw columns: 12
- Duplicate full rows: 0
- Duplicate Order_ID records beyond first: 8
- Missing Age values: 20
- Missing City values: 13
- Clean rows: 992
- Rows removed due to duplicate Order_ID: 8
- Missing Age values after cleaning: 0
- Missing City values after cleaning: 0

## Cleaning decisions
1. Parsed `Order_Date` into a date and standardized output to `YYYY-MM-DD`.
2. Trimmed leading/trailing whitespace from text/category fields and standardized Gender capitalization.
3. Removed duplicate `Order_ID` records, retaining the first occurrence.
4. Filled missing Age with the median age (41.0), rounded to an integer.
5. Filled missing City with `Unknown`.
6. Recalculated `Total_Sales` as `Quantity × Unit_Price` to enforce the business rule.
7. Exported the analysis-ready data as `cleaned_sales_dataset.csv`.

## Deliverables
- `data_dictionary.csv`
- `data_quality_report.csv`
- `cleaned_sales_dataset.csv`
- `clean_data.py`
- `README.md`
