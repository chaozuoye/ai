import numpy as np
def get_X(x):
    return np.sum(x)/np.size(x)
def get_Y(y):
    return np.mean(y)

def get_W(x,y,X,Y):
    z=0.0
    m=0.0
    for i in range(0,x.size):
        z+=(x[i]-X)*(y[i]-Y)
    for j in range(0,x.size):
        m+=pow((x[j]-X),2)
    w=z/m
    return w
def get_B(X,Y,w):
    return Y-w*X
x=np.array([64.3,99.6,145.45,63.75,
   135.46,92.85,86.97,144.76,59.3,116.03])
y=np.array([62.55,82.42,132.62,73.31,131.05,86.57
   ,85.49,127.44,55.25,104.84])

X=get_X(x)
print(X)
Y=get_Y(y)
w=get_W(x,y,X,Y)
print("W= "+str(w))

b=get_B(get_X(x),get_Y(y),w)
print("b= "+str(b))
