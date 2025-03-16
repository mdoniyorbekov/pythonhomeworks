import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 400)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, 'b-o', label='$\sin(x)$')
plt.plot(x, y_cos, 'r--s', label='$\cos(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $\sin(x)$ and $\cos(x)$')
plt.grid(True)
plt.legend()
plt.show()

