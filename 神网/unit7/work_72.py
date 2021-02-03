import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] ="SimHei"
mnist=tf.keras.datasets.mnist
(train_x,train_y),(test_x,test_y)=mnist.load_data()
plt.figure(figsize=(5,5))
for i in range(16):
    num=np.random.randint(1,10000)
    plt.subplot(4,4,i+1)
    plt.axis("off")
    plt.title("标签值："+str(test_y[num]),fontsize=14)
    plt.imshow(test_x[num],cmap="gray")
plt.tight_layout()
plt.suptitle("MNIST测试集样本",fontsize=14,color="red")

plt.show()