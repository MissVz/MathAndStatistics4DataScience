# HOS04 - Section 4: Read and Write with pandas

import pandas as pd

# Read the CSV file
df = pd.read_csv("sales_data_sample.csv", encoding='latin-1')

# Display columns
print("Columns:
", df.columns)

# Write to new CSV with selected columns
df[['ORDERNUMBER', 'QUANTITYORDERED', 'PRICEEACH', 'ORDERDATE']].to_csv("new_sales.csv", index=False)
