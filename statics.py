'''
math and static fun 
'''
import numpy as np
from numpy import random as n
a = np.array([[1,2,3,4],[1,2,3,4]])
#  min value,specifi axis for the direction in case of xly array
print(np.min(a,axis=0))
b = np.array([1,2,3,4])
#cal mean of array
m = sum(b)/4
print(m)
# ANOTHER WAY OF FINDING MEAN

print(np.mean(b))
print(np.mean (b,axis=0))
#midean
c= np.array([1,2,5,9,5])
print("--------------------------------------")
print(np.median(c))

# averrage, in average we have weights that we donot have in mean
print(np.mean(c))
weight = np.array([1,2,3,4,5])
print(np.average(c, weights=weight))

#standard divations where as varaince is the squeare of standard divation

# if you donot want to use inbuild function you have to write
u = np.mean(c)
mystd = np.sqrt(np.mean(abs(c-u)**2))
print("------------------------------------")
print(mystd)

#inbuid function
dev = np.std(c)
print(dev)

# where as  in variance 
v = (mystd**2)
print(v)

print(np.var(c))