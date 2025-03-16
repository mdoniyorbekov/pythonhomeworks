import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=1000)
plt.figure (figsize=(8,6))
plt.hist(data, bins=30, color='blue', alpha=0.7, edgecolor='black')

plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title("Histogram of 1000 Values from Normal Distribution (mean=0, std=1)")

plt.show()