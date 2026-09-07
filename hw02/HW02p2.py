import numpy as np 
import matplotlib.pyplot as plt

# Implements the Bernoulli's Equation for fluid flow relevant to the problem.
def bern(h):
    Q = 1.2
    g = 9.81
    b = 1.8
    h0 = 0.6
    H = 0.035

    return ((Q * Q) / (2 * g * b * b * h * h)) + h + H - (Q * Q) / (2 * g * b * b * h0 * h0) - h0

# Bisection root-finding algorithm
def rf_bisect(f,xlo,xhi,xtol,nmax):
    if np.abs(f(xlo)) <= xtol:
        return (root, i)
    if np.abs(f(xlo)) <= xtol:
        return (root, i)

    x = (xlo + xhi) / 2.0
    for i in range(1, nmax): # God I hate Python
        if np.abs(f(x)) <= xtol:
            return (x, i)
        
        # Assign the limit with the same sign as x to x
        if (f(x) * f(xlo) > 0):
            xlo = x
            x = (xlo + xhi) / 2.0
        else:
            xhi = x
            x = (xlo + xhi) / 2.0
    
    print("Error: bisection algorithm timed out")
    return (None, nmax)

x = np.arange(-0.4, 0.8, 0.01)
plt.plot(x, bern(x))
plt.show()

(root, iters) = rf_bisect(bern, -1, -0, 1e-10, 50)
print(root)
(root, iters) = rf_bisect(bern, 0.2, 0.3, 1e-10, 50)
print(root)
(root, iters) = rf_bisect(bern, 0.5, 0.6, 1e-10, 50)
print(root)