import numpy as np
value=np.random.random()
print(value)
import numpy as np
array=np.random.random((2,2))
print(array)

array=np.random.randint(2, 10, size=(2,4))
print(array)

array=np.zeros(3)
print(array)
array=np.full(3, 5)
print(array)
array=np.eye(2)
print(array)
array=np.ones(5)
print(array)

x=np.array([[1,2],[3,4]], dtype=np.float64)
y=np.array([[5,6],[7,8]], dtype=np.float64)

A=np.add(x, y)
print(A)
A=x+y
print(A)
Z=np.subtract(x, y)
Z=x-y
a = np.array([[9, 18], [19, 10]])
print( a > 10)