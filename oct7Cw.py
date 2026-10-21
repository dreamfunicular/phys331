#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:48:02 2026

@author: anna
"""

import numpy as np
import matplotlib.pyplot as plt

def h(t):
    return np.cos(8 * np.pi * t)

A = np.arange(-15/4, 15/4, 1/40)

plt.plot(A, h(A), 1/40)
plt.show()

Hn = np.fft.fft(A)

print(Hn)
plt.plot(np.arange(0, 300), np.abs(Hn))
plt.show()