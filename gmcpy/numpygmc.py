import numpy as np
a = np.array([(1, 2), (3, 4), (5,6)])
print(a)
c = np.array([(1, 2), (3, 4), (5,6)])
c.shape #it returns (3,2) where 3 number of lines, and 2 number of columns.
b  =np.array([0,0,0,0,1,0,0,0])
print(a.shape)
print(a)
print(b)
print(a[1,:])
print(a[:, 2])
#if you dont know how many columns you have dont worry!
print(a[:,-1])