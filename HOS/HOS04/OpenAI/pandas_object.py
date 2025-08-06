# HOS04 - Section 3: Pandas Object

import pandas as pd

# Create a Series
buyer = pd.Series([35000, 42000, 29000], index=['Tom', 'Jack', 'Steve'])
print("Series:
", buyer)

# Access using label
print("Access by label:", buyer.loc['Tom'])

# Create DataFrame
data = {'name': ['Tom', 'Jack', 'Steve'], 'salary': [35000, 42000, 29000]}
df = pd.DataFrame(data)
print("DataFrame:
", df)

# Custom index
df_custom = pd.DataFrame(data, index=['emp1', 'emp2', 'emp3'])
print("Custom Index:
", df_custom)
