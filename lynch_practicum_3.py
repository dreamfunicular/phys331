# Your Name: Anna Lynch
#-------------------------------------------
# DO NOT MODIFY
# Exam code: 823hfa32h3
#-------------------------------------------    
# Put All Import statements in this section
import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------
# Problem 1

A = np.array([[-2.0, 1.0, 3.0], [4.0, -8.0, 0.0], [7.0, -5.0, 9.0]])

(evals, evecMatrix) = np.linalg.eig(A)
evecs = [evecMatrix[:,0], evecMatrix[:,1], evecMatrix[:,2]]

for i in range(3):
    print("Eigenvalue", i, ":", evals[i], "with eigenvector", evecs[i])
    
#------------------------------------------
# Problem 2
def x(t):
    return np.cos(4.0 * np.pi * t) + 5.0 * np.sin(-3.0 * np.pi * t)

# Sample x(t)
t = np.arange(0, 10, 0.02)
y = x(t)

# Compute the DFT
sp = np.fft.fft(y)

# Plot the absolute value of the result against frequency
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq, np.abs(sp.real))

# Format the plot as prescribed
plt.legend(["Discrete Fourier Transform of x(t)"])
plt.xlabel("Hz")

# Cover the range from 0 to the Nyquist frequency

plt.show()

#-------------------------------------------
# Problem 3
def yPrime(x):
    return 0.2 * np.sin(5.0 * x)

def increment(x, h):
    return h * yPrime(x)

h = 0.05

# Variable shadowing is bad practice, but honestly this is clearest for the task. Too bad!
x = np.arange(0.0, 2.0, 0.05)
y = np.zeros(len(x))
y[0] = 7

for i in range(1, len(x)):
    y[i] = y[i- 1] + increment(x[i - 1], h)
    
plt.plot(x, y)
plt.legend(["Euler's Method Approximation for y(x)"])
plt.show()

#-------------------------------------------



