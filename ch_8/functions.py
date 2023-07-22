import numpy as np
import math
import Complex_solve as Csolve

    
#- - - - - - - - - - - - - - - - 
# returns max{0, X}
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


#---------------------
# used for exercise 8.1
def D0_Call(S0,X,u,d, r):
    Su = (1+u)*S0 ; Sd = (1+d)*S0
    A = (PLUS(Su-X) - PLUS(Sd-X))/(u-d)
    B = (1+d)*PLUS(Su-X) - (1+u)*PLUS(Sd-X)
    C = (u-d)*(1+r)
    return A + B/C


#----------- Replicate option by solving Mx = v
#            where 
#               M =  [[Su, (1+r)],
#                     [Sd, (1+r)]]
# and 
#               v = [v1,
#                    v2]

# in some cases v1,v2 will be the option payoff, but in a binomial tree
# for nodes less than t=T-2 or less v1,v2 will be the option prices @ t+1.
# so it is best to just leave v1,v2 as arbitrary inputs to be specified by
# the user.
def Replicate(Su,Sd,X,r, k, v1, v2):

    # construct matrix M
    row1 = np.array([Su, (1+r)**k])
    row2 = np.array([Sd, (1+r)**k])
    M = np.vstack([row1,row2])
    M = np.matrix(M)
    
    v = np.array([v1, v2])
    v = np.matrix(v).transpose()

    # solve Mx = v @ t=1
    classification, x = Csolve.solve(M,v,1)[0:2]
    x,y = np.round(np.real(x[0]),5), np.round(np.real(x[1]),5)
    print(f'    x,y  =  {x} , {y} ')
    
    
    return x,y


#------------------- Derivative pricing in Binomial tree model
# 'g' function is used to define functions that calculate a derivative
# price from a specified time t0. See pgs 178-179 of ref [1].
# This method is more complex but is more flexible than using equation 8.4
# in that it allows dividend prices to be paid at specified times, and
# were we interested we could even make more specifice modifications 
# like payoffs which are specific to an up or down state at a given time
# in the binomial tree.  


def generateFunc(X,u,d,r,t_div,div,  t,g):
    p = (r-d)/(u-d)
    def dynamic_function(S):
        if t == t_div:
            S += div; print(f'\ndiv @ t = {t}')
        Su = (1+u)*S ; Sd = (1+d)*S
        return (p*g(Su) + (1-p)*g(Sd))/(1+r)
    return dynamic_function


def g(X,u,d,r,option,div,t_div, t0,T):
    p = (r-d)/(u-d) # risk-neutral probability  
    t = T-1
    def gt(S):
        if t_div == T-1:
            S += div
        Su = (1+u)*S ; Sd = (1+d)*S
        if option == 'call':
            g = (p*PLUS(Su-X) + (1-p)*PLUS(Sd-X))
        if option == 'put':
            g = (p*PLUS(X-Su) + (1-p)*PLUS(X-Sd))
        return g/(1+r)
    globals()[f'g{t}'] = gt
    
    t -= 1
    while t >= t0:
        gt1 = globals()[f'g{t+1}']
        gt  = generateFunc(X,u,d,r,t_div,div,  t,gt1)
        globals()[f'g{t}'] = gt
        t -= 1
    g = globals()[f'g{t0}']
    return g
        






# REFERENCES
# [1] "Mathematics for Finance: An Introduction to Financial Engineering",
# Marek Capinski and Tomasz Zastawniak


