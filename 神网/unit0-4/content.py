class File():
    def __init__(self,filename,mode):
        print("执行__init__()方法")
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        print("执行__enter__()方法")
        self.f=open(self.filename,self.mode)
        return self.f
    def __exit__(self,*args):
        print("执行__exit__()方法")
        self.f.close()
with File('mypython.txt','r') as f:
    print(f.read())