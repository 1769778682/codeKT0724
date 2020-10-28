"""
1. 请求TPshop项目的登录接口，
请求数据（username: 13088888888, password: 123456, verify_code: 1234）
2. 登录接口URL：http://localhost/index.php?m=Home&c=User&a=do_login
"""

# 导包
import requests

# 发请求
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username": "13488888888",
    "password": "123456",
    "verify_code": "8888"
}
response = requests.post(url=login_url, data=login_data)

# 看响应
print(response.json())
