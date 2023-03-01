# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:04:28 2023
"""
#%% Uppgift 2a
import numpy as np

B = np.array([[1,2,1],[3,4,5],[2,2,1]]) #godtycklig nxn matris
b = np.array([1/np.sqrt(14), 2/np.sqrt(14), 3/np.sqrt(14)]) #En godtycklig normaliserad n-vektor

"""
    Parametrar: En n x n matris B, och en godtycklig normaliserad n-vektor b
    Returnerar: Rayleight Quotient, d.v.s b transponat * B * b
"""
def rayleigh_quotient(B, b):
    return b.T @ B @ b      # @ är matris multiplikation

print(rayleigh_quotient(B, b))

#%% Uppgift 2b
import numpy.linalg as LA

"""
    Parametrar: En n x n matris B, och en precision p
    Returnerar: Det största egenvärdet till B, och motsvarande egenvektor
"""
def power_iteration(B, p):
    b_k = np.random.rand(B.shape[1])    # En godtycklig slumpad vektor b_k
    b_k = b_k / LA.norm(b_k)            # vektorn b_k är normaliserad
    
    # Lagrar initial Rayleigh quotient i previous_quotient och den variabeln
    # lagrar "förra" Rayleigh quotient
    previous_quotient = rayleigh_quotient(B, b_k)
    
    # Relevant för den första iterationen av while-loopen,
    # varefter värdet bestäms i själva while-loopen
    rayleigh_quotient_difference = p

    while rayleigh_quotient_difference > 10**(-p):  # loopar till två på varandra följande 
                                                    # Rayleigh-kvoter i iterationen ar mindre än 10^(−p)
        b_k1 = B @ b_k
        
        b_k = b_k1 / LA.norm(b_k1) # b_k normaliseras
        
        current_quotient = rayleigh_quotient(B, b_k) # vi ankallar vår rayleigh-kvot funktion från uppgift 2a
    
        # Jamför det nya Rayleigh-kvoten med det gamla
        rayleigh_quotient_difference = abs(current_quotient - previous_quotient)
        
        # Ställer in previous_quotient som den nya Rayleigh-kvoten
        previous_quotient = current_quotient        
    
    return round(current_quotient, p), b_k

A = np.random.rand(500, 500) # En 500 x 500-matris genereras med slumpmässiga flyttal

# Vi adderar A med  A-transponat för att få en symmetrisk matris
# om matrisen inte är symmetrisk får vi imaginära egenvärden av linalg.Eig funktionen
A = A + A.T 

# Precision som är används när man jamförar skillnaden mellan
# två följande Rayleigh-kvoter så att det är mindre än 10^-p 
p = 10 

eigenValue, eigenVector = power_iteration(A, p)
print("Största egenvärdet till matrisen A enligt power_iteration():", eigenValue)
#print(eigenVector)     # Kan avkommentera om man vill kolla på vektorn

eigenValues, eigenVectors = LA.eig(A)
print("Största egenvärdet till matrisen A enligt linalg.eig():", round(np.max(eigenValues), p))
#print(eigenVectors)    # Kan avkommentera om man vill kolla på vektorn