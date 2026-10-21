#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:55:49 2026

@author: anna
"""

import numpy as np

# Part a

A1 = np.array([[3, -3, 3], [3, 5, 1], [-3, 1, 5]])
b1 = np.array([9, -7, 12])

x1 = np.linalg.solve(A1, b1)

diff = np.matmul(A1, x1) - b1
print(diff)
if np.dot(diff, np.array([0, 0, 0])) < 0.00001:
    print("Solution validated")
    
# Part b
    
A2 = np.array([[4, 8, 20], [8, 13, 16], [20, 16, -91]])
b2 = np.array([24, 17, -119])

x2 = np.linalg.solve(A2, b2)

diff = np.matmul(A2, x2) - b2
print(diff)
if np.dot(diff, np.array([0, 0, 0])) < 0.00001:
    print("Solution validated")
    
# Part c
A1inv = np.linalg.inv(A1)
print(x1)
x1 = np.matmul(A1inv, b1)
print(x1)

A2inv = np.linalg.inv(A2)
print(x2)
x2 = np.matmul(A2inv, b2)
print(x2)