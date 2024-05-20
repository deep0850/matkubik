import numpy as np
import matplotlib.pyplot as plt

def f(x, N=5, alpha=0.5):
    return N * (x/N + 1/2)**alpha - N/2

x = np.linspace(0, 1, 100)

y = f(x)

plt.plot(x, y)

plt.title('Function f(x) = N * (x/N + 1/2)^α - N/2 for N=5 and α=0.5')
plt.xlabel('x')
plt.ylabel('y')

plt.show()