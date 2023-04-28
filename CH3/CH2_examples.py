from functions import *
from random import random
import matplotlib.pyplot as plt
import numpy as np
#import docx
import datetime
import pandas as pd
import math as M

# *all exercises here pertain to plotting.
# be sure to enable plot panes in the view tab.
exercise = 3.2
example  = 0

#-------------------------- exercise 3.1
# plot binomial tree for stock movements
if exercise == 3.1:
    v = [[20]] # stock price on day 0
    # see 'plot_bin_tree' in function.py
    plot_bin_tree(v,0,3,.05,-.04)

    
#--------------------------- Example 3.2
# given stock prices, find return rates
if example == 3.2:
    S  = np.matrix('55,58,60;\
                    55,58,52;\
                    55,52,53')
    DIVIDEN = np.zeros([3,3]) 
    K = stock_to_return(S, DIVIDEN)
    print("\nK = \n",S)
    
    plt.figure()
    plot(S)
    

#------------------------------ Exercise 3.3
# given returns, find stock prices
if exercise == 3.3:
    K  = np.matrix('0.0,.10,.05 ,-.10;\
                    0.0,.05,.10 ,.10 ;\
                    0.0,.05,-.10,.10')
    dividends = np.zeros([3,4]) # no dividends here
    S0      = 45 # initial stock price.
    S       = return_to_stock(S0,K, dividends)
    print("\nStock prices: = \n",S)

    plt.figure()
    plot(S)



















