#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:12:08 2026

@author: anna
"""

import numpy as np

# Part A
def LUdecomp(Ainput):
    n=len(Ainput)
    
    U = Ainput.copy() # make copies so as not to write over originals
    
    # MINE: Create the lower triangular matrix L as an nxn identity matrix
    L = [[]] * n
    for i in range(n):
        L[i] = [0.0] * n
        L[i][i] = 1
                
    # loop over pivot rows from row 1 to row n-1 (i to n-2)
    for i in range(0,n-1):
        # loop over row to be zero'ed from row j+1 to n (j+1 to n-1)
        for j in range(i+1,n):
            c = U[j,i]/U[i,i] # multiplicative factor to zero point
            U[j,i] = 0.0 # we know this element goes to zero
            L[j][i] += c # MINE: Set the appropriate value in L
            U[j,i+1:n]=U[j,i+1:n]-c*U[i,i+1:n] # do subtraction of two rows
    return (L, U)  # return modified A and b

# Part B
A = np.array([[4.0, -2.0, 1.0], [-3.0, -1.0, 4.0], [1.0, -1.0, 3.0]])
print(A)

L, U = LUdecomp(A)
print(np.dot(L, U))
