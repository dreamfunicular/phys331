#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:01:15 2026

@author: anna
"""

import numpy as np

def g1(x):
    return np.pow(3 * np.pow(x, 3) - 15 * np.pow(x, 2) - 27 * x - 5, 1/5)

def g2(x):
    return np.pow(np.pow(x, 5) + 5 * np.pow(x, 2) + 9 * x + 5 / 3, 1 / 3)

def g3(x):
    return - np.pow(x, 5) / 27 + np.pow(x, 3) / 9 - 5/9 * np.pow(x, 2) - 5/27

def dg1(x):
    return (9 * x * x - 30 * x - 27) / (5 * np.pow(3 * x * x * x - 15 * x * x - 27 * x - 5, 4/5))

def dg2(x):
    return ((5 / 3) * np.pow(x, 4) + 10 * x + 9) / (3 * np.pow((5/3) * np.pow(x, 5) + 5 * x * x + 9 * x + 5/3, 2/3))

def dg3(x):
    return (-5 / 27)