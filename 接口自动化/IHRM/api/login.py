#1、导包
import requests

# 定义接口类
class LoginApi():

    # 初始化
    def __init__(self):
        self.url_login = "http://ihrm-test.itheima.net/api/sys/login"

    # 登录
    def login(self,login_data):
        return requests.post(url=self.url_login,json=login_data)