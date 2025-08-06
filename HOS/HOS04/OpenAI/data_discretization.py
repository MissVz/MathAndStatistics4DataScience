# HOS04 - Section 6: Data Discretization

import numpy as np
import pandas as pd

# Create random data
np.random.seed(0)
data = np.random.randint(10, 200, 10)

# Discretize with np.digitize
bins_2 = [50]
categories_2 = np.digitize(data, bins_2)
print("2-bin categories:", categories_2)

bins_3 = [50, 100]
categories_3 = np.digitize(data, bins_3)
print("3-bin categories:", categories_3)

# DataFrame for cut/qcut
df = pd.DataFrame({'height': data})

# Using cut
df['cut'] = pd.cut(df['height'], bins=[0, 25, 50, 100, 200], labels=[1, 2, 3, 4])
df['cut_label'] = pd.cut(df['height'], bins=[0, 25, 50, 100, 200], labels=["Short", "Medium", "Tall", "Very Tall"])

# Using qcut
df['qcut'] = pd.qcut(df['height'], q=5)

# Grade example
grades = [88, 92, 79, 93, 85, 91, 78, 99, 82, 73]
grade_cats = pd.cut(grades, bins=[0, 60, 70, 80, 90, 100], labels=["F", "D", "C", "B", "A"])
df_grades = pd.DataFrame({'grade': grades, 'category': grade_cats})
print("Grades Categorized:
", df_grades)

# Bar plot of grade counts
df_grades['category'].value_counts().sort_index().plot.bar(title='Grade Distribution')
