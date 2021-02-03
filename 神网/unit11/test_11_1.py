#加载数据
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x=np.array([137.97,104.50,100.00,126.32,79.20,99.00,124.00,114.00,
            106.69,140.05,53.75,46.91,68.00,63.02,81.26,86.21])
y=np.array([1,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0])
print(x.size, y.size)

#数据处理
x_train=x-np.mean(x)
y_train=y
#设置超参数
learn_rate=0.005
iter=5
display_step=1
#设置模型变量初始值
np.random.seed(612)
w=tf.Variable(np.random.randn())
b=tf.Variable(np.random.randn())
x_=range(-80,80)
y_=1/(1+(tf.exp(-(w*x_+b))))
plt.scatter(x_train,y_train)
plt.plot(x_,y_,color="red",linewidth=3)
#训练模型
cross_train=[]
acc_train=[]

for i in range(0,iter+1):

    with tf.GradientTape() as tape:
        pred_train=1/(1+tf.exp(-(w*x_train+b)))
        loss_train=-tf.reduce_mean(y_train*tf.math.log(pred_train)+(1-y_train)*tf.math.log(1-pred_train))
        Accuracy_train=tf.reduce_mean(tf.cast(tf.equal(tf.where(pred_train<0.5,0,1),y_train),tf.float32))

    cross_train.append(loss_train)
    acc_train.append(Accuracy_train)

    dl_dw,dl_db=tape.gradient(loss_train,[w,b])

    w.assign_sub(learn_rate*dl_dw)
    b.assign_sub(learn_rate*dl_db)
    if i % display_step==0:
        print("i: %i, train loss: %f, Accuracy: %f"%(i,loss_train,Accuracy_train))
        y_=1/(1+tf.exp(-(w*x_+b)))
        plt.plot(x_,y_)
plt.show()


