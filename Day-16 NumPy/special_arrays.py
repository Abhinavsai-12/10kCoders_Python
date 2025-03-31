import numpy as np

print(np.zeros((2, 3)))      # 2x3 matrix filled with 0s
print(np.ones((3, 3)))       # 3x3 matrix filled with 1s
print(np.eye(4))             # 4x4 identity matrix
print(np.arange(1, 10, 2) )  # [1, 3, 5, 7, 9] (like range())
print(np.linspace(0, 5, 10)) # 10 evenly spaced numbers from 0 to 5