# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:04:28 2023
"""
#%% Uppgift 2a

from sympy import Matrix
import numpy as np

B = np.array([[1,2,1],[3,4,5],[2,2,1]])
b = np.array([1/np.sqrt(14), 2/np.sqrt(14), 3/np.sqrt(14)])

#b = np.array([0.33038443, 0.86468049, 0.3783831])

def calculate_rayleigh_quotient(B, b):
    return b.T @ B @ b

print(calculate_rayleigh_quotient(B, b))

#%% Uppgift 2b

import numpy as np
import numpy.linalg as LA
import math

B = np.array([[1,2,1],[3,4,5],[2,2,1]])
p = 10


def power_iteration(B, precision: int):
    b_k = np.random.rand(B.shape[1])
    r0 = calculate_rayleigh_quotient(B, b_k)
    counter = 0

    while True:
        counter+=1
        b_k1 = np.dot(B, b_k)

        # calculate the norm
        b_k1_norm = LA.norm(b_k1)

        # re normalize the vector
        b_k = b_k1 / b_k1_norm
        
        r = calculate_rayleigh_quotient(B, b_k)
        
        if (abs(r - r0) <= 10**(-precision)):
            #print(counter)
            print(r)
            #print(r-r0)
            break
        else:
            r0 = r

    return b_k

def calculate_rayleigh_quotient(B, b):
    return b.T @ B @ b

print(power_iteration(B, p))

A = np.random.rand(500, 500)
A = A + A.T
print(power_iteration(A, p))
print(LA.eig(A))