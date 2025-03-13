import numpy as np
A = np.array([[4, 5, 6],
             [3, -1, 1],
             [2, 1, -2]])
B = np.array([7, 4, 5])
x, y, z = np.linalg.solve(A, B)

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")