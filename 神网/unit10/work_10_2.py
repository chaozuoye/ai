import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
#加载数据
boston_housing = tf.keras.datasets.boston_housing
(train_x,train_y),(test_x,test_y)=boston_housing.load_data()

test=np.arange(12).reshape(3,4)
num_train =len(train_x)
num_test=len(test_x)
#数据处理，归一化
x_train=(train_x-train_x.min(axis=0))/(train_x.max(axis=0)-train_x.min(axis=0))
y_train=train_y

x_test=(test_x-test_x.min(axis=0))/(test_x.max(axis=0)-test_x.min(axis=0))
y_test=test_y

x0_train=np.ones(num_train).reshape(-1,1)
x0_test=np.ones(num_test).reshape(-1,1)

X_train=tf.cast(tf.concat([x0_train,x_train],axis=1),tf.float32)
X_test=tf.cast(tf.concat([x0_test,x_test],axis=1),tf.float32)

Y_train=tf.constant(y_train.reshape(-1,1),tf.float32)
Y_test=tf.constant(y_test.reshape(-1,1),tf.float32)

#设置超参数
learn_rate=0.01
iter=2000
display_step=200

#设置模型变量初始值
np.random.seed(612)
W=tf.Variable(np.random.randn(14,1),dtype=tf.float32)

mse_train=[]
mse_test=[]

for i in range(0,iter+1):
    with tf.GradientTape() as tape:
        pred_train=tf.matmul(X_train,W)
        loss_train=0.5*tf.reduce_mean(tf.square(Y_train-pred_train))

        pred_test=tf.matmul(X_test,W)
        loss_test=0.5*tf.reduce_mean(tf.square(Y_test-pred_test))

    mse_train.append(loss_train)
    mse_test.append(loss_test)

    dl_dw=tape.gradient(loss_train,W)
    W.assign_sub(learn_rate*dl_dw)

    #输出训练误差和测试误差
    if i % display_step==0:
        print("i:%i,Train Loss: %f, Test Loss: %f" % (i, loss_train, loss_test))

#可视化
plt.figure(figsize=(20,4))

plt.subplot(131)
plt.ylabel("MSE")
plt.plot(mse_test,color="blue",linewidth="3",label="train loss")
plt.plot(mse_test,color="red",linewidth="1.5",label="test loss")

plt.subplot(132)
plt.plot(y_train,color="blue",marker="o",label="true_price")
plt.plot(pred_train,color="red",marker=".",label="predict")
plt.legend()
plt.ylabel("Price")

plt.subplot(133)
plt.plot(y_test,color="blue",marker="o",label="true_price")
plt.plot(pred_test,color="red",marker=".",label="predict")
plt.legend()
plt.ylabel("price")

plt.show()