import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = x**2+4*x+4

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='$f(x)=x^2+4x+4$')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('$f(x)=x^2+4x+4$')
plt.grid(True)
plt.legend()
plt.show()

