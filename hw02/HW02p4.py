import numpy as np
import matplotlib.pyplot as plt 

def g(a, x):
    return a * np.cos(x)

# Rewrote the function to take a and the number of iterations as arguments
def fixedPoint(a, x, iter):
    for i in range(iter):
        print(x)
        x = g(a, x)
    return x 

x = fixedPoint(1, .1, 25)
print(x)

print("The purported root", x, "yields f(x)=", x - g(1, x))

print(fixedPoint(1, -1, 25))
print(fixedPoint(1, -10, 25))
print(fixedPoint(1, 100, 25))
print(fixedPoint(1, 10000, 25))

print(fixedPoint(1.2, 0.1, 50))
print(fixedPoint(1.2, 0.7, 50))
print(fixedPoint(1.2, - np.pi * 1000 / 2, 500))

print(fixedPoint(2, 0.1, 50))
print(fixedPoint(2, 1, 50))
print(fixedPoint(2, -1, 50))