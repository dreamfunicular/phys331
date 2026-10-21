#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 20:47:51 2026

@author: anna
"""

import numpy as np
import matplotlib.pyplot as plt

# Part B
def checkConditioning(tvec):
    A = np.array([
        [1, tvec[0], tvec[0] * tvec[0]],
        [1, tvec[1], tvec[1] * tvec[1]],
        [1, tvec[2], tvec[2] * tvec[2]]
    ])
    
    n = 0
    for i in range(3):
        for j in range(3):
            n += A[i][j] * A[i][j]
    n = np.sqrt(n)
    
    d = np.abs(np.linalg.det(A))
    
    return d / n

# Part C
def checkConditioningWithInterval(dt):
    return checkConditioning([0, dt, 2 * dt])

x = np.arange(0.1, 5, 0.02)
y = np.array([])
for each in x:
    y = np.append(y, checkConditioningWithInterval(each))
    
plt.plot(x, y)
plt.ylabel("Conditioning Number")
plt.xlabel("delta-t")
plt.show()

# Part D
def checkConditioningWithMidpoint(t):
    return checkConditioning([0, t, 10])

x = np.arange(0.1, 10, 0.02)
y = np.array([])
for each in x:
    y = np.append(y, checkConditioningWithMidpoint(each))
    
plt.plot(x, y)
plt.ylabel("Conditioning Number")
plt.xlabel("Midpoint t")
plt.show()

# Part E
tvec = [0, 5, 10]

A = np.array([
    [1, tvec[0], tvec[0] * tvec[0]],
    [1, tvec[1], tvec[1] * tvec[1]],
    [1, tvec[2], tvec[2] * tvec[2]]
])

b = np.array([0.3, 4.425, 14.3])

x = np.linalg.solve(A, b)
print(x)
tvec = [0, 1, 10]
A = np.array([
    [1, tvec[0], tvec[0] * tvec[0]],
    [1, tvec[1], tvec[1] * tvec[1]],
    [1, tvec[2], tvec[2] * tvec[2]]
])

b = np.array([0.3, 0.665, 14.3])

x = np.linalg.solve(A, b)
print(x)
