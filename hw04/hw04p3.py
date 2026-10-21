#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 23:39:25 2026

@author: anna
"""

def LinearSolve2(a, b, c, d, y1, y2):
    if (a * d - b * c) < 0.000001:
        print("Error! Determinant is too close to nothin'")
        return
    
    x1 = (d * y2 - b * y2) / (a * d-b * c)
    x2 = (-c * y1 + a * y2) / (a * d - b * c)
    
    return (x1, x2)

LinearSolve2(0, 0, 0, 0, 3, 5)
print(LinearSolve2(1, 2, -1, 3, 3, 5))