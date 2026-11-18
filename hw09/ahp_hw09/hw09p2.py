#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:25:52 2026

@author: anna
"""

import numpy as np
import matplotlib.pyplot as plt

# Part B

def EulerIntegrate(f, xstart, xstop, y0, h):
    yvals = np.array([y0])
    xvals = np.arange(xstart, xstop, h)
    
    for i in range(1, len(xvals)):
        yvals = np.append(yvals, yvals[-1] + h * f(xvals[i], yvals[-1]))
        
    return (xvals, yvals)

# Part C

def g(x):
    return 3.5 * np.e * np.exp(- x * x) + 0.5
    
def f1(x, y):
    return x - 2 * x * y

set1 = EulerIntegrate(f1, -1.0, 3.0, 4.0, .3)
set2 = EulerIntegrate(f1, -1.0, 3.0, 4.0, .1)
set3 = EulerIntegrate(f1, -1.0, 3.0, 4.0, .01)

plt.plot(set1[0], set1[1])
plt.plot(set2[0], set2[1])
plt.plot(set3[0], set3[1])
plt.plot(set3[0], g(set3[0]))
plt.legend([".3 Approximation", ".1 Approximation", ".01 Approximation", "Original Function"])
