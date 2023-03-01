# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:04:28 2023
"""

import matplotlib as plt
import numpy as np

def rayleigh_quotient(M, x):
    return x.T @ M @ x


def power_iteration(A, p):
    b_k = np.random.rand(A.shape[1])
    b_k = b_k / np.linalg.norm(b_k)
    previous_quotient = rayleigh_quotient(A, b_k)
    p_check = 10

    while p_check > 10**(-p):
        
        b_k1 = A @ b_k
        
        b_k1_norm = np.linalg.norm(b_k1)

        b_k = b_k1 / b_k1_norm
        
        current_quotient = rayleigh_quotient(A, b_k)
    
        p_check = abs(current_quotient - previous_quotient)
        
        previous_quotient = current_quotient        
    
    return current_quotient