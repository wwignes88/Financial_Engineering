import sys
from helpful_scripts import *
import matplotlib.pyplot as plt
import numpy as np                               
import math

# *NOTES: *I use np.matrix even when it unneccessarily complicates thing
#          this helps make codes as general as possible so that they are
#          readily scaled up to more advanced applications.
#         *collapse functions by clicking the down arrow to the left
#         * (pops up with you scroll over the line number)

# choose what figues to plot or examples/ exercises to run
figure   = 7.4
exercise = 0
example  = 0
#===========================================
#================ FIGURES ==================
#===========================================

if figure == 7.1:
    
    # *NOTE: I consolidated both graphis in figure 7.1 into one graph.
    #        I then repeated the graphs from the seller/ writers perspective.
        
    X = 220 # strike price
    r = 0.0523 # interest rate
    T = 2/12
    C = 19.5
    S = np.matrix('150 200 250 300')
    
    
    # Option buyer profits:
    BC_Profit = EUCallBuyerProfit(S[0,0],X,C,r,T)
    BP_Profit = EUPutBuyerProfit(S[0,0],X,C,r,T)
    # *must initialize the profit matrix with a value.
    EUCallBuyerProfits = np.matrix(BC_Profit)
    EUPutBuyerProfits  = np.matrix(BP_Profit)
    
    # Option seller profits
    SC_Profit = EUCallSellerProfit(S[0,0],X,C,r,T)
    SP_Profit = EUPutSellerProfit(S[0,0],X,C,r,T)
    EUCallSellerProfits = np.matrix(SC_Profit)
    EUPutSellerProfits  = np.matrix(SP_Profit)
    
    i = 1
    while i < S.shape[1]:
        s = S[0,i] # stock price @ date i
        
        # calculate/ append option buyer profits
        BC_Profit = EUCallBuyerProfit(s,X,C,r,T)
        BP_Profit = EUPutBuyerProfit(s,X,C,r,T)
        EUCallBuyerProfits = np.append(EUCallBuyerProfits,[[BC_Profit]],axis=1)
        EUPutBuyerProfits  = np.append(EUPutBuyerProfits ,[[BP_Profit]] ,axis=1)
        
        # calculate/ append option seller profits
        SC_Profit = EUCallBuyerProfit(s,X,C,r,T)
        SP_Profit = EUPutBuyerProfit(s,X,C,r,T)
        EUCallSellerProfits = np.append(EUCallSellerProfits,[[SC_Profit]],axis=1)
        EUPutSellerProfits  = np.append(EUPutSellerProfits ,[[SP_Profit]],axis=1)
        
        i += 1
        
    # for plotting we convert to arrays using np.ravel
    StockPrices = np.ravel(S[0,:])
    EUCallBuyerProfits = np.ravel(EUCallBuyerProfits[0,:])
    EUPutBuyerProfits  = np.ravel(EUPutBuyerProfits[0,:])
    EUCallSellerProfits= np.ravel(EUCallSellerProfits[0,:])
    EUPutSellerProfits = np.ravel(EUPutSellerProfits[0,:])
    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(StockPrices, EUCallBuyerProfits,'r--',\
             StockPrices, EUPutBuyerProfits,'b--')
    ax1.set_title('BUYER Profits \n blue = put, red = call')

    ax2.plot(StockPrices, EUCallSellerProfits,'r--',\
             StockPrices, EUPutSellerProfits,'b--')
    ax2.set_title('SELLER Profits \n blue = put, red = call')


if figure == 7.4:
    
    S0 = np.arange(0,100,5)
    X  = 33
    r  = 0.05
    T  = 3/12
    
    # EU call bounds
    CallUpperBound = S0
    CallLowerBound = PLUS(S0 - X*(math.e)**(-r*T))
    
    # EU put bounds
    PutUpperBound = PLUS(-S0 + X*(math.e)**(-r*T))
    PutLowerBound = X*(math.e)**(-r*T) + S0-S0  
    # adding/ subtracting S0 in the above converted a constant float to an array.
    
    # plot call bounds
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(S0, CallLowerBound,'r--',\
             S0, CallUpperBound,'b--')
    ax1.set_title('European Call Bounds')
    ax1.set_xticks([X*(math.e)**(-r*T)])  # Set the x-axis tick locations
    ax1.set_xticklabels(['Xe^(-rT)'])  # Set the x-axis tick labels
    ax1.set_xlim(0, np.max(S0))  # Set x-axis bounds
    ax1.set_ylim(0, np.max(CallUpperBound))  # Set y-axis bounds
    #fill between lines
    ax1.fill_between(S0, CallLowerBound, CallUpperBound, color='blue', alpha=0.3)
    
    # plot put bounds
    ax2.plot(S0, PutUpperBound,'r--',\
             S0, PutLowerBound,'b--')
    ax2.set_title('European Put Bounds')
    ax2.set_xticks([X*(math.e)**(-r*T)])  # Set the x-axis tick locations
    ax2.set_xticklabels(['Xe^(-rT)'])  # Set the x-axis tick labels
    ax2.set_xlim(0, np.max(S0))  # Set x-axis bounds
    ax2.set_ylim(0, np.max(CallUpperBound))  # Set y-axis bounds
    #fill between lines
    ax2.fill_between(S0, PutLowerBound, PutUpperBound, color='blue', alpha=0.3)

#===========================================
#================ EXAMPLES =================
#===========================================


    

#===========================================
#================ EXERCISES ================
#===========================================


if exercise == 7.1:
    strike = 36
    traded = 4.5
    r      = 0.12
    months = 3
    payBack = traded*(math.e)**(r*months/12)
    
    putVal = 3
    ExerciseStock = strike - putVal - payBack
    print(f'stock price: {ExerciseStock}')

if exercise == 7.2:
    X = 90 # strike price
    r = 0.09 # interest rate
    T = 6/12
    C = 8
    S = np.matrix('87 92 97')
    
    # Option buyer profits for stock = $87:
    BC_Profit = EUCallBuyerProfit(S[0,0],X,C,r,T)
    # *must initialize the profit matrix with a value.
    EUCallBuyerProfits = np.matrix(BC_Profit)
    
    # Expetation value of profit:
    # E[S] = P1*profit1 + P2*profit2 + ...
    # for now we initialize it with P1*profit1. add other values in loop.
    ExpectedProfit = BC_Profit/3 
    i = 1
    while i < S.shape[1]:
        s = S[0,i] # stock price @ date i

        # calculate/ append option buyer profits
        BC_Profit = EUCallBuyerProfit(s,X,C,r,T)
        EUCallBuyerProfits = np.append(EUCallBuyerProfits,[[BC_Profit]],axis=1)
        
        # add to expected value
        ExpectedProfit += BC_Profit/3 
        i += 1
     
    print(f'EUCallBuyerProfits: {EUCallBuyerProfits}')
    
    print(f'Expecte Profits: {ExpectedProfit}')
    
    
    # plot profits
    # *for plotting we convert to arrays using np.ravel
    StockPrices        = np.ravel(S[0,:])
    EUCallBuyerProfits = np.ravel(EUCallBuyerProfits[0,:])
    
    fig, ax = plt.subplots()
    ax.plot(StockPrices, EUCallBuyerProfits)
    ax.set_title('EUCallBuyerProfitst')

if exercise == 7.3:
    X = 15   # strike price
    C = 2.83   # Call trading @
    r = 0.0672 # interest rate
    T = 3/12   # option exercised @ time T
    S0 = 15.6
    P = C - S0 + X*(math.e)**(-r*T)
    print(f'Put price: {P}')

if exercise == 7.4:
    X = 24   # strike price
    C = 5.09   # Call trading @
    P = 7.78   # Put trading @
    r = 0.0748 # interest rate
    T = 6/12   # option exercised @ time T
    S0 = 20.37
    left  = C-P
    right =  (S0 - X*(math.e)**(-r*T) )
    print(f'right: {right}')
    print(f'LEFT : {C-P}')
    
    if left < right:
        # @ t=0:
        # sell one share, write/sell one P, buy one call
        invest = S0 + P - C
        
        # @ t=6/12:
        # X = [exercise call if S > X, 
        #      settle put if S < X] 
        X = input(f'X = ... ')
        balance = invest*(math.e)**(r*T) + X # [positive]
        
        # X = 
    if left > right:
        # @ t=0:
        # buy one share, buy one put, sell one call
        invest = C - P - S0
        
        # @ t=6/12:
        #X =  [exercise put if S < X, 
        #      settle call if S > X] 
        X = input(f'X = ... ')
        balance = invest*(math.e)**(r*T) + X # [positive]
    
    print(f'balance = {balance}')
    
# exercise 7.5 - 7.6 very similar to 7.4

    
if exercise == 7.8:
    
    # Euro is the underlying asset.
    rUS = 0.04
    rEU = 0.03
    exchange = 0.9834 # EU to US
    T = 6/12
    F = exchange*(math.e)**((rUS-rEU)*T)
    print(f'F = {F}')

# for exercise 7.12 see figure 7.4 in 'figures' section
# modifying this graph for the dividend is trivial.

















