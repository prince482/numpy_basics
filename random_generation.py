'''
numpy random module
'''
import numpy as np
from numpy import random as n
# np. arrange this is not the part of random module this will be used to generate a array in a given range
#where 10 is the final value and if we use  any number outside the bracket  this will be the starting vvalue
#diffference between rand and randn
# random number tro9 be generated in same order you have to set a seed in the begining of the random function read more about this in detail.
n.seed(1)
a = np.array([1,2,3,4])
b = np.array([1,2,3,4])
c = np.arange(10) +5 
print(c)
#shufling of array
n.shuffle(a)
print(a)
#generating random numbers
# it return value from standard normal distrubution there are varioud distribution please go through them
v = n.randn(2,3)
print(v)
# 5,10 is range and 6 is the total number you needed
g = n.randint(5,10,6)
print(g)

#random pick from one element from array

element = n.choice([1,2,3,4,56,8])
print(element)
