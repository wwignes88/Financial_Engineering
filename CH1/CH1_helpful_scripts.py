import sys
sys.path.append('..')
from Complex_solve import *
from helpful_scripts import * 
import numpy as np


# given stock/ bond prices at t0 and two possible
# outcomes for stock prices @ t1, calculate the price
# of the option: option = 1 calculates put option price
# option = 0 calculates call option price.
def option_price(S0,S1a,S1b,A0,A1,strike, option):
    # stack possible outcomes for portfolio @ t1 in matrix form.
    M = [[S1a,A1],[S1b,A1]]
    M = np.matrix(M) # solve func. accepts matrix inputs.
    print(f'\npossible [Stock,Bond] values @ t1: \n{M}')

    if option == 1:
        # find value of call option @ t1:
        # call_diff returns zero if result if S - strike < 0.
        o1a = put_diff(S1a, strike)
        o1b = put_diff(S1b, strike) 
        option_str = 'put'
    if option == 0:
        # find value of call option @ t1:
        # call_diff returns zero if result if S - strike < 0.
        o1a = call_diff(S1a, strike)
        o1b = call_diff(S1b, strike)
        option_str = 'call'
    
    v1  = [o1a,o1b]
    v1  = np.matrix(v1).transpose() 
    
    # Now solve x in the system system Mx = v
    x = np.real(Csolve(M,v1,0)[1])
    print(f'\ncalculated weights: x = {np.round(x,3)}')
    
    # calculate value of C0
    v0 = np.array([S0,A0])
    o0 = np.sum(v0*x)
    print(f'\n{option_str} price:\nC0 = {np.round(o0,4)}\n')
    return o0



#---------------------------------------------
# exercise 1.10
# Find the wealth of investment split 50\50 between call and stock options
def split_investment(split, Capital, S0, C0, s1a, s1b, option):

    # calculate the number of stocks/ calls to purchase for a 50/50 
    # split between the two investments.
    Osplit  = 1-split  # percentage of capital invested in the call option
    nS      = split*Capital/S0    # number of stocks purchased
    nO      = Osplit*Capital/C0   # number of call options purchased
    # put the number of respective investmnets into transposed matrix form
    n = np.matrix([nS,nO]).transpose()
    
    print(f'\nn = {n}')

    # calculate put/ call option prices at t1:
    if option == 0:
        o1a = call_diff(s1a, strike) ; o1b = call_diff(s1b, strike)
    if option == 1:
        o1a = put_diff(s1a, strike)  ; o1b = put_diff(s1b, strike)
    
    # stack possible outcomes for portfolio @ t1 in matrix form.
    M = [[s1a,o1a],[s1b,o1b]] ; M = np.matrix(M) 
    print(f'\npossible [Stock,Call] values @ t1: \n{M}')
    
    
    # find value of portfolio for the two possibilities:
    # stock goes up (top row) or stock goes down (bottom row)
    v = np.matmul(M,n)
    print(f'\nvalue for 50/50 split: \n{v}')

