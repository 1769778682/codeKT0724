"""
1. 使用requests库调用TPshop登录功能的相关接口，完成登录操作
2. 登录成功后获取‘我的订单’页面的数据

接口地址：
获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
登录用户：（username: 13088888888, password: 123456, verify_code: 1234）
登录：http://localhost/index.php?m=Home&c=User&a=do_login
我的订单：http://localhost/Home/Order/order_list.html
"""

import requests

# 获取验证码
response = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
print(response.cookies)
PHPSESSID = response.cookies.get("PHPSESSID")
print(PHPSESSID)

# 登录
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username": "13488888888",
    "password": "123456",
    "verify_code": "8888"
}
cookies = {
    "PHPSESSID": PHPSESSID
}
response = requests.post(url=login_url, data=login_data, cookies=cookies)
print(response.json())

# 我的订单：http://localhost/Home/Order/order_list.html
response = requests.get("http://localhost/Home/Order/order_list.html", cookies=cookies)
print(response.text)
