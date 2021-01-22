import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 2


x = np.linspace(-10, 10)
y = f(x)

plt.plot(x, y, c="r")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot")
plt.show()
