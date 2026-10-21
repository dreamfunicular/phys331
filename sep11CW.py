#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:36:21 2026

@author: anna
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("DisplacementData.csv", delimiter=",")
tdata = data[:,0]
zdata = data[:,1]

plt.plot(tdata, zdata)