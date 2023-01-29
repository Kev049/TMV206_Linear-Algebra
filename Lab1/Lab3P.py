# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:13:23 2023

@author: Kevin
"""

#%% Uppgift 1

import matplotlib.pyplot as plt
import numpy as np

A = np.array([[1, 4, 7, 10],[2, 5, 8, 11],[3, 6, 9, 12]])
b = np.array([[1],[3],[5]])
c = np.array([[0, 2, 4, 6, 8]])

(m, n) = b.shape
(o, p) = c.shape

print(A.max())
print(A.min())

print(A.dtype)

#%% Uppgift 2

a = np.array([0, 2, 4])
b = np.array([1, 3, 5])
c = np.array([-1, 0, 9])

crossAns = np.cross(b, c)
crossAns = np.cross(a, crossAns)

dotAns = b * (np.dot(a,c)) - c*(np.dot(a, b))

print(crossAns)
print(dotAns)