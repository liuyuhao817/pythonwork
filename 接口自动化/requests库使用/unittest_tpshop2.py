# 获取验证码： http://localhost/index.php?m=Home&c=User&a=verify
# 登录 ： http://localhost/index.php?m=Home&c=User&a=do_login

# 1、导包
import unittest
import requests
from parameterized import parameterized
import json
# 构造测试数据
def bulid_data():
    test_data = []
    with open("./data/login.json","r",encoding="utf-8") as f:
        json_data = json.load(f)  #读取到的内容是列表嵌套字典
        for case_data in json_data:
            username = case_data.get("username")
            password = case_data.get("password")
            code = case_data.get("code")
            status_code = case_data.get("status_code")
            status = case_data.get("status")
            msg = case_data.get("msg")
            test_data.append((username, password, code, status_code,status, msg))
        return test_data

# 2、创建测试类
class TPShopLogin2(unittest.TestCase):

    # 3、创建测试方法
    def setUp(self) -> None:
        # 实例化session对象
        self.session = requests.Session()
        # 获取验证码url
        self.url_ver = "http://localhost/index.php?m=Home&c=User&a=verify"
        #获取登录url
        self.url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"

    def tearDown(self) -> None:
        # 关闭session对象
        self.session.close()

    # 登陆成功
    @parameterized.expand(bulid_data())
    def test01(self,username,password,code,status_code,status,mag):
        # 发送验证码请求并断言
        response = self.session.get(url=self.url_ver)
        self.assertEqual(200,response.status_code)
        self.assertIn("image",response.headers["Content-Type"])
        # 发送登录请求并断言
        login_data = {
            "username": username,
            "password": password,
            "verify_code": code
        }
        response = self.session.post(url=self.url_login, data=login_data)
        # print(response.json())
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(status, response.json().get("status"))
        self.assertIn(mag, response.json().get("msg"))
