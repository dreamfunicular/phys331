#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 20:54:57 2026

@author: anna
"""

import numpy as np

# Part A

def triSolve(A, b, upperOrLower):
    n = len(A)
    x = [0] * n
    
    # If lower
    if upperOrLower == 0:
        for i in range(n):
            diff = b[i]
            for j in range(i):
                # Modify diff based on x[i] and A[i][j] for each j < i (values left of the diagonal)
                diff -= x[j] * A[i][j]
            # Divide the diff by A[i][i] (the diagonal). Assign this value to x[i]
            x[i] = diff / A[i][i]
    elif upperOrLower == 1:
        for i in range(n-1, -1, -1):
            diff = b[i]
            for j in range(n-1, i, -1):
                # Modify diff based on x[i] and A[i][j] for each j < i (values left of the diagonal)
                diff -= x[j] * A[i][j]
            # Divide the diff by A[i][i] (the diagonal). Assign this value to x[i]
            print(i, i)
            x[i] = diff / A[i][i]

    return x

# Part B

def checkSolve(A, x, b):
    n = len(A)
    
    for i in range(n):
        for j in range(n):
            b[i] -= A[i][j] * x[j]
    
    return b

# Part C

A1 = [[9, 0, 0], [-4, 2, 0], [1, 0, 5]]
b1 = [8, 1, 4]
x1 = triSolve(A1, b1, 0)

print(checkSolve(A1, x1, b1))

A2 = [[2, 4, 5], [0, 2, -4], [0, 0, 5]]
b2 = [-4, 9, 4]
x2 = triSolve(A2, b2, 1)

print(checkSolve(A2, x2, b2))

# Part D

def lowerTriangularMatrix(n):
    A = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1):
            A[i][j] = np.random.random()
    
    return A

def randomColumnMatrix(n):
    b = [0] * n
    for i in range(len(b)):
        b[i] = np.random.random()
    return b

for n in [3, 10, 30, 100]:
    A = lowerTriangularMatrix(n)
    b = randomColumnMatrix(n)
    
    x = triSolve(A, b, 0)
    print(checkSolve(A, x, b))