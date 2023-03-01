# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

A1 = np.array([[0, 0], [0, 0.16]])
A2 = np.array([[0.85, 0.04], [-0.04, 0.85]])
A3 = np.array([[0.2, -0.26], [0.23, 0.22]])
A4 = np.array([[-0.15, 0.28], [0.26, 0.24]])

b1 = np.array([0, 0])
b2 = np.array([0, 1.6])
b3 = np.array([0, 1.6])
b4 = np.array([0, 0.44])

def f1(v):
    new_v = np.matmul(A1, v)
    r = np.add(new_v, b1)
    return r

def f2(v):
    new_v = np.matmul(A2, v)
    r = np.add(new_v, b2)
    return r

def f3(v):
    new_v = np.matmul(A3, v)
    r = np.add(new_v, b3)
    return r

def f4(v):
    new_v = np.matmul(A4, v)
    r = np.add(new_v, b4)
    return r

v = [1, 1]

for i in range(1000):
    x = np.random.randint(0, 100);
    
    if (x == 0):
        v = f1(v)
    elif (x >= 1 and x < 86):
        v = f2(v)
    elif (x >= 86 and x < 93):
        v = f3(v)
    elif (x >= 93 and x < 100):
        v = f4(v)
    
    plt.scatter(v[0], v[1], color="green")
    
plt.show()
    
    
