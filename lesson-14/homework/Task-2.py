import numpy as np
def function(num, pow):
    return num ** pow

nums = np.array([2, 3, 4, 5])
pows = np.array([1, 2, 3, 4])

vectorization = np.vectorize(function)
print (vectorization(nums, pows))