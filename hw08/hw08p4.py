#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:46:42 2026

@author: anna
"""

import numpy as np

# Part A

def Make_Hermitian(n):
    arr = np.zeros((n, n), dtype=complex)
    
    for i in range(n):
        for j in range(i +1):
            if i == j:
                arr[i][j] = np.random.random()
            else:
                a = np.random.random() 
                b = np.random.random() * 1j
                arr[i][j] = a + b
                arr[j][i] = a - b
    return arr

# Part B
A = Make_Hermitian(5)
print(np.array_equal(A, np.transpose(np.conjugate(A))))

eig = np.linalg.eig(A)
evals = eig[0]
print(evals)

# Part C
evecs = eig[1]
dp = np.dot(evecs[:,0], np.conjugate(evecs[:,1]))

if dp <= 0.0001:
    print("The matrices are orthogonal")
else:
    print("The matrices are not orthogonal")