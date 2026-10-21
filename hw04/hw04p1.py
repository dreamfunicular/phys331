#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:26:08 2026

@author: anna
"""

import numpy as np
import matplotlib.pyplot as plt

arr = np.loadtxt("./HW4p1data.csv", delimiter=",")

v = []
Sv = []

for each in arr:
    v = np.append(v, each[0])
    Sv = np.append(Sv, each[1])

plt.plot(v, Sv)

def L(v, ))
    (1 / np.pi) * ()

def ModelSpectrum(c1, c2, v01, v02, gamma1, gamma2, v):
    return (1 / np.pi)