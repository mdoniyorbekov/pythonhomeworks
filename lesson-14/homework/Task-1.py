import numpy as np
def far_to_cel(fahrenheit):
    celcius = (fahrenheit - 32)*5/9
    return celcius
vectorization = (np.vectorize(far_to_cel))
fah_temp = np.array([32, 68, 100, 212, 77])
cel_temp = vectorization(fah_temp)

for i in range(5):
    print(f"{fah_temp[i]} Fahrenheit is {cel_temp[i].round(2)} Celsius")