import numpy as np
import pandas as pd

print(f'\nexample [beginning of section 1.4]:\n')
# this was not a labeled example. It is between the labeled examples 1.4 and 1.5
# at the beginning of section 1.4

# enter data: columns are different investments.
# rows are for different time values, but there are 
# subcategories for different outcomes (I = stock falls
# at t1, II = stock rises at t1). Run the program and see
# the printout.
data   = np.matrix('100 80;\
                   110 60;\
                   110 100')
x = 60; y = 50  # purchase 60 bonds, 50 shares of stock.

#----------------------------------------------------
# initialize pandas row/ column headers.
rows = [np.array(["t0"   , "t1"   , "t1"    ]),
        np.array(["  -- ", "  I  ", "  II  "])]

cols  = ["A", "S"]

#------------------------------------------------------
# create price table (the cost of stocks/ bonds/ other investments, ect.)
price_tbl = pd.DataFrame(data,index=rows, columns=cols)
price_tbl = price_tbl.rename_axis( columns="t  outcome")
print(f'commodity prices: \n{price_tbl}')


#------------------------------------------------------
# create investment table (multiply colums by x,y,... - the number
# of assets purchased, respectively.)
Investments = price_tbl
Investments['A'] = Investments['A'].apply(lambda A:int(A)*x)
Investments['S'] = Investments['S'].apply(lambda S:int(S)*y)

# calculate value (add columns):
value = Investments['A'] + Investments['S']
# append as a column to data frame:
Investments['Value'] = value


#---------------------------------
# calculate value rate of return (Kv):
V  = Investments['Value'].values # convert to np.array
V0 = V[0] # initial investment value.
i  = 1 ; Kv = np.zeros(len(V))
while i < len(V):
    ki    = (V[i] - V0)/V0
    Kv[i] = np.round(ki,4)
    i += 1
Investments['Kv'] = Kv
print(f'\nInvestments: \n{Investments}')

#-------------------------------
# Find expectation / variance (σ**2) vals.
# Note: this step presumes either A) a risky asset is known to follow a probability 
# density function or B) the investor for some reason feels they have a reasonable 
# idea of what the probabilities are that stocks will rise or falle. In either case
# we are presuming probabilities have been calculated in some way.

# let p represent the probability that a stock rises. q = 1-p the probability that it 
# falls (binomial distribution). Looking at the 'Value' column tells us that the second
# row corresponds to a fall, the third to a rise. so the probability vector is 
# p = [0, q, p]
P  = np.array([0, 0.2, 0.8])
E  = np.sum(Kv*P)                 # expectation
σ  = np.sqrt(np.sum(P*(Kv-E)**2)) # standard deviation
print(f'\nExpected value    : {E}')
print(f'Standard deviation: {σ}')



















