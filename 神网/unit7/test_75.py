import tensorflow as tf
import matplotlib.pyplot as plt
mnist=tf.keras.datasets.mnist
(train_x,train_y),(test_x,test_y)=mnist.load_data()

print("Training set: ",len(train_x))
print("Test set:",len(test_x))

plt.imshow(train_x[3],cmap="gray")
plt.show()