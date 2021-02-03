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
while True:
    print("请选择属性：")
    print("1--CIRM\n2--ZN\n3--INDUS\n4--CHAS\n5--NOX\n6--RM\n7--AGS\n8--DIS\n9--RAD\n10-TAX\n11-PTRATIO\n12-B\n13--LSTAT")
    print("14--Exit")
    i=int(input())
    if(i==14):exit()
    #plt.subplot(4,4,(i))
    plt.scatter(train_x[:,i-1],train_y)   #绘制散点图
    plt.xlabel(titles[i-1])   #设置x轴标签文本
    plt.ylabel("Price($1000's)")    #设置y轴标签文本
    plt.title(str(i)+"."+titles[i-1]+"-Price ")   #设置标题
    plt.show()