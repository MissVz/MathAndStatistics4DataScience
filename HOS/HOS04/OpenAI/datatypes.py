# HOS04 - Section 2: NumPy - Datatypes

import numpy as np

# Display how NumPy describes data types
data_type = np.dtype(np.int32)
print("Data Type Info:", data_type)

# Define a structured data type
student_dtype = np.dtype([('name', 'S10'), ('age', 'i4'), ('points', 'f4')])

# Create an ndarray object with the structured data type
students = np.array([("John", 21, 88.5), ("student2withlongname", 19, 92.3)], dtype=student_dtype)

print("Structured Array:
", students)
