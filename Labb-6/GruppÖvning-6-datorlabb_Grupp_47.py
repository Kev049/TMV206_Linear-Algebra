# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 08:26:01 2023
# Grupp 47
"""

import numpy as np
from numpy import random
import numpy.linalg as LA

#%% Uppgift 1a

"""
    Parameter: n: antal noder i en oriktad graf
    Parameter: p: sannolikheten att en nod har en kant till en annan nod (förutom sig själv)
    Returnerar: En slumpmässig n*n grannmatris
"""
def random_graph(n, p):
    grannmatris = np.zeros((n, n)) # Skapar en n*n nollmatris
    prob = p*100 # Konverterar p till procent
    
    for i in range(n):
        for j in range(i):
            x = random.randint(100) # En slumpmässigt x som används att 
            if (x < prob):          # emulera använding av sanolikhet
                grannmatris[i][j] = 1
    
    # Nu har vi byggt halva matrisen och eftersom grannmatrisen för en oriktad
    # graf alltid är symmetrisk, kan vi addera grafen med dess transponat
    grannmatris += grannmatris.T
    return grannmatris

#%% Uppgift 1b

"""
    Parameter: En n*n grannmatris M för en oriktad graf
    Returnerar: En matris med element i,j som representerar antal vägar mellan i och j av längd högst n
"""
def num_paths(M):
    matrix = M #Kopierar matris M

    for k in range(1, M[0].size+1): # Loopar n gånger (börjar med k=1)
        matrix = matrix + LA.matrix_power(M, k) # Vi lägger kontinuerligt till matris^k
    
    return matrix

#%% Uppgift 1c

# Två slumpmässiga grannmatriser (som representerar grafer)
matrix1 = random_graph(10, 0.5)
matrix2 = random_graph(100, 0.5)

path1 = num_paths(matrix1)
print("NP.max värde:", np.max(path1), "   NP.min: värde", np.min(path1))
path2 = num_paths(matrix2)
print("NP.max värde:", np.max(path2), "   NP.min: värde", np.min(path2))

#%% Uppgift 1d

"""
    Parameter: En n*n grannmatris M för en (oriktad eller riktad) graf
    Returnerar: Boolean värdet som visar om grafen är sammanhängande
"""
def is_connected(M):
    
    matrix = M # #Kopierar matris M
    # Använder följdsats 9.22 i boken
    for k in range(1, M[0].size+1):
        matrix = matrix + LA.matrix_power(M, k) # Vi lägger kontinuerligt till matris^k
        # För att eliminera risken för overflow(att elementen överskrider numpy's max) byter vi värdet
        # av varje element > 0 till 1, varje iterationen av for-loopen
        matrix = (matrix>0)*1 
    
    if np.min(matrix) > 0:
        return True
    return False

#%% Uppgift 1e

import matplotlib.pyplot as plt

"""
    Parameter: n: antal noder i en oriktad graf
    Parameter: p: sannolikheten att en nod har en kant till en annan nod
    Returnerar: Andel av grannmatris som är sammanhängande
"""
def is_connected_probability(p, n):
    was_graph_connected = 0 # En variabel som vi kommer att inkrementera i for-loopen
    num_iterations = 10
    
    for i in range(num_iterations):
        graph = random_graph(n, p)  # Generar en slumpmässig graf
        if (is_connected(graph)):   # Om det är sammanhängande
            was_graph_connected += 1    # Inkrementerar variabeln
        
    return was_graph_connected/num_iterations #Returnerar "andelen" grafer som var sammanhängande

x_axis = []
y_axis = []

# Vi använder en for-loop för att anropa is_connected_probability flera gånger
# och för att lättare samla in data
for i in range(11, 131, 20):
    x_axis.append(i)
    y_axis.append(is_connected_probability(0.1, i))
    
# Vi plottar ett linjediagram med hjälp av datan i x_axis och y_axis listor
pltfig, ax = plt.subplots()
plt.plot(x_axis, y_axis, marker="o")
plt.xlabel('n')
plt.ylabel('p')
plt.ylim(0, 1.2)
plt.show()

# Slutsats är att när n -> ∞, p -> 1 