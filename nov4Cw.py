#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:42:10 2026

@author: anna
"""

import numpy as np


A = np.array([[9.0, 0.0, 2.0], [1.0, 16.0, 1.0], [0.0, -1.0, 11.0]])
b = np.array([7.0, 8.0, 1.0])

x = np.linalg.solve(A, b)

D = np.array([[9.0, 0.0, 0.0], [0.0, 16.0, 0.0], [0.0, 0.0, 11.0]])
U = np.array([[0.0, 0.0, 2.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0]])
L = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]])

Dinv = np.linalg.inv(D)

xg = np.array([1.0, 1.0, 1.0])

for i in range(10):
    xg = - np.matmul(Dinv, np.dot((L + U), xg)) + np.dot(Dinv, b)
    
A = np.array([[9.0, 10.0, 2.0], [20.0, 16.0, 1.0], [10.0, -1.0, 11.0]])

x = np.linalg.solve(A, b)
print(x)
print(np.matmul(A, x) - b)

D = np.array([[A[0][0], 0.0, 0.0], [0.0, A[1][1], 0.0], [0.0, 0.0, A[2][2]]])
U = np.array([[0.0, A[0][1], A[0][2]], [0.0, A[1][1], A[1][2]], [0.0, 0.0, 0.0]])
L = np.array([[0.0, 0.0, 0.0], [A[1][0], 0.0, 0.0], [A[2][0], A[2][1], 0.0]])

for i in range(10):
    xg = - np.matmul(Dinv, np.dot((L + U), xg)) + np.dot(Dinv, b)
    print(xg)
    
def solveJacobi(A, b, n):
    D = np.array([[A[0][0], 0.0, 0.0], [0.0, A[1][1], 0.0], [0.0, 0.0, A[2][2]]])
    U = np.array([[0.0, A[0][1], A[0][2]], [0.0, 0.0, A[1][2]], [0.0, 0.0, 0.0]])
    L = np.array([[0.0, 0.0, 0.0], [A[1][0], 0.0, 0.0], [A[2][0], A[2][1], 0.0]])
    
    Dinv = np.linalg.inv(D)
    
    xg = np.array([1.0, 1.0, 1.0])
    for i in range(n):
        xg = - np.matmul(Dinv, np.dot((L + U), xg)) + np.dot(Dinv, b)
    
    return xg

A = np.array([[9.0, 0.0, 2.0], [1.0, 6.0, 3.0], [0.0, -1.0, 2.0]])
b = np.array([7.0, 8.0, 1.0])

xg = solveJacobi(A, b, 5)
print(xg)

Ainv = np.linalg.inv(A)
x = np.dot(Ainv, b)
print(x)

print(np.linalg.norm(xg - x))

def solveJacobiWithRelaxation(A, b, n, w):
    D = np.array([[A[0][0], 0.0, 0.0], [0.0, A[1][1], 0.0], [0.0, 0.0, A[2][2]]])
    U = np.array([[0.0, A[0][1], A[0][2]], [0.0, 0.0, A[1][2]], [0.0, 0.0, 0.0]])
    L = np.array([[0.0, 0.0, 0.0], [A[1][0], 0.0, 0.0], [A[2][0], A[2][1], 0.0]])
    
    Dinv = np.linalg.inv(D)
    
    xg = np.array([1.0, 1.0, 1.0])
    for i in range(n):
        xg = w * (- np.matmul(Dinv, np.dot((L + U), xg)) + np.dot(Dinv, b)) + (1 - w) * xg
    
    return xg

xg = solveJacobiWithRelaxation(A, b, 5, 1)
print(xg)

xg = solveJacobiWithRelaxation(A, b, 5, 0.7)
print(xg)

xg = solveJacobiWithRelaxation(A, b, 5, 1.3)
print(xg)
