import numpy as np
import matplotlib.pyplot as plt

# Problem 1
def plot_tanh(xlim, dx):
    x = np.arange(-xlim, xlim, dx)

    plt.plot(x, np.tanh(x))
    plt.show()

plot_tanh(3.0, 1.0)
plot_tanh(3, 0.3)
plot_tanh(3, 0.1)
plot_tanh(3, 0.03)

def plot_tanh2(a):
    x = np.arange(-5, 5, 0.01)

    plt.plot(x, np.tanh(a * x))

plot_tanh2(0.5)
plot_tanh2(1.0)
plot_tanh2(2.2)
plt.show()

# Problem 2