import numpy as np

'''
list1=[[1,1,1],[1,1,1],[1,1,1]]
arr0=np.ones((3,3))
arry1=np.array(arr0)
arry2=np.asarray(arr0)

arr0[0,0]=3

print('arr0:\n',arr0)
print('arry1:\n',arry1)
print('arry2:\n',arry2)

b=np.arange(12)
print(b)
b.resize(3,4)
a=b
print(a)
print(b)

a=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(a[0:,1:3])
'''
'''a = np.array([[1, 2, 3], [4, 5, 6]],dtype=np.int64)
print(a.shape,a.ndim,a.itemsize,a.size)

b = np.array([[7, 8, 9], [10, 11, 12]])

c=np.stack((a, b), axis=1)
d=np.arange(10)
print(d.shape)
print(d)
print(c.shape)
print(c)'''
'''m=np.array([[1,2,3], [4, 5, 6]])
n=np.array([[10,20,30],[40,50,60]])
x=np.stack((m,n),axis=0)
print(x,x.shape)
y=np.mat(m)
print(y,y.shape)'''
a = np.array([0, 1, 2, 3])

print(a)