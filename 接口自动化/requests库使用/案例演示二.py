import requests

#1). 访问查询天气信息的接口，并获取JSON响应数据
# 2). 接口地址：http://www.weather.com.cn/data/sk/101010100.html
# response = requests.get(url="http://www.weather.com.cn/data/sk/101010100.html")
# response.encoding = "utf-8"
# print(response.json())

# 案例：解决tpshop登录验证码问题  设置cookie
"""
1. 使用requests库调用TPshop登录功能的相关接口，完成登录操作
2. 登录成功后获取‘我的订单’页面的数据
接口地址：
获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
登录用户：（username: 13088888888, password: 123456, verify_code: 1234）
登录：http://localhost/index.php?m=Home&c=User&a=do_login
我的订单：http://localhost/Home/Order/order_list.html
"""
# 获取cookie
response = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
print(response.cookies)
# 获取指定cookie
PHPSESSID = response.cookies.get("PHPSESSID")
print(PHPSESSID)

login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
        "username": "17362955793",
        "password": "123456",
        "verify_code": "8888"
}
cookie = {"PHPSESSID":PHPSESSID}
response = requests.post(url=login_url,data=login_data,cookies=cookie)
print(response.json())

# 我的订单
response = requests.get("http://localhost/Home/Order/order_list.html",cookies=cookie)
print(response.text)