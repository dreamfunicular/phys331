#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 21:22:29 2026

@author: anna
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.pow(np.e, -x)

x = np.arange(-1, 1, 0.02)

y = np.array([])

for each in x:
    y = np.append(y, f(each))

co2 = np.polyfit(x, y, deg=2)
co3 = np.polyfit(x, y, deg=3)
co4 = np.polyfit(x, y, deg=4)

deg2 = np.poly1d(co2)
deg3 = np.poly1d(co3)
deg4 = np.poly1d(co4)

plt.plot(x, deg2(x))
plt.plot(x, deg3(x))
plt.plot(x, deg4(x))

plt.plot(x, y)

plt.legend(["2nd-degree", "3rd-degree", "4th-degree", "Data"])
plt.show()

def diff2(x):
    return deg2(x) - f(x)

def diff3(x):
    return deg3(x) - f(x)

def diff4(x):
    return deg4(x) - f(x)

plt.plot(x, diff2(x))
plt.plot(x, diff3(x))
plt.plot(x, diff4(x))

plt.show()
