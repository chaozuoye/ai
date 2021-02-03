import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x1=np.array([137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,
               106.69,138.05,53.75,46.91,68.00,63.02,81.26,86.21])
x2=np.array([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2])
y=np.array([145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,
               62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30])

x0=np.ones(len(x1))

X=np.stack((x0,x1,x2),axis=1)
Y=np.array(y).reshape(-1,1)

Xt=np.transpose(X)
XtX_l=np.linalg.inv(np.matmul(Xt,X))
XtX_l_Xt=np.matmul(XtX_l,Xt)
W=np.matmul(XtX_l_Xt,Y)     #w=(XtX)^(-1)XtY
W=W.reshape(-1)
print("多元回归方程:")
print("Y=",W[1],"*x1+",W[2],"*x2+",W[0])

print("请输入房屋面积和房间数，预测房屋销售价格：")
x1_test=float(input("商品房面积："))
x2_test=int(input("房间数："))
y_pred=W[1]*x1_test+W[2]*x2_test+W[0]
print("预测价格：",round(y_pred,2),"万元")

fig=plt.figure(figsize=(8,6))
ax3d=Axes3D(fig)
ax3d.scatter(x1,x2,y,color="b",marker="*")

ax3d.set_xlabel('Area',color='r',fontsize=16)
ax3d.set_ylabel('Room',color='r',fontsize=16)
ax3d.set_zlabel('Price',color='r',fontsize=16)
ax3d.set_yticks([1,2,3])
ax3d.set_zlim3d(30,160)
plt.show()