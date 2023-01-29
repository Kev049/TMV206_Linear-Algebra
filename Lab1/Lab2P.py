# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:30:33 2023

@author: -
"""

import matplotlib.pyplot as plt
import numpy as np

#%% Uppgift 1

fig, ax = plt.subplots()

def l(t):
    return [t, (3*t + 2)/4]

Q = np.array([l(0), l(2)])


ax.quiver(0, 4,3,-4,angles='xy', scale_units='xy', scale=1)
ax.quiver(4, 3, -4, -3, angles='xy', scale_units='xy', scale=1, color='red')

ax.plot(Q[:,0],Q[:,1], color='green', linewidth=3)

ax.axis('equal')

#%% Uppgift 2

import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(projection='3d')

def l1(x,y):
    return 1-2*x+2*y

x=np.linspace(-1,1,10)
y=np.linspace(-1,1,10)

X,Y = np.meshgrid(x,y)
ax.plot_surface(X, Y, l1(X,Y),color='blue',alpha=0.5)

ax.view_init(15,-115)
ax.set_box_aspect((1, 1, 1))
ax.set_xticks([-1,0,1])
ax.set_yticks([-1,0,1])
ax.set_zticks([-4,-2,0,2,4])

def xt(t):
    return [-0.5+0.5*t,-1+t,t]

P=np.array([xt(0),xt(2)])
ax.plot3D(P[:,0],P[:,1],P[:,2],
color='red', linewidth=3)

ax.quiver(0, 0, 1, 2, -2, 1, color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.show()

ax.axis('equal')

#%% Uppgift 3

import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(projection='3d')

x=np.linspace(-1,1,2)
y=np.linspace(-1,1,2)

X,Y = np.meshgrid(x,y)

def l1(x,y):
    return (-0.19*x + 0.39*y + 0.032)/0.43

ax.plot_surface(X, Y, l1(X,Y),color='blue',alpha=0.5)

ax.scatter(0.1, 0.2, 0.3)
ax.scatter(0.8, 0.1, -0.1)
ax.scatter(0.9, 0.7, 0.4)

ax.axis('equal')