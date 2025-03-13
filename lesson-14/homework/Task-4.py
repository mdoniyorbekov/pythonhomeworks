import numpy as np

A = np.array([[10, -2, 3],
              [3, -1, 1],
              [2, 1, -2]])
B = np.array([12, -5, 15])

I1 = np.linalg.solve(A, B)[0]
I2 = np.linalg.solve(A, B)[1]
I3 = np.linalg.solve(A, B)[2]

print(f"I1 = {I1}")
print(f"I2 = {I2}")
print(f"I3 = {I3}")