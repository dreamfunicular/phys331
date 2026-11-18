#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 23:18:05 2026

@author: anna
"""

import numpy as np
import time
import matplotlib.pyplot as plt

# Non-part code
def myDFT(h):
    h = np.asarray(h, dtype=complex)
    N = len(h)
    H = [0.0] * N
    
    for n in range(N):
        for k in range(N):
            H[n] += h[k] * np.exp(-2j * np.pi * k * n / N)
    return H

# Part a
h = np.random.random(10)

mine = myDFT(h)
theirs = np.fft.fft(h)

diff = mine - theirs
print(np.linalg.norm(diff))

# Part b
def executionTime(func, N):
    runtimes = [0.0] * N
    
    for i in range(N):
        h = np.random.random(i)
        
        start = time.time()
        func(h)
        runtimes[i] = time.time() - start
    
    plt.loglog(range(N), runtimes)
    plt.show()
        
executionTime(myDFT, 100)