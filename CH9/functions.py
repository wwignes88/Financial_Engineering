import numpy as np
import math
import Complex_solve as Csolve

#===============================================
#============ BLACK SCHOLES ====================
#===============================================

from scipy.integrate import quad


def d(S,X,r,σ,T,t):
    DEN  = σ*np.sqrt(T-t)
    NUM1 = np.log(S/X) + (r+0.5*σ**2)*(T-t)
    NUM2 = np.log(S/X) + (r-0.5*σ**2)*(T-t)
    d1   = NUM1/DEN    ;   d2 = NUM2/DEN
    return d1,d2


def N(x): 
    pi    = np.pi
    C     = 1/(np.sqrt(2*pi))
    return C*np.exp(-0.5*(x**2)) 
 

def DE(S,X,r,σ,T, t, option):
    d1,d2 = d(S,X,r,σ,T,t)
    if option == 'call':
        N1, error = quad(N, d1-10, d1)
        N2, error = quad(N, d2-10, d2)
        
    if option == 'put':
        N1, error = quad(N, -d1-10, -d1)
        N2, error = quad(N, -d2-10, -d2) 

    A = S*N1 
    B = X*np.exp(-r*(T-t))*N2
    if option == 'call':
        print(F'    C  = {A-B}')
        Δ = N1
        return Δ,N2, A-B
    if option == 'put':
        print(F'    P  = {B-A}')
        Δ = -N1
        return Δ,N2, B-A
    
# REFERENCES
# [1] "Mathematics for Finance: An Introduction to Financial Engineering",
# Marek Capinski and Tomasz Zastawniak


