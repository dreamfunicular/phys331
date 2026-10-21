import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.pow(x, 5) - 3 * np.pow(x, 3) + 15 * np.pow(x, 2) + 27 * x + 5

def fPrime(x):
    return 5 * np.pow(x, 4) - 9 * np.pow(x, 2) + 30 * x + 27

def next(xn):
    return xn - f(xn) / fPrime(xn)

def Newt(xstart, tol, nmax):
    xn = xstart
    if np.abs(f(xn)) <= tol:
        return xn

    for i in range(nmax):
        xn = next(xn)

        if np.abs(f(xn)) <= tol:
            return xn

x = np.arange(-2.2, 0, 0.01)
plt.plot(x, f(x))
plt.show()

print(Newt(-2.15, 10e-15, 15))
