import sys
sys.path.append('..')
from Complex_solve import *
from helpful_scripts import * 
import numpy as np
from CH1_helpful_scripts import *

# problems from section 1.7


problem = 2 # select problem

if problem == 1:
    print('exercises 1.10:')
    Capital = 1000      # initial investment capital
    C0      = 13.634    # cost of put (see section 1.6)
    strike  = 100       # strike price of call
    
    # stock prices @ t0 and possible outcomes @ t1:
    s0, s1a,s1b   = 100 , 120, 80 ; 
    split = 0.5
    split_investment(split , Capital, S0, C0, s1a, s1b, 0)

if problem == 2:
    print('exercises 1.11:')

    p   = 0.75 # probability value

    A0, A1 = 100, 110 ; r = A1/A0 # r=loan interest rate.
    s0, s1a, s1b = 100,160, 40 ; strike = 100
    c1a = call_diff(s1a,strike) ;
    c1b = call_diff(s1b,strike)
    
    # price call option @ t0/ 
    # (see 'option_price' function in CH1_helpful_scripts.py)
    c0  = option_price(s0,s1a,s1b,A0,A1,strike, 0) # enter 0 for call option
     
    # a) invest in one stock, no option
    x = 1
    
    # portfolio values @ t0, t1:
    v0  = x*s0    
    v1a = x*s1a 
    v1b = x*s1b 
    
    # rates of return
    ka  = (v1a - v0)/v0  ; kb  = (v1b - v0)/v0
    # expected return:
    E   = ka*p + kb*(1-p)    ; #print(f'\n\nE = {np.round(E,4)}')             
    # standard deviation (risk):
    s   = np.sqrt(p*(ka-E)**2 +(1-p)*(kb-E)**2) ; 
    print(f'\nrisk w/ out option:\nS = {np.round(s,4)}')


    #------------------------------------------------
    # b) invest in one stock, buy one call option
    x = 1; y = 1
    # portfolio values @ t0, t1:
    v0  = x*s0   ; 
    v1a = y*c1a - r*c0
    v1b = y*c1b - r*c0
    # rates of return:
    ka  = (v1a - v0)/v0  ; kb  = (v1b - v0)/v0
    # expected return:
    E   = ka*p + kb*(1-p)    ; #print(f'\n\nE = {np.round(E,4)}')             
    # standard deviation (risk):
    s   = np.sqrt(p*(ka-E)**2 +(1-p)*(kb-E)**2) ; 
    print(f'\nrisk w/ option:\nS = {np.round(s,4)}')












