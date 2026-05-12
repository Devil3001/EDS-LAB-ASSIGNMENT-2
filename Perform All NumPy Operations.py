import numpy as np

# Create arrays
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# Basic operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Shape and size
print("Shape:", a.shape)
print("Size:", a.size)
print("Data Type:", a.dtype)

# Reshape
c = a.reshape(2, 2)
print("Reshaped Array:\n", c)

# Zeros and Ones
print("Zeros:\n", np.zeros((2,2)))
print("Ones:\n", np.ones((3,3)))
