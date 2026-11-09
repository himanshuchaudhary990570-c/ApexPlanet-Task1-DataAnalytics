# ApexPlanet Data Analytics Internship – Task 1
## Data Immersion & Wrangling

This repository contains the Task 1 data cleaning work using Python and Pandas.

### Files
- `data_dictionary.csv` – meaning, data type, and business relevance of each field.
- `data_quality_report.csv` – missing values and uniqueness profile before cleaning.
- `cleaned_sales_dataset.csv` – cleaned analysis-ready data.
- `data_cleaning_report.md` – data quality findings and cleaning decisions.
- `clean_data.py` – reproducible cleaning script.
- `ApexPlanet_DataAnalytics_Dataset.xlsx` – original dataset (add this file if you want the script to run locally).

### Run the script
Install dependencies:
```bash
pip install pandas openpyxl
```
Place the original Excel file in this folder, then run:
```bash
python clean_data.py
```

### Cleaning summary
- Standardized date and text formatting.
- Removed duplicate Order_ID records (first record retained).
- Filled missing Age with median and missing City with `Unknown`.
- Recalculated `Total_Sales = Quantity * Unit_Price`.
