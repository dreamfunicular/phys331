#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:04:05 2026

@author: anna
"""

import numpy as np

# Part A

def proj(v1, v2):
    return np.dot(np.dot(v1, v2) / (np.dot(v1, v1)), v1)

def Gram_Schmidt(v1, v2):
    p = proj(v1, v2)
    
    # We are not required to normalize, but let's do so here
    vp2 = v2 - p
    vp2 = vp2 / np.dot(vp2, vp2)
    
    return vp2


# Part B

A = [[12., -34., -20., 27.], [14., -37., -21., 28.], [0.,  2., 0., -2.], [14.0, -34.0, -20.0, 25.0]]

eig = np.linalg.eig(A)

evals = eig[0]
evecs = [eig[1][:,0], eig[1][:,1], eig[1][:,2], eig[1][:,3]]

print("Eigenvalues of A:", evals)
print("Eigenvectors of A:", evecs)

# Part C

new = Gram_Schmidt(evecs[1], evecs[3])
print("New eigenvector (evecs[3] less evecs[3] projected onto evecs[1], normalized):", new)

print(np.dot(new, evecs[1]))
print(np.dot(A, new) - np.dot(evals[1], new))

evecs[3 ] = new

# Part D
for i in range(4):
    for j in range(i):
        if (np.dot(evecs[i], evecs[j]) < 0.0001):
            print("Eigenvectors", i, "and", j, "are orthagonal!")