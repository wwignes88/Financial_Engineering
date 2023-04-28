from CH1_helpful_scripts import option_price
import numpy as np


# Examples/ exercises of section 1.6


#-------------------------------------------
print('exercises 1.7, 1.8:')
# for exercise 1.7 simply change the strike price 
# to A) 90, B) 110
# for exercise 1.8 change the value of A1

# strike price of call:
strike = 100

# stock/ bond prices at t1:
S0  = 100 ; S1a = 120; S1b = 80 ;
A1  = 110 ; A0  = 100

option_price(S0,S1a,S1b,A0,A1,strike, 0) # enter 0 for call option


#---------------------------------------------
print('\n---------------\nexercises 1.9:')
A1 = 110
option_price(S0,S1a,S1b,A0,A1,strike, 1) # enter 1 for put option





