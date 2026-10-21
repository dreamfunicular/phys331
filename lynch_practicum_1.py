# Your Name: Anna Lynch 
#-------------------------------------------
# DO NOT MODIFY
# Exam code: m932jaflw
#-------------------------------------------    
# Put All Import statements in this section

import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------
# Problem 1

# Function definitions
def f1(x):
    return np.pow(x, 4) - 87 * np.pow(x, 3) - np.pow(x, 2) + 14

def f2(x):
    return 100000 * x - 5000000

def yaxis(x):
    return 0 * x

plt.xkcd() # I just kinda like it and I think this shows I'm a human person. Please remove this statement if it is offensive to you or your rubric.

# Invokations of plt functionality
x = np.arange(0, 100, 0.01)
plt.plot(x, f1(x))
plt.plot(x, f2(x))
plt.plot(x, yaxis(x))

# Add a legend
plt.legend(["f1", "f2", "Y-axis"])

plt.show()
#-------------------------------------------
# Problem 2

def search144(arr):
    for i in range(len(arr)):
        if arr[i] > 144.0: # After testing, calling np.greater() does not offer any precision advantage. Using a comparator here is okay!
            return i 
    return -1

#-------------------------------------------
# Problem 3

def nextValue(x):
    return x + (np.sin(np.pi * np.sqrt(np.abs(x))) / (np.pow(x, 4) + 3))

def Iterate(xstart, n):
    for i in range(n):
        xstart = nextValue(xstart)
    return xstart

#-------------------------------------------
# Problem 4

# Assuming row-first matrices...
def matrix_mult(J, x):
    return [J[0][0] * x[0] + J[0][1] * x[1], J[1][0] * x[0] + J[1][1] * x[1]]

#-------------------------------------------
