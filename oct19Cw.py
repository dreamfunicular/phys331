#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:49:22 2026

@author: anna
"""

import numpy as np
import matplotlib.pyplot as plt

def a(t, fm):
    return 1 + 0.1 * np.sin(2* np.pi * fm * t)

def s(t, fm, fc):
    return a(t, fm) * np.cos(2 * np.pi * fc * t)

dt = 0.05
Ttot = 3
fm1 = 2
fc1 = 10
tmesh = np.arange(0, Ttot, dt)
plt.plot(tmesh, s(tmesh, fm1, fc1))
plt.show()

