#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:47:26 2026

@author: anna
"""

import numpy as np

def myJacobi(A, b, w, tol):
    nmax = 1000

    Dinv = np.zeros_like(A)
    L = np.zeros_like(A)
    U = np.zeros_like(A)

    print(len(A))
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                Dinv[i][j] = 1 / A[i][j]
            elif i < j:
                L[i][j] = A[i][j]
            elif i > j:
                U[i][j] = A[i][j]

    print(Dinv)
    print(L)
    print(U)

    n = 0
    x = np.dot(Dinv, b)
    
    while (np.linalg.norm(np.dot(A, x) - b) > tol):
        x = np.dot(Dinv, b - np.dot(L + U, x))
        print(x)
        n += 1
        if n > nmax:
            return (n, x)

    return (n, x)

A = np.array([[1.01, 0.99], [0.99, 1.01]])
b = np.array([2.0, 2.0])

(n, x) = myJacobi(A, b, 1, 0.001)