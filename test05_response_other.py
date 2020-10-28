import requests

# 1). 访问百度首页的接口`http://www.baidu.com`，获取以下响应数据
response = requests.get("http://www.baidu.com")

# 2). 获取响应状态码
print("响应状态码：", response.status_code)

# 3). 获取请求URL
print("URL:", response.url)

# 4). 获取响应字符编码
print("编码格式为：", response.encoding)

# 5). 获取响应头数据
print("响应头信息：", response.headers)
print("Content-Type:", response.headers.get("Content-Type"))

# 6). 获取响应的cookie数据
print("cookies:", response.cookies)
print("提取指定的cookie：", response.cookies.get("BDORZ"))

# 7). 获取文本形式的响应内容
print("文本形式显示响应内容：", response.text)

# 8). 获取字节形式的响应内容
print("获取字节形式的响应内容：", response.content)
print("获取字节形式的响应内容：", response.content.decode("utf-8"))

# 9). json查看响应结果
print(response.json())