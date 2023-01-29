# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:01:05 2023

@author: Kevin
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#%% Uppgift 1
r = 4
A = np.pi * (r**2)
print(A)

#%% Uppgift 2
x = np.arange(0, 4*np.pi, 0.1)
f = x * np.sin(x)
plt.plot(x, f)


#%% Uppgift 4

# Potential error, accuracy very low
s = 0
for n in range(100):
    s+=(pow(-1,n))/(2*n+1)
round(s,7)
print(s)

#%% Uppgift 5

# Does not seem to work - likely linked to bug in Uppgift 4


import numpy as np
import matplotlib.pyplot as plt

sum = 0
i = 0

while(abs(sum*4 - np.pi) >= (0.5 * (10**-5))):
    sum += ((-1) ** i)/(2*i + 1)
    i+=1
    
print(i)
print(sum)

#%% Uppgift 6

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def min_fun(x):
    y = (x**2) - (np.cos(x))
    return y;
    
    
x = np.linspace(-1.5, 1.5)
y = min_fun(x);

plt.plot(x, y)
plt.grid('on')

z = fsolve(min_fun, -1)
plt.plot(z, min_fun(z), 'o')

z = fsolve(min_fun, 1)
plt.plot(z, min_fun(z), 'o')




















