import numpy as np

a = np.arange(20).reshape(5,4)

b = np.arange(0,10,2)
print(b)
print(a[(b<3)[1]])
a = a[b<3]

print(a)