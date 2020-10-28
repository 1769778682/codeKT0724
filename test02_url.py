# 导包
import requests

# 发送请求
# 直接通过url传递参数
# response = requests.get(" http://localhost/Home/Goods/search.html?q=iphone")

#  通过params传递参数：
#  （1）字符串
urlA = "http://localhost/Home/Goods/search.html"
stringA = "q=iphone"
response = requests.get(url=urlA, params=stringA)

#  （2）字典
dictA = {
    "q": "iphone"
}
response = requests.get(url=urlA, params=dictA)
# 查看响应
print(response.text)