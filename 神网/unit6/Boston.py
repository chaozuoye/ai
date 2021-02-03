import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

boston_housing=tf.keras.datasets.boston_housing
(train_x, train_y),(_, _)=boston_housing.load_data(test_split=0)
titles=["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS"
        ,"RAD","TAX","PTRATIO","B-1000","LSTAT","MEDV"]
print("Training set:",len(train_x))
print(titles[:5])
plt.figure(figsize=(12,12))   #设置绘图尺寸
for i in range(13):
    plt.subplot(4,4,(i+1))
    plt.scatter(train_x[:,i],train_y)   #绘制散点图
    plt.xlabel(titles[i])   #设置x轴标签文本
    plt.ylabel("Price($1000's)")    #设置y轴标签文本
    plt.title(str(i+1)+"."+titles[i]+"-Price ")   #设置标题
plt.show()
