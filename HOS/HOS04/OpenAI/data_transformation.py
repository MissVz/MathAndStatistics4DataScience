# HOS04 - Section 5: Data Transformation

import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})

# Use transform to add 10
df_transformed = df.transform(lambda x: x + 10)
print("Transformed DataFrame:
", df_transformed)
