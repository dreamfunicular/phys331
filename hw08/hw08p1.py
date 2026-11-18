#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 22:45:21 2026

@author: anna
"""
import numpy as np
import matplotlib.pyplot as plt

B = 0.1
wc = 3 / 2.0 * np.pi
wa = 2 / 2.0 * np.pi

def A(t):
    return 1.0 + B * np.sin(wa * t)

def s(t):
    return A(t) * np.cos(wc * t)

x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)

plt.plot(x, s(x))
plt.axvspan(2.0 * np.pi / wc, 2 * 2.0 * np.pi / wc, 0, 0.01, color="orange")
plt.axvspan( - 2.0 * np.pi / wa, - 2 * 2.0 * np.pi / wa, 0, 0.01, color="green")
plt.axvspan(5.9, 6.0, -1 - B, 1 + B, color="pink")
plt.legend(["s(t)", "Period of carrier oscillations", "Period of amplitude modulations", "Minimum and maximum amplitude of s(t)"], loc="upper left")
plt.show()