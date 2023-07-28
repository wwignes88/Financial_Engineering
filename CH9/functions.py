import numpy as np
import math
import Complex_solve as Csolve

#===============================================
#============ BLACK SCHOLES ====================
#===============================================

from scipy.integrate import quad
π = np.pi

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
    
    
# Greek parameters for European calls/ puts
def Greeks(S,X,r,σ,T, t, option):
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
        δ = N1
        γ = (1/(S*σ*np.sqrt(2*π*T)))*np.exp(-d1**2/2)
        θ = -(S*σ/(2*np.sqrt(2*π*T)))*np.exp(-d1**2/2)\
            -r*X*np.exp(-r*T)*N2
        ν = S*np.sqrt(T/(2*π))*np.exp(-d1**2/2)
        ρ = T*X*np.exp(-r*T)*N2
        DE = A-B
        print(F'    C  = {DE}')
    if option == 'put':
        δ = -N1
        γ = (1/(S*σ*np.sqrt(2*π*T)))*np.exp(-d1**2/2)
        θ = -(S*σ/(2*np.sqrt(2*π*T)))*np.exp(-d1**2/2)\
            +r*X*np.exp(-r*T)*N2
        ν = S*np.sqrt(T/(2*π))*np.exp(-d1**2/2)
        ρ = -T*X*np.exp(-r*T)*N2
        DE = B-A
        print(F'    P  = {DE}')

    return δ, γ, θ, ν, ρ, DE




def Replicate(Su,Sd,X,r, k, v1, v2):

    # construct matrix M
    row1 = np.array([Su, (1+r)**k])
    row2 = np.array([Sd, (1+r)**k])
    M = np.vstack([row1,row2])
    M = np.matrix(M)
    
    v = np.array([v1, v2])
    v = np.matrix(v).transpose()

    # solve Mx = v @ t=1
    classification, x = Csolve.solve(M,v,1)[0:2]
    x,y = np.round(np.real(x[0]),5), np.round(np.real(x[1]),5)
    print(f'    x,y  =  {x} , {y} ')
    
    
    return x,y







# REFERENCES
# [1] "Mathematics for Finance: An Introduction to Financial Engineering",
# Marek Capinski and Tomasz Zastawniak


