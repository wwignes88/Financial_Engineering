

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








#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def plot(M): # plots rows of arbitrary matrix along t = 0,1,2,...
    i = 0
    W = len(np.ravel(M[0,:]))
    L = len(M)
    t = np.arange(0,W,1)
    YTICK = np.array([])
    while i < L:
        plt.hlines(y = M[i,W-1],xmin = 0, xmax = np.max(t) \
                   ,color = 'r',linestyle = '--') 
        Ytick = str(np.round(M[i,W-1],2))
        YTICK = np.append(YTICK,Ytick)
        plot_row = np.ravel(M[i,:])
        plt.plot(t,plot_row)
        plt.title(str(M))
        i += 1
    plt.yticks(M[:,W-1], YTICK)

def RETURN_stock(S0,K,DIV): # convert return to stock 
    # S0 = integer
    # K  = return matrix (first column should be zeros
    # DIV = dividends matrix
    i   = 0
    DIM = K.shape
    W   = DIM[1]
    L   = DIM[0]
    S_M = S0*np.ones([L,W])
    while i < L:
        j = 1
        while j < W :
            Sm  = S_M[i,j-1]
            div = DIV[i,j]
            Sj  = Sm*(1+K[i,j]) - div
            S_M[i,j] = np.round(Sj,2)
            j   += 1
        i += 1
    return S_M

def STOCK_ret(M,DIV): # Convert stock to return 
    i = 0
    DIM = M.shape
    W   = DIM[1]
    L   = DIM[0]
    K_matrix = np.zeros([L,W])
    while i < L:
        j = 1
        K = np.array([])
        while j < W :
            Sm = M[i,j]
            Sn = M[i,j-1]
            div= DIV[i,j]
            Kj = (Sm - Sn )/Sn
            K  = np.append(K,np.round(Kj,2))
            j += 1
        K_matrix[i,1:] = K
        i += 1
    return K_matrix



###################### exercise 3.8


def logK(S,DIV): # Convert stock to return 
    i   = 0
    DIM = S.shape
    W   = DIM[1]
    L   = DIM[0]
    logK_matrix = np.zeros([L,W])
    while i < L:
        j = 1
        K = np.array([])
        while j < W :
            Sn = S[i,j]
            Sm = S[i,j-1]
            div= DIV[i,j]
            Kj = np.log((Sn + div )/Sm)
            K  = np.append(K,Kj)
            j += 1
        logK_matrix[i,1:] = K
        i += 1
    return logK_matrix

def logK_pick(S,DIV,C1,C2): # Convert stock to return 
    i   = 0
    DIM = S.shape
    W   = DIM[1]
    L   = DIM[0]
    logK_matrix = np.zeros([L,1])
    while i < L:
        K = np.array([])
        Sn = S[i,C2]
        Sm = S[i,C1]
        div= DIV[i,C2]
        Kj = np.log((Sn + div )/Sm)
        logK_matrix[i,0] = Kj
        i += 1
    return logK_matrix


################################

def E(M,P): # EXPEXTATION
    DIM = M.shape
    L = DIM[0]
    W = DIM[1]
    i = 0
    Ex = np.array([])
    while i < W:
        Mi  = np.ravel(M[:,i])
        print("Mi = ",Mi)
        Exi = np.sum(Mi*P)
        Ex  = np.append(Ex,Exi)
        i   += 1
    return Ex
        


def K_pick(S,DIV,C1,C2): # Convert stock to return 
    i   = 0
    DIM = S.shape
    W   = DIM[1]
    L   = DIM[0]
    K_matrix = np.zeros([L,1])
    while i < L:
        K = np.array([])
        Sn = S[i,C2]
        Sm = S[i,C1]
        div= DIV[i,C2]
        Kj = (Sn - Sm )/Sm
        K_matrix[i,0] = Kj
        i += 1
    return K_matrix



###########################################
########### FUNCTIONS SPECIFIC TO CH 4 ####
###########################################


    
def V_t(S,X,y,A,t,rA): # for example 4.1 - 4.2

    Pt  = np.array([])
    
    yi = y[t]
    Aj = A[t]
    Sj = np.ravel(S[:,t])
    Xj = np.ravel(X[:,t])
    pricei   = V(Xj,Sj,yi,Aj)
    
    X0 = np.ravel(X[:,0])
    S0 = np.ravel(S[:,0]) 
    receive_0 = -np.sum(X0 * S0)
    receive_j =  np.sum(X0 * Sj)
    deposit   =  abs(receive_0*rA*t)
    gain      =  receive_0 + receive_j
    close     =  deposit + gain 
    return pricei, deposit, gain, close


######################## #for exercise 4.1
def y_t(S,X,y0,A,V0):  
    DIM = S.shape
    W   = DIM[1]
    
    y_array = np.array([y0])
    VM      = np.array([V0])
    j  = 1
    Vm = V0
    while j < W:
        Xn = np.ravel(X[:,j])
        Sm = np.ravel(S[:,j-1])
        Sn = np.ravel(S[:,j])
        An = A[j]
        Am = A[j-1]
        
        yn = (Vm - np.sum(Xn*Sm))/Am
        y_array = np.append(y_array,yn)
        
        Vm = V(Xn,Sn,yn,An)
        VM = np.append(VM,Vm)
        j += 1
    return y_array, VM


############### FOR TREE ON PAGE 95 #########
def NODES(vec):
    Nsort = sorted(vec)
    i     = 0
    node  = np.array([])
    while i < len(vec):
        ni   = Nsort[i]
        loci = np.where(Nsort == ni)
        Ni   = len(np.ravel(loci))
        node = np.append(node,ni)
        i   += Ni
    return node

def Count(S):
    j   = 0
    DIM = S.shape
    W   = DIM[1]
    
    N   = 0
    while j < W-1:
        Sm = np.ravel(S[:,j])
        m_nodes = NODES(Sm)       
        N += len(m_nodes)
        j +=1
    return N

    


def equationsBIN(vars,A,S,N):
    j   = 0
    DIM = S.shape
    W   = DIM[1]
    L   = DIM[0]
    my_dict = {}
    while j < W - 1:
        Sm = np.ravel(S[:,j])
        m_nodes = NODES(Sm)
        i = 0
        while i < len(m_nodes):
            k = (2**j) + len(m_nodes)-1-i
            x = 'p' + str(k)
            my_dict[x] = vars
            i   += 1
        j += 1
    print(len(my_dict))
    j = 0
    EQN = np.array([])
    while j < W-1:
        
        Sm = np.ravel(S[:,j])
        Sn = np.ravel(S[:,j+1])
        m_nodes = NODES(Sm)
        n_nodes = NODES(Sn)
        i = 0
        while i < len(m_nodes):
            
            Am      = A[j]
            An      = A[j+1]
            Sm      = m_nodes[i]
            Snd     = n_nodes[2*i]
            Snu     = n_nodes[2*i+1]
            #print('m_nodes = ',m_nodes)
            #print('n_nodes = ',n_nodes)
            #print('Sm = ',Sm)
            #print('Su = ',Snu)
            #print('Sd = ',Snd)
            km     = (2**j)  +  len(m_nodes) -i -1
            #print('k,i,j = ',km,i,j)
            P      = my_dict['p' + str(km)]
        
            #print('k = ',km)
            print('P = ', np.round(P,2))
            pm     = P[km-1]  
            
            eqi  = pm*(Snu/An) + (1-pm)*(Snd/An) - (Sm/Am)  
            EQN  = np.append(EQN,eqi)
            
            i += 1
        #print('\n\n')
        j += 1

    return EQN
         
        
############ scrap
def equations(vars,nodes,S):
    DIM = S.shape
    W   = DIM[1]
    X = np.ravel(S[0,:])
    my_dict = {} 
    i       = 0
    while i < W:
        x = 'p' + str(i)
        my_dict[x] = vars
        i   += 1
    
    EQN = np.array([])
    i = 0
    while i < len(nodes) :
        P    = my_dict['p'+ str(i)]
        p    = P[i]
        eqi  = p**2 + p - 4#X[i]
        EQN  = np.append(EQN,eqi)
       # print("p = ",np.round(p,2))
        i   += 1
    #print("\n\n")
    return EQN

############ # Convert BIN tree to matrix
def MatBIN(p):
    LP = (len(p)+1)/2
    WP = np.log(LP)/np.log(2)
    Pm = p[0]*np.ones([1,1])
    s = 0
    while s < WP:
    
        Pn = np.zeros([2**(s+1), s+2])
        i  = 0
        while i < 2**(s):
            #print('i = ',i)
            #print('s = ',s)
        
            k     = 2**(s) + i
            pm    = p[k-1]
            pu_ind= 2*k   ; pu_val = p[pu_ind-1]
            pd_ind= 2*k+1 ; pd_val = p[pd_ind-1]
            #print('Pn = \n', Pn)
            #print('Pm = \n', Pn)
            Pn[2*i,:]   = np.append(Pm[i,:] ,pu_val )
            Pn[2*i+1,:] = np.append(Pm[i,:] ,pd_val )
            i +=  1
        Pm = Pn
        s += 1
    return Pm

def Pw(vec):
    
    p = np.array([1])
    
    
    LP = (len(p)+1)/2
    WP = np.log(LP)/np.log(2)
    Pm = p[0]*np.ones([1,1])
    s = 0
    while s < WP:
    
        Pn = np.zeros([2**(s+1), s+2])
        i  = 0
        while i < 2**(s):
            #print('i = ',i)
            #print('s = ',s)
        
            k     = 2**(s) + i
            pm    = p[k-1]
            pu_ind= 2*k   ; pu_val = p[pu_ind-1]
            pd_ind= 2*k+1 ; pd_val = p[pd_ind-1]
            #print('Pn = \n', Pn)
            #print('Pm = \n', Pn)
            Pn[2*i,:]   = np.append(Pm[i,:] ,pu_val )
            Pn[2*i+1,:] = np.append(Pm[i,:] ,pd_val )
            i +=  1
        Pm = Pn
        s += 1
    return Pm
     
def PRODUC(Mat):
    i = 0
    vec = np.array([])
    while i < len(Mat):
        prodi = M.prod(Mat[i,:])
        vec   = np.append(vec, prodi)
        i += 1
    return vec
       

def STRIKE(S,X):
    DIM = S.shape
    L   = DIM[0]
    W   = DIM[1]
    MAT = np.zeros([L,W])
    i = 0
    while i < L:
        j = 0
        while j < W:
            if S[i,j] < X:
                MAT[i,j] = 0.0
            if S[i,j] >= X:
                VAL      = S[i,j] - X
                MAT[i,j] = np.round(VAL,2)
                #print('M[i,j] =',MAT[i,j])
            j += 1
        i += 1
    return MAT

def EC(C,A,p):
    DIM = C.shape    
    L   = DIM[0]
    W   = DIM[1]
    j   = W-2
    MAT = np.zeros([L,W])
    MAT[:,W-1] = np.ravel(C[:,W-1])
    while j >= 0:
        i = 0
        cm = np.ravel(C[:,j])
        cn = np.ravel(MAT[:,j+1])
        while i < L:
            wi      = np.where(cm == cm[i])
            p_node  = p[wi]
            cn_node = cn[wi]
            a       = A[j]/A[j+1]
            b       = np.sum(p_node*cn_node)
            c       = np.sum(p_node)
            MAT[i,j]  = a*b/c
            
            #print('i,j = ',i,j)
            #print('cm = ',cm)
            #print('cn = ',cn)
            #print('where = ',wi)
            #print('cmw = ',cm[wi])
            #print('cnw = ',cn[wi])
            #print('p = ',p)
            #print('pw = ',p_node)
            #print('a = ',a)
            #print('b = ',b)
            #print('c = ',c)
            #print('Cij = ',a*b/c)
            #print('\n\n')
            
            i += 1
        j+= -1
    return np.round(MAT,2)









