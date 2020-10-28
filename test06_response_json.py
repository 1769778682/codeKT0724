# import requests
#
# # 1). 访问查询天气信息的接口，并获取JSON响应数据
# # 2). 接口地址：http://www.weather.com.cn/data/sk/101010100.html
# response = requests.get("http://www.weather.com.cn/data/sk/101010100.html")
#
# print(response.json())

"""
1. 请求IHRM项目的登录接口，请求数据（ {"mobile":"13800000002", "password":"123456"} ）
2. 登录接口URL：http://ihrm-test.itheima.net/api/sys/login
"""
# 导包
import requests

# 发送请求
login_url = "http://ihrm-test.itheima.net/api/sys/login"
login_data = {
    "mobile": "13800000002",
    "password": "123456"
}
response = requests.post(url=login_url, json=login_data)

# 查看响应
print(response.json())