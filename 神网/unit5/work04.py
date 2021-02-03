import numpy as np
import random
random.seed(612)
ls=np.random.rand(1000)
count=1
num=eval(input("Please enter a number:"))
if num>=1 and num<=100:
    print("{0:4}{1:6} {2:}".format("序号","索引值","随机数"))
    for i in range(1,1001):
        if i%num==0:
            print("{0:4}{1:6}   {2:}".format(count,i,ls[i-1]))
            #print(i,ls[i-1])
            count+=1
else:
    print("您输入的数字不在1-100之间")