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

# 创建session对象
session = requests.Session()

# 获取验证码
response = session.get("http://localhost/index.php?m=Home&c=User&a=verify")


# 登录
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username": "13488888888",
    "password": "123456",
    "verify_code": "8888"
}

response = session.post(url=login_url, data=login_data)
print(response.json())

# 我的订单：http://localhost/Home/Order/order_list.html
response = session.get("http://localhost/Home/Order/order_list.html")
print(response.text)
