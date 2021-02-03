class Person:
    def __init__(self,name,age,gender="男"):
        self.name = name
        self.age =age
        self.gender = gender
    def __del__(self):
        print("Bye bye-from",self.name)
    def printInfo(self):
        print("姓名:",self.name,"年龄：",self.age,"性别：",self.gender)

zhangsan=Person("zhangsan",18)
lisi=Person("lisi",19,"女")
zhangsan.printInfo()
lisi.printInfo()

del zhangsan
del lisi