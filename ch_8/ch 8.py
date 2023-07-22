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
#==================== EXERCISES ==============
#=============================================
# choose what exercises to run
exercise = 8.7

#--------- 8.1: EUROPEAN OPTIONS


if exercise == 8.1:
	# initialize arrays
    D0_u = np.array([]) # D0 - u variable array
    D0_d = np.array([]) # D0 - d variable array
    U    = np.array([]) # u array
    D    = np.array([]) # d array
    i = 0; u = 0 ; d = 0
    while i < 100:
        
        # u varies
        d0_u = D0_Call(20,18,u,-0.11, 0.05)
        D0_u = np.append(D0_u, d0_u)
        U    = np.append(U, u)
        
        # d varies
        d0_d = D0_Call(20,18,0.11,d, 0.05)
        D0_d = np.append(D0_d, d0_d)
        D    = np.append(D, d)
        
        u += 0.01
        d += -0.01
        i += 1

    # plot D0 w/ u variable
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(U, D0_u,'r--')
    ax1.set_title('D0: u variable')
    ax1.set_xlabel('u')

    # plot D0 w/ d variable
    # !!! NOTE: if read from left to right it seems the graph INCREASES.
    # However, being as d is negative, as d increases in MAGNITUDE (right to left)
    # we see this decreases as it ought to.
    ax2.plot(D, D0_d,'b--')
    ax2.set_title('D0: d variable')
    ax2.set_xlabel('d')

if exercise == 8.5 :
    S0 = 120 ; X = 120  ; T = 2
    u  = 0.2 ; d = -0.1 ; r = 0.1
    option = 'call'

    print(f'\n======== 8.6 (no div) ========')
    div = 0 ; t_div = -1

    print(f'option prices:')
    print('\nOption prices:')
    print(f'@ t = 0:')
    g0 = g(X,u,d,r,option,div,t_div, 0, T)  
    D0 = g0(S0) ; print(f'    D0 = {D0}')
    
    print(f'@ t = 1:')
    g1  = g(X,u,d,r,option,div,t_div, 1, T) 
    D1u   = g1(144)  ; print(f'    D1(Su) = {D1u}')
    D1d   = g1(108)  ; print(f'    D1(Sd) = {D1d}')
    
    
    print('\nReplication Strategy:')
    k   = 1
    print(f'@ t = 0:')
    Sd    = (1+d)*S0 + 0  ;  Su = (1+u)*S0 + 0
    x0,y0 = Replicate(Su,Sd,X,r, k, D1u, D1d)
    
    print(f'@ t = 1:')
    print('  up state:')
    Suu   = (1+u)*((1+u)*S0 + div)  ;  Sud = (1+d)*((1+u)*S0 + div)
    x1u,y1u = Replicate(Suu,Sud,X,r, k, PLUS(Suu-X), PLUS(Sud-X))
    print(f'    Δx = {x1u-x0}')
    print(f'    Δy = {y1u-y0*(1+r)}')
    
    print('  down state:')
    Sdd   = (1+d)*((1+d)*S0 + div)  ;  Sdu = (1+u)*((1+d)*S0 + div)
    x1d,y1d = Replicate(Sdu,Sdd,X,r, k, PLUS(Sdu-X), PLUS(Sdd-X))
    print(f'    Δx = {x1d-x0}')
    print(f'    Δy = {y1d-y0*(1+r)}')

if exercise == 8.6 :
    S0 = 120 ; X = 120  ; T = 2
    u  = 0.2 ; d = -0.1 ; r = 0.1
    option = 'call'

    print(f'\n======== 8.6 (no div) ========')
    div = -15 ; t_div = 1

    print(f'option prices:')
    print('\nOption prices:')
    print(f'@ t = 0:')
    g0 = g(X,u,d,r,option,div,t_div, 0, T)  
    D0 = g0(S0) ; print(f'    D0 = {D0}')
    
    print(f'@ t = 1:')
    g1  = g(X,u,d,r,option,div,t_div, 1, T) 
    D1u   = g1(144)  ; print(f'    D1(Su) = {D1u}')
    D1d   = g1(108)  ; print(f'    D1(Sd) = {D1d}')
    
    
    print('\nReplication Strategy:')
    k   = 1
    print(f'@ t = 0:')
    Sd    = (1+d)*S0 + 0  ;  Su = (1+u)*S0 + 0
    x0,y0 = Replicate(Su,Sd,X,r, k, D1u, D1d)
    
    print(f'@ t = 1:')
    print('  up state:')
    Suu   = (1+u)*((1+u)*S0 + div)  ;  Sud = (1+d)*((1+u)*S0 + div)
    x1u,y1u = Replicate(Suu,Sud,X,r, k, PLUS(Suu-X), PLUS(Sud-X))
    print(f'    Δx = {x1u-x0}')
    print(f'    Δy = {y1u-y0*(1+r)}')
    
    print('  down state:')
    Sdd   = (1+d)*((1+d)*S0 + div)  ;  Sdu = (1+u)*((1+d)*S0 + div)
    x1d,y1d = Replicate(Sdu,Sdd,X,r, k, PLUS(Sdu-X), PLUS(Sdd-X))
    print(f'    Δx = {x1d-x0}')
    print(f'    Δy = {y1d-y0*(1+r)}')

if exercise == 8.7 :
    S0 = 50 ; X = 60  ; T = 3
    u  = 0.3 ; d = -0.1 ; r = 0.05
    div = 0 ; t_div = -1

    print(f'call price @ t = 0:')
    option = 'call'
    g0 = g(X,u,d,r,option,div,t_div, 0, T)  
    D0 = g0(S0) ; print(f'    D0 = {D0}')

    print(f'put price @ t = 0:')
    option = 'put'
    g0 = g(X,u,d,r,option,div,t_div, 0, T)  
    D0 = g0(S0) ; print(f'    D0 = {D0}')
















