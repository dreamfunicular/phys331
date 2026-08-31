# Anna Lynch, 2026

import numpy as np
import matplotlib.pyplot as plt

# Parts a, b, c
def f(sigma, x):
    return 1 * np.exp((-x * x) / (2 * sigma * sigma)) + 10000

def dfTrue(sigma, x):
    return (-x / (sigma * sigma)) * np.exp((-x * x) / (2 *sigma * sigma))

def dfNumerical(sigma, x, dx):
    return ((f(sigma, x + (dx / 2)) - f(sigma, x - (dx / 2))) / dx)


# Part d
a = np.arange(-8, 8, 0.01)
plt.plot(a, dfTrue(1, a))
plt.plot(a, dfNumerical(1, a, 0.1))
plt.show()

# Part e
def error(sigma, x):
    return 100 * ((dfTrue(sigma, x) - dfNumerical(sigma, x, 0.1)) / dfTrue(sigma, x))

plt.plot(a, error(1, a))
plt.show()