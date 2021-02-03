import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ="SimHei"

'''tf.enable_eager_execution(
    config=None,
    device_policy=None,
    execution_mode=None
)
'''
# 加载样本数据
x1=np.array([137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00,
            106.69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26, 86.21])
x2=np.array([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2, 2])
y =np.array([145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00,
            62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69, 95.30])
#数据处理
x0=np.ones(len(x1))
X=np.stack((x0,x1,x2),axis=1)
Y=np.array(y).reshape(-1,1)
#求解模型参数
Xt=np.transpose(X)
XtX_l=np.linalg.inv(np.matmul(Xt,X))
XtX_l_Xt=np.matmul(XtX_l,Xt)
W=np.matmul(XtX_l_Xt,Y)
W=W.reshape(-1)
#预估房价
print("请输入房屋面积和房间数，预测房屋销售价格：")
while(1):
    x1_test=float(input("商品房面积："))
    if x1_test>=20 and x1_test<=500:
        x2_test=float(input("房间数："))
        if x2_test>=1 and x2_test<=10:
            y_pred=W[1]*x1_test+W[2]*x2_test+W[0]
            print("预测价格：",round(y_pred,2),"万元")
            exit(0)
        else:
            print("对不起，您的输入有误，请重新输入")
    else:
        print("对不起，您的输入有误，请重新输入")