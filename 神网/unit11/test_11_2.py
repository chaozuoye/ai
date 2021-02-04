import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# 加载数据
TRAIN_URL="http://download.tensorflow.org/data/iris_training.csv"
train_path=tf.keras.utils.get_file(TRAIN_URL.split('/')[-1],TRAIN_URL)

df_iris=pd.read_csv(train_path,header=0)
# 处理数据
iris=np.array(df_iris)

train_x=iris[:,0:2]
train_y=iris[:,4]

x_train=train_x[train_y<2]
y_train=train_y[train_y<2]

num=len(x_train)
cm_pt=mpl.colors.ListedColormap(["blue","red"])
x_train=x_train-np.mean(x_train,axis=0)
x0_train=np.ones(num).reshape(-1,1)
X=tf.cast(tf.concat((x0_train,x_train),axis=1),tf.float32)
Y=tf.cast(y_train.reshape(-1,1),tf.float32)
# plt.scatter(x_train[:,0],x_train[:,1],c=y_train,cmap=cm_pt)
# plt.show()
# 设置超参数
learn_rate=0.2
iter=120
display_step=30
# 设置模型参数初始值
np.random.seed(612)
W=tf.Variable(np.random.randn(3,1),dtype=tf.float32)

# 训练模型
ce=[]
acc=[]

for i in range(0,iter+1):
    with tf.GradientTape() as tape:
        pred=1/(1+tf.exp(-tf.matmul(X,W)))
        loss=-tf.reduce_mean(Y*tf.math.log(pred)+(1-Y)*tf.math.log(1-pred))

    accuracy=tf.reduce_mean(tf.cast(tf.equal(tf.where(pred.numpy()<0.5,0.,1.),Y),tf.float32))
    ce.append(loss)
    acc.append(accuracy)
    dl_dw=tape.gradient(loss,W)
    W.assign_sub(learn_rate*dl_dw)

    if i %display_step==0:
        print("i: %f, Acc: %f,loss: %f"%(i,accuracy,loss))
# 可视化
plt.figure(figsize=(5,3))
plt.plot(ce,color="blue",label="loss")
plt.plot(acc,color="red",label="acc")
plt.legend()
plt.show()