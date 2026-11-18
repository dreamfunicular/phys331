#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 23:11:16 2026

@author: anna
"""

import numpy as np
import matplotlib.pyplot as plt

# Part A

A = [[], [], [], []]
A[0] = np.random.random(4)
A[1] = np.random.random(4)
A[2] = np.random.random(4)
A[3] = np.random.random(4)

eig = np.linalg.eig(A)

evals = eig[0]
evecs = eig[1]

print("Eigenvalues:", evals)

# Part B

w1 = [evecs[0][0], evecs[1][0], evecs[2][0], evecs[3][0]]
w2 = [evecs[0][1], evecs[1][1], evecs[2][1], evecs[3][1]]
w3 = [evecs[0][2], evecs[1][2], evecs[2][2], evecs[3][2]]
w4 = [evecs[0][3], evecs[1][3], evecs[2][3], evecs[3][3]]

print("w1:", w1)
print("Aw_1:", np.matmul(A, w1))
print("lambda w_1:", np.multiply(evals[0], w1))

# Part C
P = evecs
Pinv = np.linalg.inv(P)
D = np.diag(evals)

print(np.dot(P, np.dot(D, Pinv)))
print(A)