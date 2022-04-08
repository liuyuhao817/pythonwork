"""
    目标：GET请求方法演练
    案例：http://www.baidu.com
    请求：1、请求方法：GET
    响应：
        2、响应对象.url #获取请求url
        3、响应对象.status_code #获取响应状态码
        4、响应对象.text  #以文本形式显示响应内容
"""
# 1、导包
import requests

# 2、调用get
url="http://www.baidu.com"
r=requests.get(url)

# 3、获取请求url
print("请求url",r.url)

# 4、获取响应状态码
print("状态码",r.status_code)

# 5、获取响应信息 文本形式
print("文本响应内容",r.text)