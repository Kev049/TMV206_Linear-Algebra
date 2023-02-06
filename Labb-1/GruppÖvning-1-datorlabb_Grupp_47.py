# Uppgift 2
import numpy as np

"""
    Parametrar: Två vektorer u,v i R3.
    Returnerar: En ortogonal vektor till u,v av längd 1. Normalen till
                planet som u,v spänner upp
"""
def normal_vector(u,v):
    norm = np.cross(u,v)                    #Ta fram en normalvektor
    length = np.sqrt(np.dot(norm,norm))     #Ta fram längden av normalvektorn
    return norm / length                    #Returnera den normaliserade normalvektorn

"""
    Parametrar: En punkt p och en normal n av längd 1 till ett plan.
    Returnerar: Punktens projektion på planet.
"""
def project_plane(p,n):
    d = (np.dot(n,p)) / np.sqrt(np.dot(n,n))    #Punktens avstånd till planet
    scaled_n = [n[0]*d,                         #Skalar längden av normalen n
                n[1]*d,                         #till avståndet från punkten p
                n[2]*d]                         #till planet
    return np.subtract(p,scaled_n)              #Returnerar projektionens koordinat

print(project_plane([np.pi,np.e,1],[1,0,0]))