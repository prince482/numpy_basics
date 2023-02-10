'''
Working with numpy
'''
import numpy as np
# how to create and inetialize an array in numpy
a = np.array([1,2,3,4])
print(a)
print(type(a))
#printing the shape of array shape basically mean dimension of the array
print(a.shape)
b = np.array([1,21,2,6])
print(b)
print(type(b))
print(b.shape)
#accessing perticular value from array
#print(b[1][1])
#creating zero and ones custom array
c = np.zeros((3,3))
print(c)
d =np.ones((2,3))
print(d)
#array for some constants
e = np.full((3,2),5)
print(e)
#identify matrix - size/squeare matrix
f = np.eye(4)
print(f)
#creating random matrix
g = np.random.random((2,3))
print(g)
print(g[:,1])
#update array using slicing operations
g[1,1:3] = 1
# 1 = row, 1:3 are columns = 1 is the updated value
print(g)
#set some rows and columns and changing  data type
z = np.zeros((3,3), dtype = np.int64)
print(z)
z[1, : ] = 2
z[:, -1 ] = 72
print(z)
# -1 = before last
#Data types 
print(z.dtype)
#Mathematical operaions
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[1,2]])
#element wise addition
print(x+y)
print((np.add(x,y)))
#same goes with sub we write np.subtract, np.multipy, np divide, to take square roo we will use np.sqrt

#imp operaton matrix xly or dot product
print(x)
print(y)
print(x.dot(y))
print(np.dot(x,y))
#xly(Dot product) of two matrix will give you a scaler
p = np.array([1,2,3,4])
o = np.array([1,2,3,4])
print(p.dot(o))

#SUM function - it will give you sum of all the elelement of that perticular matrix
print(p)
print(sum(p))
#np.sum
print(np.sum(p))
# this will be used to make the sum of the perticuar row column axis = 0 mean column sum and axis = 1 mean sum of rows
print(x)

print(np.sum(x, axis=0))

#stacking function usefull in machine learning
print("------------------------------------------->")
print(a)
b=b*2
print(b)
#compining two array in single array
v = np.stack((a,b),axis=1)
print(v)

#reshaping the numpy array if you donot know the exact number of row of column then you can write -1
t = v.reshape((4,-1))
print(t)