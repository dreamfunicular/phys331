#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 23:42:09 2026

@author: anna
"""

# Part B
import numpy as np

def RK4integrate(F, x, y, xStop, h):    
    def run_kut4(F,x,y,h):
        K0 = h*F(x,y)
        K1 = h*F(x+h/2.0, y+K0/2.0)
        K2 = h*F(x+h/2.0, y+K1/2.0)
        K3 = h*F(x+h, y+K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + run_kut4(F,x,y,h)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X),np.array(Y)

def FCoupled(x, y):
    y1 = y[0]
    y2 = y[1]
    
    dy2 = x - 6.0 * y1 * x - (2.0 * x + 3.0) * y2
    dy1 = y2
    
    return np.array([dy1, dy2])

x0 = 0.0
y0 = np.array([1.0, 1.0])
xStop = 5.0
h = 0.01

x, y = RK4integrate(FCoupled, x0, y0, xStop, h)
