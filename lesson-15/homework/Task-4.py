import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.figure(figsize=(8,6))
plt.scatter(x, y, c=np.random.rand(100), marker='o', s=50, cmap='viridis', edgecolors='black')

plt.xlabel('x values')
plt.ylabel('y values')
plt.title("Scatter plot of 100 random points")
plt.grid(True)
plt.show()

