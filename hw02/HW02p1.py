# Template File for Homework 2, Problem 1
# PHYS 331
# Anna Lynch
import numpy as np
import matplotlib.pyplot as plt

def rf_bisect(f,xlo,xhi,xtol,nmax):
# Computes the value of the root for function f bracketed in the domain [xlo, xhi]. 
# PARAMETERS:
#   f     --  (function) The one-dimensional function to evaluate a root of.
#   xlo   --  (float) The lower limit of the bracket.
#   xhi   --  (float) The upper limit of the bracket.
#   xtol  --  (float) The tolerance the calculated root should achieve.
#   nmax  --  (int) The maximum number of iterations allowed.
# RETURNS: (root, iters) 
#   root  --  (float) A root of f that meets the tolerance tol
#   iters --  (int) The number of iteratons undergone.

#----> Implement your solution for rf_bisect here <-------
    # The loop logic otherwise allows a failure case in which at least one initial limit is within tolerance. In this case, that root becomes unreachable.
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
    

#----> Add your functions here <-------
# An example function that may be used to test rf_bisect
def func(x):
    return (x-0.5)**2

def f1(x):
    return (2 * x) - 3 * np.sin(x) - np.exp(x)

def f2(x):
    return np.pow(x, 3) - 0.125

def f3(x):
    return np.sin(1.0 / (x + 0.01))

def f4(x):
    return 1.0 / (x - 0.49)

#----> Do everything else here <-------
# Example: Find the root of func(x) and print the result
x = np.arange(-1.0, 1.0, 0.01)

ax = plt.gca()
ax.set_ylim([-5, 5])
plt.plot(x, f1(x))
plt.plot(x, f2(x))
plt.plot(x, f3(x))
plt.plot(x, f4(x))
plt.show()

(root1,iters1) = rf_bisect(f1, -1, 1, 1e-10, 50)
print(root1)
(root2,iters1) = rf_bisect(f2, -1, 1, 1e-10, 50)
print(root2)
(root3,iters1) = rf_bisect(f3, -1, 1, 1e-10, 50)
print(root3)
(root4,iters1) = rf_bisect(f4, -1, 1, 1e-10, 50)
print(root4)
# print('Root of func: ' + str(root1))
# print('# iterations: ' + str(iters1))
# fval1 = func(root1)
# print(str(func.__name__) + ' evaluated at root is: ' + str(fval1))



