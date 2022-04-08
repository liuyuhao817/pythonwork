"""
    目标：GET请求方法演练
    案例：
        1、http://www.baidu.com?id=1001
        2、http://www.baidu.com?id=1001,1002
        3、http://www.baidu.com?id=1001&kw=北京
    请求：请求方法：GET

    参数：params：字典或字符串（推荐使用字典）

    响应：
        2、响应对象.url #获取请求url
        3、响应对象.status_code #获取响应状态码
        4、响应对象.text  #以文本形式显示响应内容
"""
# 1、导包
import requests

# 2、调用get
url="http://www.baidu.com"
# 不推荐写法  静态
# url="http://www.baidu.com?id=101"

# 案例一 定义字典
# params={"id":1001}
# r=requests.get(url,params=params)

# 案例一 字符串形式编写 (不推荐)
# r=requests.get(url,params="id=1001")

# 案例二
# params = {"id":"1001,1002"}   #一个key 对应的value里包含几个
# r = requests.get(url,params=params)

# 案例三
params = {"id":"1001","kw":"北京"}   #多个键值对的使用
r = requests.get(url,params=params)

# 3、获取请求url
print("请求url",r.url)

# 4、获取响应状态码
print("状态码",r.status_code)

# 5、获取响应信息 文本形式
print("文本响应内容",r.text)
