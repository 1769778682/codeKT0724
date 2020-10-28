"""
1. 请求IHRM项目的登录接口，URL： http://ihrm-test.itheima.net/api/sys/login
2. 请求头： Content-Type: application/json
3. 请求体： {"mobile":"13800000002", "password":"123456"}
"""

import requests
login_url = "http://ihrm-test.itheima.net/api/sys/login"
login_header = {
    "Content-Type": "application/json"
}
login_data ={
    "mobile": "13800000002",
    "password": "123456"
}
# 发送请求
response = requests.post(url=login_url, json=login_data, headers=login_header)

# 查看响应
print(response.json())