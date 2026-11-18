#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:47:26 2026

@author: anna
"""

import numpy as np

def myJacobi(A, b, w, tol):
    nmax = 1000

    Dinv = np.zeros_like(A) # I hope these are kosher? They ought to be...
    L = np.zeros_like(A)
    U = np.zeros_like(A)

    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                Dinv[i][j] = 1 / A[i][j]
            elif i < j:
                L[i][j] = A[i][j]
            else:
                U[i][j] = A[i][j]

    n = 0
    x = np.dot(Dinv, b)
    
    while (np.linalg.norm(np.dot(A, x) - b) > tol):
        x = np.dot(Dinv, b - w * np.dot(L + U, x))
        n += 1
        if n > nmax:
            return (n, x)

    return (n, x)

# Part B

A = np.array([[1.01, 0.99], [0.99, 1.01]])
b = np.array([2.0, 2.0])

(n, x) = myJacobi(A, b, 1, 0.001)
print(np.dot(A, b) - x)
