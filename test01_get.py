# 导包
import requests

# 发送请求
response = requests.get("http://www.baidu.com")

# 查看响应
# 查看响应数据编码格式
print("原始的数据编码为：", response.encoding)
print("设置前响应数据：", response.text)

# 设置响应数据编码格式
response.encoding = "utf-8"
print("设置编码后数据编码为：", response.encoding)
print("设置后响应数据：", response.text)