import numpy as np

# Define two NumPy arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# Concatenate arrays horizontally
result = np.concatenate((a, b), axis=1)

print("Concatenated array horizontally:\n", result)
