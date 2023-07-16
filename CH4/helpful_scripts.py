

from random import random
import matplotlib.pyplot as plt
import numpy as np
import datetime
import pandas as pd
import math as M



##########################################
########  Define Functions  ##############
##########################################
#-----------------------------------------------
# calculate value of portfolia @ time t
# M is matrix with p rows and T columns. row i is 
# asset i, columns are asset i values @ time t = 0,1,2,..
# xt is a row matrix with length p. Entries are number
# of .
def portfolio_value(M,xt, t):
    return np.matmul(xt[t,:], M[:,t])[0,0]

#----------------------------------
# self-financing strategy:
# calculate bond position y(t) - c.f. pg. 78
    # V : single column matrix of portfolio values  @ t = 1,2,...
    # xt: stock holding matrix. Rows are stocks held @ t = 1,2,...
    #     last column is bonds held.
    # M : Asset price matrix. Columns are stock prices @ t = 1,2,..
    #     bottom row is bonds values.
    # A : single column matrix of bonds held at time t @ t = 1,2,...

# note that last column of input xt should be zero; we are calculating
# this value.
def y_self_finance(V,xt,M,A, t):
    yt = (V[t-1,0]-np.matmul(xt[t,:],M[:,t-1])[0,0])/ A[0,t-1]
    return yt













