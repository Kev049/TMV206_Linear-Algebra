# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:13:07 2023

@author: Grupp 47
"""

#%% Uppgift 2a
from sympy import Matrix
import numpy as np

#Matris A som var definierat i uppgift 5.7 i boken
A = Matrix([[1,2,1,-1,2],[3,4,5,2,0],[2,2,1,0,2]])

x = A.rref() #Konverterar A till radreducerad trappstegsform och lagras i x

# Nu har vi redan typ löst problemet men att presentera lösningen som
# en parametrisering av planet behöver vi modifiera vördet vi får från rref().

vector_a = x[0].col(3) * -1 #Fjärde kolumn - hur motiverar man det
vector_b = x[0].col(4) * -1 #Femthe kolumn - hur motiverar man det

#Omvandlas både vektorer till listor så att dem kan skrivas ut på ett mer läsbart sätt
arr_a = vector_a.tolist();
arr_b = vector_b.tolist();

#"Lägger" vi till (1, 0) så att första vektorn blir (-1, 3/2, -1, 1, 0)
arr_a.append([1])
arr_a.append([0])

#"Lägger" vi till (0, 1) så att andra vektorn blir (0, -5/3, 4/3, 0, 1)
arr_b.append([0])
arr_b.append([1])

#Vi skriver ut det slutliga resultatet
print("x = s *", arr_a, "+ t *", arr_b)

#%% Uppgift 2b
from sympy import Matrix
import numpy as np
import time

"""
Vi försökte först generera slumpmässiga heltal men insåg att det skulle ta alldeles
för mycket tid att anropa rref på en sådan 100 x 100-matris.
På grund av detta, med hjälp från handledaren, bestämde vi oss för att använda flyttal i stället.
"""

A = np.random.rand(100, 100) #En 100 x 100-matris genereras med slumpmässiga flyttal

b = np.random.rand(100) #En 100-vektor genereras med slumpmässiga flyttal

#Vi konverterar både A och b till typ Matrix enligt uppgiften
A = Matrix((A))
b = Matrix((b))

#Vi lägger till b som en kolumn till A och spara nya värden i variabeln total_matrix
total_matrix = A.col_insert(-1, b)

t = time.time() #Sparar aktuell tid för att jämföra senare
rref_output = total_matrix.rref() #Anropar rref() på total_matrix
time_taken = time.time()-t #Beräknar hur lång tid det tog att exekvera rref()

print(time_taken) #Skriver ut hur lång tid det tog att exekvera rref()

#Vi testade program 5 gånger och time_taken var 17.81, 17.10, 17.31, 17.65, 15.71.
#Då är det medelvärdet för time_taken 17.12
#(Använde en bärbar dator med en AMD Ryzen 7 6800HS och 16 GB RAM) 

#Om man vill skriva ut returvärdet som man fick när rref anropades på total_matrix,
#kan man avkommentera raden nedan

#print(rref_output)