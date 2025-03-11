import numpy as np

# 1. Vector from 10 to 49
task_1 = np.arange(10, 50)
print("Task 1: Vector from 10 to 49")
print(task_1)

# 2. 3x3 matrix with values 0-8
task_2 = np.arange(9).reshape(3, 3)
print("\nTask 2: 3x3 matrix with values 0-8")
print(task_2)

# 3. 3x3 identity matrix
task_3 = np.eye(3)
print("\nTask 3: 3x3 identity matrix")
print(task_3)

# 4. 3x3x3 array with random values
task_4 = np.random.random((3, 3, 3))
print("\nTask 4: 3x3x3 random array")
print(task_4)

# 5. 10x10 array with random values, find min and max
task_5 = np.random.random((10, 10))
min_val = np.min(task_5)
max_val = np.max(task_5)
print("\nTask 5: 10x10 random array - Min and Max")
print("Minimum value:", min_val, "Maximum value:", max_val)

# 6. Random vector of size 30, find mean
task_6 = np.random.random(30)
mean_val = np.mean(task_6)
print("\nTask 6: Mean of random vector of size 30")
print(mean_val)

# 7. Normalize a 5x5 random matrix
task_7 = np.random.random((5, 5))
normalized_7 = (task_7 - np.min(task_7)) / (np.max(task_7) - np.min(task_7))
print("\nTask 7: Normalized 5x5 random matrix")
print(normalized_7)

# 8. Multiply 5x3 matrix by 3x2 matrix
task_8_a = np.random.random((5, 3))
task_8_b = np.random.random((3, 2))
product = np.dot(task_8_a, task_8_b)
print("\nTask 8: 5x3 × 3x2 matrix product")
print(product)

# 9. Dot product of two 3x3 matrices
task_9_a = np.random.random((3, 3))
task_9_b = np.random.random((3, 3))
dot_product_9 = np.dot(task_9_a, task_9_b)
print("\nTask 9: Dot product of two 3x3 matrices")
print(dot_product_9)

# 10. Transpose of 4x4 matrix
task_10 = np.random.random((4, 4))
transpose_10 = np.transpose(task_10)
print("\nTask 10: Transpose of 4x4 matrix")
print(transpose_10)

# 11. Determinant of 3x3 matrix
task_11 = np.random.random((3, 3))
det_11 = np.linalg.det(task_11)
print("\nTask 11: Determinant of 3x3 matrix")
print(det_11)

# 12. 3x4 × 4x3 matrix product
task_12a = np.random.random((3, 4))
task_12b = np.random.random((4, 3))
product_ab1 = np.dot(task_12a, task_12b)
print("\nTask 12: 3x4 × 4x3 matrix product")
print(product_ab1)

# 13. 3x3 matrix × 3-element vector
mat_13 = np.random.random((3, 3))
vec_13 = np.random.random((3, 1))
product_ab2 = np.dot(mat_13, vec_13)
print("\nTask 13: 3x3 matrix × 3-element vector product")
print(product_ab2)

# 14. Solve Ax = b
A = np.random.random((3, 3))
b = np.random.random((3, 1))
x = np.linalg.solve(A, b)
print("\nTask 14: Solution to Ax = b")
print(x)

# 15. Row-wise and column-wise sums of 5x5 matrix
task_15 = np.random.random((5, 5))
row_sums = np.sum(task_15, axis=1)
col_sums = np.sum(task_15, axis=0)
print("\nTask 15: 5x5 matrix with row and column sums")
print("Matrix:")
print(task_15)
print("Row sums:", row_sums)
print("Column sums:", col_sums)