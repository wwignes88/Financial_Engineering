
import matplotlib.pyplot as plt
import numpy as np                          
from   helpful_scripts import *
import sys

exercise = 0
example  = 4.1
    
#### Examples 4.1-4.4, exercises
S  = np.matrix('60 65 75;\
                20 15 25')  
A  = np.matrix('100 110 121')
M  = np.vstack([S,A])
T  = M.shape[1] - 1; # index of maximal time value.

# x_t = [x1_t,x2_t,y_t] 
# where xi_t is number of stock i heald @ time t. y_t is # of bonds held.
x_0 = np.matrix('20 65 5')
p = x_0.shape[1] - 1; # index of last asset
#-----------------
if example == 4.1:
    x = np.vstack([x_0,x_0])
    # portforlio values @ t = 0,1
    V0 = portfolio_value(M,x, 0) ; print(f'\nV0 = {V0}')
    V1 = portfolio_value(M,x, 1) ; print(f'V1 = {V1}')

    x_1 = np.matrix('15 94 4')
    x   = np.vstack([x,x_1])
    V2  = portfolio_value(M,x, 2) ; print(f'V2 = {V2}')

#-----------------
if example == 4.2:
    x_1 = np.matrix('18.22 -16.81 22.43;\
                    18.22 -16.81 22.43')
    V1  = portfolio_value(M,x_1,1) ; print(f'V1 = {V1}')
    

#-----------------
if example == 4.3:
    # Short 20 of stock 1
    x = np.matrix('-20 0 0;\
                   -20 0 0')
    V0  = portfolio_value(M,x,0) ; print(f'V0 = {V0} (sell [anticipate stock drop])')
    V1  = portfolio_value(M,x,1) ; print(f'V1 = {V1} (stock INCREASED)')
    profit = V1 - V0 ; print(f'profit1 = {-(V0 -V1) } [Loss]')
    
    # Short 60 of stock 2
    x = np.matrix('0 -60 0;\
                    0 -60 0')
    V0  = portfolio_value(M,x,0) ; print(f'\nV0 = {V0} (sell)')
    V1  = portfolio_value(M,x,1) ; print(f'V1 = {V1} (gain)')
    profit = V1 - V0 ; print(f'profit = {-(V0 -V1)} (profit)')

if exercise == 4.1:
    Vt  = np.matrix('200')
    xt  = np.matrix('0     0      0 ;\
                     35.24 24.18  0 ;\
                    -40.50 10.13  0') 
    y1      = y_self_finance(Vt,xt,M,A, 1) ; 
    xt[1,T] = y1
    print(f'\ny(1) = {y1}')
    V1      = portfolio_value(M,xt,1) ; 
    Vt      = np.append(Vt,[[V1]],axis = 0)
    print(f'V1   = {np.round(V1,5)}')
    
    y2      = y_self_finance(Vt,xt,M,A, 2) ; 
    xt[2,T] = y2
    print(f'\ny(2) = {y2}')
    V2      = portfolio_value(M,xt,2) ; 
    Vt      = np.append(Vt,[[V2]],axis = 0)
    print(f'V2   = {np.round(V2,5)}')  
     

