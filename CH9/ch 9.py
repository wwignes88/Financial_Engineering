import sys

from functions import *
import matplotlib.pyplot as plt
import numpy as np                               
import math

# *NOTES: *I use np.matrix even when it unneccessarily complicates thing
#          this helps make codes as general as possible so that they are
#          readily scaled up to more advanced applications.
#         *collapse functions by clicking the down arrow to the left
#         * (pops up with you scroll over the line number)


#=============================================
#==================== EXAMPLES  ==============
#=============================================
# choose what exercises to run
example  = 0
exercise = 9.3
#--------- 8.1: EUROPEAN OPTIONS

# see pg. 194-195
if example == 0:
    X  = 60; r = 0.08; T = 90/365 
    S0 = 60; σ = 0.30; t = 0
    option = 'call'
    
    print(f'@ t=0:')
    # call value
    Δ,N2,C0 = DE(S0,X,r,σ,T, t, option)
    print(f'    Δ = {Δ}')
    
    x,y,z = Δ, -X*np.exp(-T*r)*N2, -1
    x,y,z = 1000*np.array([x,y,z])
    print(f'\n    x = {x} [buy stock]')
    print(f'    y = {y} [borrow $]')
    print(f'    z = {z} [write/sell options] ')
    
    # portfolio value 
    V0 = x*S0 + y + z*C0
    print(f'\n    V0 : {np.round(V0,5)}')
    
    # ----------------------------------
    print(f'\n@ t=1:')
    t=1/365
    
    print('S1=S0:')
    S=S0
    N1,N2,C = DE(S,X,r,σ,T, t, option)
    V = x*S + y*(1+r*t) + z*C
    print(f'    V [w/hedge] : {np.round(V,5)}')
    # w/out hedging our original money position would have been -zC0
    # so as to make V0=0.
    U = -z*C0*(1+r*t) + z*C
    print(f'    U [w/out ]  : {np.round(U,5)}')
    
    
    print('S1=61:')
    S = 61
    N1,N2,C = DE(S,X,r,σ,T, t, option)
    V = x*S + y*(1+r*t) + z*C
    print(f'    V [w/hedge] : {np.round(V,5)}')
    U = -z*C0*(1+r*t) + z*C
    print(f'    U [w/out ]  : {np.round(U,5)}')
        
    print('S1=59:')
    #S = 62; r = 0.09 ; σ = 0.30 # see pg. 196
    N1,N2,C = DE(S,X,r,σ,T, t, option)
    V = x*S + y*(1+r*t) + z*C
    print(f'    V [w/hedge] : {np.round(V,5)}')
    U = -z*C0*(1+r*t) + z*C
    print(f'    U [w/out ]  : {np.round(U,5)}')


#=============================================
#==================== EXERCISES ==============
#=============================================


if exercise == 9.3:
    X  = 1.80; r = 0.05; T = 90/365 
    S0 = 1.82; σ = 0.14; t = 0 ; n = 50000
    option = 'put'
    
    print(f'@ t=0:')
    # call value
    Δ,N2,P0 = DE(S0,X,r,σ,T, t, option)
    print(f'    Δ = {Δ}')
    
    x,y,z = Δ, X*np.exp(-T*r)*N2, -1
    x,y,z = n*np.array([x,y,z])
    print(f'\n    x = {x} [sell stock]')
    print(f'    y = {y} [borrow]')
    print(f'    z = {z} [write/sell options] ')
    
    # portfolio value 
    V0 = x*S0 + y + z*P0
    print(f'\n    V0 : {np.round(V0,5)}')
    
    # ----------------------------------
    print(f'\n@ t=1:')
    t=1/365;
    
    print('S1=1.81:')
    S=1.81
    N1,N2,P = DE(S,X,r,σ,T, t, option)
    V = x*S + y*np.exp(r*t) + z*P
    print(f'    V [w/hedge] : {np.round(V,5)}')
    # w/out hedging our original money position would have been -z*P0
    # so as to make V0=0.
    U = -z*P0*(1+r*t) + z*P
    print(f'    U [no hedge]: {np.round(U,5)}')
    





























