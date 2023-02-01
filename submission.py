# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:03:24 2023
"""

import matplotlib.pyplot as plt
import numpy as np

def normal_vector(u, v):
    normal = np.cross(u, v)
    unit = return_unit_vector(normal)
    normal = normal/unit
    return normal

def return_unit_vector(x):
    return np.sqrt(x[0]**2 + x[1]**2 + x[2]**2)

def calculate_orthogonal_project(p, n):
    projection = (np.dot(p, n)/np.dot(n, n))*n
    print(p-projection)
    return p - projection

def main():
    p = np.array([np.pi, np.e, 1])
    n = np.array([1, 0, 0])
    calculate_orthogonal_project(p, n)  
    
main()