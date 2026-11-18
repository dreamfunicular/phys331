#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:15:26 2026

@author: anna
"""

import numpy as np
import matplotlib.pyplot as plt

# A(n), B(n) return the coefficients of sine and cosine necessary for the respective terms in the Fourier transform

def A(n):
    return - (2.0 / (np.pi * np.pi * n * n)) * (np.cos(np.pi * n) - 1)

def B(n):
    return 0.0

def sawtooth(x):
    return 1 - np.abs(x) / 2.0

def funcSawtooth(nmax):
    # Set a variable for our special case of A_0
    A0 = 1
    
    # Determine mesh size based on nmax
    dt = 1.0 /(nmax * 20)
    
    # Set up our x and y categories, using A0/2 as our default value to save computational effort
    x = np.arange(-2, 2, dt)
    y = [A0 / 2] * len(x) 
    
    # Calculate the value of y(x) for each value of x by adding the appropriate multiples of sines and cosines for the first n terms in the DFT expansion
    for i in range(len(y)):
        for n in range(1, nmax):
            y[i] += A(n) * np.cos((np.pi * n) * x[i] / 2.0 ) + B(n) * np.sin((np.pi * n) * x[i] / 2.0) 
    
    plt.plot(x, y)
    plt.plot(x, sawtooth(x)) 
    plt.legend(["Fourier Transform Estimation", "Original Function"])
    plt.show()

funcSawtooth(1)
funcSawtooth(2)
funcSawtooth(3)
funcSawtooth(30)

def ModFuncSawtooth(nmax):
    # Set a variable for our special case of A_0
    A0 = 1
    
    # Determine mesh size based on nmax
    dt = 1.0 /(nmax * 20)
    
    # Set up our x and y categories, using A0/2 as our default value to save computational effort
    x = np.arange(-6, 6, dt)
    y = [A0 / 2] * len(x) 
    
    # Calculate the value of y(x) for each value of x by adding the appropriate multiples of sines and cosines for the first n terms in the DFT expansion
    for i in range(len(y)):
        for n in range(1, nmax):
            y[i] += A(n) * np.cos((np.pi * n) * x[i] / 2.0 ) + B(n) * np.sin((np.pi * n) * x[i] / 2.0) 
    
    plt.plot(x, y)
    plt.plot(x, sawtooth(x)) 
    plt.legend(["Fourier Transform Estimation", "Original Function"])
    plt.show()
    
ModFuncSawtooth(1)
ModFuncSawtooth(3)
ModFuncSawtooth(30)
