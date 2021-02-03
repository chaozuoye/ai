import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] =['SimHei']

x=tf.constant([137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,
               106.69,138.05,53.75,46.91,68.00,63.02,81.26,86.21])
y=tf.constant([145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,
               62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30])

meanX=tf.reduce_mean(x)
meanY=tf.reduce_mean(y)

sumXY=tf.reduce_sum((x-meanX)*(y-meanY))
sumX=tf.reduce_sum((x-meanX)*(x-meanX))

w=sumXY/sumX
b=meanY-w*meanX

print("权值w=",w.numpy(),"\n偏置值b=",b.numpy())
print("线性模型：y=",w.numpy(),"*x+",b.numpy())

x_test=np.array([128.15,45.00,141.43,106.27,99.00,53.84,85.36,70.00])
y_pred=(w*x_test+b).numpy()

print("面积\t估计房价")
n=len(x_test)
for i in range(n):
    print(x_test[i],"\t",round(y_pred[i],2))

plt.figure()
plt.scatter(x,y,color="red",label="销售记录")
plt.scatter(x_test,y_pred,color="blue",label="预测房价")
plt.plot(x_test,y_pred,color="green",label="拟合直线",linewidth=2)

plt.xlabel("面积（平方米）",fontsize=20)

plt.legend(loc="upper left")
plt.show()
