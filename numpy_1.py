"""
NumPy Basics Tutorial
From : Infite Learn
Description: This file explains NumPy basics with examples for students.
"""

import numpy as np



# 1. ARRAY CREATION


# 1D Array
arr = np.array([1, 2, 3])
print("1D Array:", arr)
print("Type:", type(arr))
print("Shape:", arr.shape)


# 2D Array
arr2 = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10]])
print("\n2D Array Shape:", arr2.shape)   # (rows, columns)



# 2. SPECIAL NUMPY FUNCTIONS


# arange()
print("\nArange:", np.arange(0, 10, 2))

# reshape()
arr3 = np.array([1, 2, 3, 4, 5])
print("Reshape (5x1):\n", arr3.reshape(5, 1))

# ones()
print("\nOnes Matrix:\n", np.ones((3, 4)))

# zeros()
print("\nZeros Matrix:\n", np.zeros((3, 4)))

# identity matrix
print("\nIdentity Matrix:\n", np.eye(4))



# 3. ARRAY PROPERTIES


arr4 = np.array([1, 2, 3])

print("\nDimensions:", arr4.ndim)
print("Size:", arr4.size)
print("Data Type:", arr4.dtype)
print("Item Size (bytes):", arr4.itemsize)



# 4. VECTORIZED OPERATIONS


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

print("\nAddition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)



# 5. UNIVERSAL FUNCTIONS


arr = np.array([1, 2, 3, 4])

print("\nSquare Root:", np.sqrt(arr))
print("Exponential:", np.exp(arr))
print("Sine:", np.sin(arr))
print("Log:", np.log(arr))



# 6. INDEXING & SLICING


arr = np.array([
    [1, 2, 3, 4],
    [6, 7, 8, 9],
    [10, 11, 12, 13]
])

print("\nElement [2][0]:", arr[2][0])
print("Rows from index 1:\n", arr[1:])
print("Submatrix [1:,2:]:\n", arr[1:, 2:])
print("Submatrix [0:2,2:]:\n", arr[0:2, 2:])
print("Submatrix [1:,1:]:\n", arr[1:, 1:])



# 7. MODIFY ARRAY


arr[0, 3] = 90
print("\nModified Array:\n", arr)

arr[1:] = 100
print("After Bulk Update:\n", arr)



# 8. STATISTICS (NORMALIZATION)


arr = np.array([1, 2, 3, 4, 5])

mean = np.mean(arr)
std = np.std(arr)

normalized = (arr - mean) / std

print("\nNormalized Data:", normalized)
print("Median:", np.median(arr))
print("Variance:", np.var(arr))



# 9. LOGICAL OPERATIONS


data = np.array([1,2,3,4,5,5,6,7,8,9,10])

print("\nLess than 5:", data < 5)
print("Filtered (<5):", data[data < 5])
print("Between 5 and 6:", data[(data >= 5) & (data <= 6)])