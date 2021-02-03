import numpy as np
import matplotlib.pyplot as plt

#加载样本数据
x=np.array([137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,
               106.69,138.05,53.75,46.91,68.00,63.02,81.26,86.21])
y=np.array([145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,
               62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30])
#设置超参数
learn_rate=0.00001
iter=1000
display_step=10
#设置模型参数初值
np.random.seed(612)
w=np.random.randn()
b=np.random.randn()
#训练模型
mse=[]
for i in range(0,iter+1):
    dl_dw=np.mean(x*(w*x+b-y))
    dl_db=np.mean(w*x+b-y)

    w=w-learn_rate*dl_dw
    b=b-learn_rate*dl_db

    pred=w*x+b
    Loss=np.mean(np.square(y-pred))/2
    mse.append(Loss)

    plt.plot(x,pred)

    if i %display_step==0:
        print("i: %i,Loss: %f,w: %f,b: %f"%(i,mse[i],w,b))
#结果可视化

plt.rcParams['font.sans-serif']=['SimHei']
plt.figure()

plt.scatter(x,y,color="red",label="销售记录")
plt.scatter(x,pred,color="blue",label="梯度下降算法")
plt.plot(x,pred,color="blue")

plt.xlabel("Area",fontsize=14)
plt.ylabel("Price",fontsize=14)

plt.legend(loc="upper left")
plt.plot(range(20,100),mse[20:100])
plt.xlabel("Iteration",fontsize=14)
plt.ylabel("Loss",fontsize=14)
plt.show()