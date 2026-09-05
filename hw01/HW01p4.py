import numpy as np 
import matplotlib.plt as plt

def firstOrder(x):
    return 1 + x

def secondOrder(x):
    return 1 + x + ((x ** 2) / 2)

def thirdOrder(x):
    return 1 + x + ((x ** 2) / 2) + ((x ** 3) / 6)

x = np.arange(-3, 3, 0.01)

plt.plot(x, np.exp(x), label="The Exponential Function")
plt.plot(x, firstOrder(x), label="First Order Taylor Approximation")
plt.plot(x, secondOrder(x), label="Second Order Taylor Approximation")
plt.plot(x, thirdOrder(x), label="Third Order Taylor Approximation")

plt.title("Comparison of Taylor Approximations of the Exponential Function")
plt.legend()
plt.show()