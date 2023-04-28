from functions import *
from random import random
import matplotlib.pyplot as plt
import numpy as np
#import docx
import datetime
import pandas as pd
import math as M


  
##########################################
########  Define Functions  ##############
##########################################

#-------------------------------------------
# Binomial tree; c.f. exercise 3.2:
# plot binomial tree for stock prices with two possible outcomes:
    # up by up_percent or down by down_percent.
    # v is a list of a list with one single input, e.g.
    #     v = [[s0]]
    # where s0 is the known stock price today.
# returns an appended list which forms a tree:
    # [[s0], [su,sd], [suu,sud,sdu,sdd],...]
    # (terminates at step/ time n)
    
    # n is start time/ day (0 = day 1 due to python indexing). 
    # N is stop time/ day. 
    
def plot_bin_tree(v,n,N, up_percent, down_percent):
    s0 = v[0][0]
    if n == N-1:
        return 
    else:
        vn = v[n]; vm = [];  
        for s in vn:
            s_up   = s*(1+up_percent) ; 
            s_down = s*(1+down_percent)
            plt.plot([n,n+1],[s,s_up])
            plt.plot([n,n+1],[s,s_down])
            vm.append(s_up)
            vm.append(s_down)
        v.append(vm)


        return plot_bin_tree(v, n+1, N , up_percent, down_percent)
    
#----------------------------------------------
# Convert matrix of daily stock prices to daily return rates 
def stock_to_return(M,DIV): 
    i   = 0
    DIM = M.shape ; W   = DIM[1] ; L   = DIM[0]
    K   = np.zeros([L,W])
    while i < L:
        j = 1             # start at day 2
        
        while j < W :
            Sm = M[i,j]    # todays stock price
            Sn = M[i,j-1]  # yesterdays stock price
            div= DIV[i,j] # dividend payment
            Kij = (Sm - Sn + div)/Sn # rate of return
            K[i,j]  = np.round(Kij,2)
            j += 1
        i += 1
    return np.matrix(K)
 
#----------------------------------------------------
#  Given S0, convert return rates to stock prices
def return_to_stock(S0,K,DIV): 
    DIM = K.shape ; W   = DIM[1] ; L   = DIM[0]
    # S0 = integer
    # K  = return matrix (first column should be zeros
    # DIV = dividends matrix
    i   = 0
    
    S = S0*np.ones([L,W]) # initialize matrix of stock prices
    while i < L:
        j = 1 # start @ day 2
        while j < W :
            Sj_1   = S[i,j-1] # yesterdays stock price
            Sj     = Sj_1*(1+K[i,j]) - DIV[i,j]
            S[i,j] = np.round(Sj,2)
            j   += 1
        i += 1
    return np.matrix(S)






#------------------------------------------------
# plot trajectories (rows of matrix M). Equidistant x-axis intervals presumed.
# input: M, a matrix.
# also, will draw vertical lines with yticks to the y values in the last column,
# (the last days values)

def plot(M): # plots rows of arbitrary matrix along t = 0,1,2,...
    DIM = M.shape ; W   = DIM[1] ; L   = DIM[0]
    i = 0
    t = np.arange(0,W,1)
    y_ticks = np.array([])
    while i < L:
        plt.hlines(y = M[i,W-1],xmin = 0, xmax = np.max(t) \
                   ,color = 'r',linestyle = '--') 
        y_ticks  = np.append(y_ticks,M[i,W-1])
        plot_row = np.ravel(M[i,:])
        #print(f'plot_row: \n{plot_row}')
        #print(f't: \n{t}')
        plt.plot(t,plot_row)
        plt.title(str(M))
        i += 1
        
    #print(f'y_ticks: \n{y_ticks}')
    plt.yticks(y_ticks)
    




