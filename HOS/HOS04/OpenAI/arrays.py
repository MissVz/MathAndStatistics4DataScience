# HOS04 - Section 2: NumPy - Arrays

import numpy as np

# Create numpy arrays
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Use np.arange, np.zeros, np.ones
print("Arange:", np.arange(10))
print("Zeros:", np.zeros((2,3)))
print("Ones:", np.ones((2,3)))

# Indexing and slicing
a = np.array([10,20,30,40,50])
print("Index 1 to 3:", a[1:4])

# Integer indexing
x = np.array([[1, 2], [3, 4], [5, 6]])
rows = np.array([0, 1, 2])
cols = np.array([0, 1, 0])
print("Integer Indexed:", x[rows, cols])
