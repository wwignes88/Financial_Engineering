import sys
import Complex_solve as Csolve
from functions import *
import matplotlib.pyplot as plt
import numpy as np                               
import math

# *NOTES: *I use np.matrix even when it unneccessarily complicates thing
#          this helps make codes as general as possible so that they are
#          readily scaled up to more advanced applications.
#         *collapse functions by clicking the down arrow to the left
#         * (pops up with you scroll over the line number)


# choose what exercises/ examples to run
Hedging = -1
"""
0 = Delta Heding
1 = Delta-Gamma Hedging
2 = Delta-Vega Hedging
* for Delta-Rho Hedgin see exercise 9.7
"""
example  = -1
exercise = 9.7

#=============================================
#==================== HEDGING   ==============
#=============================================

# Delta heding. see pg. 194-195
if Hedging == 0:
    print('===========\nDelta hedge')
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

# Delta-Gamma Hedging see page 199
if Hedging == 1:
    print('===========\nDelta-Gamms hedge')
    t = 0; S0 = 60; σ = 0.30; r = 0.08 ; n = 1
    X1,T1 = 60, 90/365
    X2,T2 = 65, 60/365
    option = 'call'
    
    print(f'\n@ t=0:')
    # first call option
    print(f'T = 90/365, X=60:')
    δ1,γ1,θ1,ν1,ρ1,C1 = Greeks(S0,X1,r,σ,T1, t, option)
    print(f'    δ1 = {δ1}')
    print(f'    γ1 = {γ1}')
    print(f'    ν1 = {ν1}')
    
    # second call option
    print(f'T = 90/365, X=60:')
    X = 65; T = 60/365
    δ2,γ2,θ2,ν2,ρ2,C2 = Greeks(S0,X2,r,σ,T2, t, option)
    print(f'    δ2 = {δ2}')
    print(f'    γ2 = {γ2}')
    print(f'    ν2 = {ν2}')
     
    z1     = -1000 # short position in C1
    
    # solve Mx = b
    # matrix M:
    MdeltaRow = np.array([1,δ2]) 
    MgammaRow = np.array([0,γ2])
    M = np.vstack([MdeltaRow,MgammaRow])
    M = np.matrix(M)
    
    v = np.array([-δ1*z1, -γ1*z1])
    v = np.matrix(v).transpose()

    classification, x = Csolve.solve(M,v,1)[0:2]
    x,z2 = np.round(np.real(x[0]),5), np.round(np.real(x[1]),5)
    print(f'\n    x   =  {x}')
    print(f'    z2  =  {z2} ')
    
    S = 60
    y = -x*S0 - z1*C1 - z2*C2
    print(f'    y   =  {y}')
    
    
    # ----------------------------------
    print(f'\n@ t=1:')
    t=1/365
    
    print('S1=S0:')
    S = 70
    N1,N2,C1 = DE(S,X1,r,σ,T1, t, option)
    N1,N2,C2 = DE(S,X2,r,σ,T2, t, option)
    V = x*S + y*(1+r*t) + z1*C1 + z2*C2
    print(f'    V : {np.round(V,5)}')

# Delta-Vega Hedging see page 200
if Hedging == 2:
    print('===========\nDelta-Vega hedge')
    t = 0; S0 = 60; σ = 0.30; r = 0.08 ; n = 1
    X1,T1 = 60, 90/365
    X2,T2 = 65, 60/365
    option = 'call'
    
    print(f'\n@ t=0:')
    # first call option
    print(f'T = 90/365, X=60:')
    δ1,γ1,θ1,ν1,ρ1,C1 = Greeks(S0,X1,r,σ,T1, t, option)
    print(f'    δ1 = {δ1}')
    print(f'    γ1 = {γ1}')
    print(f'    ν1 = {ν1}')
    print(f'    C1 = {C1}')
    
    # second call option
    print(f'T = 90/365, X=60:')
    X = 65; T = 60/365
    δ2,γ2,θ2,ν2,ρ2,C2 = Greeks(S0,X2,r,σ,T2, t, option)
    print(f'    δ2 = {δ2}')
    print(f'    γ2 = {γ2}')
    print(f'    ν2 = {ν2}')
    print(f'    C2 = {C2}')
     
    z1     = -1000 # short position in C1
    
    # solve Mx = b
    # matrix M:
    MdeltaRow = np.array([1,δ2]) 
    MgammaRow = np.array([0,ν2])
    M = np.vstack([MdeltaRow,MgammaRow])
    M = np.matrix(M)
    
    v = np.array([-δ1*z1, -ν1*z1])
    v = np.matrix(v).transpose()

    classification, x = Csolve.solve(M,v,1)[0:2]
    x,z2 = np.round(np.real(x[0]),5), np.round(np.real(x[1]),5)
    print(f'\n    x   =  {x}')
    print(f'    z2  =  {z2} ')
    
    S = 60
    y = -x*S0 - z1*C1 - z2*C2
    print(f'    y   =  {y}')
    
    
    # ----------------------------------
    print(f'\n@ t=1:')
    t = 1/365 ; σ = 0.32
    
    print('S1=S0:')
    S = 62
    N1,N2,C1 = DE(S,X1,r,σ,T1, t, option)
    N1,N2,C2 = DE(S,X2,r,σ,T2, t, option)
    V = x*S + y*(1+r*t) + z1*C1 + z2*C2
    print(f'    V : {np.round(V,5)}')

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
    
if exercise == 9.7:
    print('===========\nDelta-Rho hedge')
    t = 0/365; S0 = 60; σ = 0.30; r = 0.08 
    X1,T1 = 60, 90/365
    X2,T2 = 65, 120/365
    option = 'call'
    
    print(f'\n@ t=0:')
    # first call option
    print(f'T = 90/365, X=60:')
    δ1,γ1,θ1,ν1,ρ1,C1 = Greeks(S0,X1,r,σ,T1, t, option)
    print(f'    δ1 = {δ1}')
    print(f'    ρ1 = {ρ1}')
    
    # second call option
    print(f'T = 120/365, X=65:')
    δ2,γ2,θ2,ν2,ρ2,C2 = Greeks(S0,X2,r,σ,T2, t, option)
    print(f'    δ2 = {δ2}')
    print(f'    ρ2 = {ρ2}')
     
    z1     = -1000 # short position in C1
    
    # solve Mx = b
    # matrix M:

    MdeltaRow = np.array([1,0,δ2]) 
    MrhoRow   = np.array([0,t,ρ2])
    MV0Row    = np.array([S0,1,C2])
    M = np.vstack([MdeltaRow,MrhoRow])
    M = np.vstack([M,MV0Row])
    M = np.matrix(M)
    
    v = np.array([-δ1*z1, -ρ1*z1, -C1*z1])
    v = np.matrix(v).transpose()

    classification, x = Csolve.solve(M,v,0)[0:2]
    X=x
    x,y,z2 = np.round(np.real(x[0]),8), \
             np.round(np.real(x[1]),8),\
             np.round(np.real(x[2]),8)
    print(f'\n    x   =  {x}')
    print(f'    y   =  {y} ')
    print(f'    z2  =  {z2} ')
    V = x*S0 + y*np.exp(r*t) + z1*C1 + z2*C2
    print(f'    V0  = {np.round(V,5)}')
    
    
    # ----------------------------------
    print(f'\n@ t=1:')
    t = 1/365 ; r = 0.9
    #T1,T2 = 89/365,119/365
    
    print('S1=S0:')
    S = 60
    N1,N2,C1 = DE(S,X1,r,σ,T1, t, option)
    N1,N2,C2 = DE(S,X2,r,σ,T2, t, option)
    V = x*S + y*np.exp(r*t) + z1*C1 + z2*C2
    print(f' !!!WRONG!!!  V  = {np.round(V,5)}')



























