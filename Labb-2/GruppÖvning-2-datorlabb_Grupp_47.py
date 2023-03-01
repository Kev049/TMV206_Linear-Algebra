# -*- coding: utf-8 -*-

# Uppgift 4

import numpy as np
import matplotlib.pyplot as plt

# De matriser och vektorer som krävs för att generera 'Barnsleys ormbunksblad' initieras

A1 = np.array([[0, 0], [0, 0.16]])
A2 = np.array([[0.85, 0.04], [-0.04, 0.85]])
A3 = np.array([[0.2, -0.26], [0.23, 0.22]])
A4 = np.array([[-0.15, 0.28], [0.26, 0.24]])

b1 = np.array([0, 0])
b2 = np.array([0, 1.6])
b3 = np.array([0, 1.6])
b4 = np.array([0, 0.44])

# De 4 avbildningar som krävs för att generera 'Barnsleys ormbunksblad' deklareras som funktioner

"""
    Parameter: En vektor v
    Returnerar: En ny vektor v_new som är lika med A1*v + b1
"""
def f1(v):
    new_v = np.matmul(A1, v)    # Multiplicerar matrisen A1 med vektorn v och lagrar resultatet i new_v
    return np.add(new_v, b1)    # Returnerar summan av new_v och vektorn b1 

"""
    Parameter: En vektor v
    Returnerar: En ny vektor v_new som är lika med A2*v + b2
"""
def f2(v):
    new_v = np.matmul(A2, v)    # Multiplicerar matrisen A1 med vektorn v och lagrar resultatet i new_v
    return np.add(new_v, b2)    # Returnerar summan av new_v och vektorn b2

"""
    Parameter: En vektor v
    Returnerar: En ny vektor v_new som är lika med A3*v + b3
"""
def f3(v):
    new_v = np.matmul(A3, v)    # Multiplicerar matrisen A1 med vektorn v och lagrar resultatet i new_v
    return np.add(new_v, b3)    # Returnerar summan av new_v och vektorn b3

"""
    Parameter: En vektor v
    Returnerar: En ny vektor v_new som är lika med A4*v + b4
"""
def f4(v):
    new_v = np.matmul(A4, v)    # Multiplicerar matrisen A1 med vektorn v och lagrar resultatet i new_v
    return np.add(new_v, b4)    # Returnerar summan av new_v och vektorn b4
    
# En godtyckligt vektor v_0 initieras för att börja rekursivt definiera nya vektorer
v = [1, 1]

for i in range(1000):
    x = np.random.randint(0, 100);  # En (pseudo) slumpmässigt x mellan från 0-99 väljs

    # Värdet av x används för att bestämma hur v ändras (dvs vilken funktion som används)

    if (x == 0):                    # 1% chans att denna funktion anropas
        v = f1(v)
    elif (x >= 1 and x < 86):       # 85% chans att denna funktion anropas
        v = f2(v)
    elif (x >= 86 and x < 93):      # 7% chans att denna funktion anropas
        v = f3(v)
    elif (x >= 93 and x < 100):     # 7% chans att denna funktion anropas
        v = f4(v)

    # Punkten som definieras av koordinaterna lagrade i variabeln v plottas
    plt.scatter(v[0], v[1], color="green")

plt.show()