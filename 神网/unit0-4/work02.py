def Scanner(self):
    time=3
    while time>0:
        Input=input("请输入1-100之间的整数")
        flag=1
        if Input.isalpha():
            if time==1:
                print("对不起，你已经3次输入错误，程序退出")
                exit(0)
            else:
                print("对不起，你输入的全是字母")
                flag=0
                time-=1
        elif Input.isdigit():
            n=(int)(Input)
            if n>=1 and n<=100:
                if n%1==0:
                    print("您输入的整数是：%d"%n)
                    return n
                else:
                    print("对不起，您输入的不是整数")
                    flag=0
                    time-=1
            else:
                if time ==1:
                    print("对不起，您已经3次输入错误，程序退出")
                    exit(0)
                else:
                    print("对不起，您输入的数字范围不正确")
                    flag=0
                    time-=1
        else:
            if time==1:
                print("对不起，您已经3次输入错误，程序退出")
                exit(0)
            else:
                print("对不起，您输入的是字符加数字")
                flag=0
                time-=1
