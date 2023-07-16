import numpy as np
import math

# use of these two functions ought to be replaced with use of 
# the 'PLUS' function below which is far more robust; it can 
# take np.arrays, np.matrices, float, and integer inputs.
# ...but it was developed towards the end of my coding of CH 7
# and I did not feel like editing what examples/ exercises make 
# use of the following two functions.
def C_PLUS(S,X):
    if X > S:
        return 0
    if X <= S:
        return S-X
def P_PLUS(S,X):
    if S > X:
        return 0
    if S <= X:
        return X-S
    
#- - - - - - - - - - - - - - - - 
def PLUS(X):
    if isinstance(X, int) \
        or isinstance(X, np.int32)\
            or isinstance(X, float) \
                or isinstance(X, np.float64):
        #print("Input is a number")
        if X > 0:
            return X
        if X <= 0:
            return 0
    if isinstance(X, np.matrix):
        #print("Input is a matrix")
        if X.shape[0] > 1:
            print('PLUS function not set up for two dimensional matrices')
        X = np.ravel(X)
    if isinstance(X, np.ndarray):
        #print("Input is a numpy.ndarray")
        newArray = np.array([])
        for x in X:
            if x > 0:
                newArray = np.append(newArray,x)
            if x <= 0:
                newArray = np.append(newArray,0)
        return newArray
    

def EUCallBuyerProfit(S,X,C,r,T):
    gain = PLUS(S-X) - C*(math.e)**(r*T)
    return gain

def EUPutBuyerProfit(S,X,P,r,T):
    gain = PLUS(X-S) - P*(math.e)**(r*T)
    return gain

# *NOTE: 'seller' is synomous with 'writer' of the opiton
def EUCallSellerProfit(S,X,C,r,T):
    gain = C*(math.e)**(r*T) - PLUS(S-X)  
    return gain

def EUPutSellerProfit(S,X,P,r,T):
    gain = P*(math.e)**(r*T) - PLUS(X-S) 
    return gain












