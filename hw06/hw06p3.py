#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:40:32 2026

@author: anna
"""
import numpy as np
import matplotlib.pyplot as plt

n = 10
ns = 1000

rat = np.zeros(ns)
Ca = np.zeros(ns)
nresid = np.zeros(ns)
nb = np.zeros(ns)

for i in np.arange(ns):
    A = np.random.randn(n, n)
    b = np.random.randn(n, 1)
    
    Ainv = np.linalg.inv(A)
    
    x = np.dot(Ainv, b)
    resid = np.dot(A, x) - b
    
    rat[i] = np.abs(np.linalg.det(A)) / np.linalg.norm(A)
    Ca[i] = np.abs(np.linalg.det(Ainv)) * np.linalg.det(Ainv)
    nresid[i] = np.linalg.norm(resid)


plt.loglog(Ca, rat, '.')
plt.ylabel("Ratio Det to Norm")
plt.xlabel("Condition Number")
plt.show()

plt.loglog(Ca, nresid, '.')
plt.ylabel("Norm of residual")
plt.xlabel("Condition Number")
plt.show()