import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-10,10, 400)
x2 = np.linspace(0, 10, 400)
y1= x1**3
y2 = np.sin(x1)
y3 = np.exp(x2)
y4 = np.log(x2+1)

fig, axc = plt.subplots(2, 2, figsize=(12, 10))

axc[0, 0].plot(x1, y1, 'b')
axc[0, 0].set_title('$f(x)=x^3$')
axc[0, 0].set_xlabel('x')
axc[0, 0].set_ylabel('f(x)')

axc[0, 1].plot(x1, y2, 'r')
axc[0, 1].set_title('$f(x)=\sin(x)$')
axc[0, 1].set_xlabel('x')
axc[0, 1].set_ylabel('f(x)')

axc[1, 0].plot(x2, y3, 'g')
axc[1, 0].set_title('$f(x)=e^x$')
axc[1, 0].set_xlabel('x')
axc[1, 0].set_ylabel('f(x)')

axc[1, 1].plot(x2, y4, 'm')
axc[1, 1].set_title('$f(x)= \log(x+1)$')
axc[1, 1].set_xlabel('x')
axc[1, 1].set_ylabel('f(x)')

plt.tight_layout
plt.show()