import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]  → Element-wise addition
print(a - b)   # [-3 -3 -3]  → Element-wise subtraction
print(a * b)   # [4 10 18]  → Element-wise multiplication
print(a / b)   # [0.25 0.4 0.5]  → Element-wise division
print(a ** 2)  # [1 4 9]  → Element-wise exponentiation


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)      # Matrix multiplication
print(A.T)        # Transpose of A
print(np.linalg.inv(A))  # Inverse of A