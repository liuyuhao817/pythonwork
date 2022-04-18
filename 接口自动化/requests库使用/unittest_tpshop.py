# 获取验证码： http://localhost/index.php?m=Home&c=User&a=verify
# 登录 ： http://localhost/index.php?m=Home&c=User&a=do_login

# 1、导包
import unittest
import requests

# 2、创建测试类
class TPShopLogin(unittest.TestCase):

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
    def test01(self):
        # 发送验证码请求并断言
        response = self.session.get(url=self.url_ver)
        self.assertEqual(200,response.status_code)
        self.assertIn("image",response.headers["Content-Type"])
        # 发送登录请求并断言
        login_data = {
            "username": "17362955793",
            "password": "123456",
            "verify_code": "8888"
        }
        response = self.session.post(url=self.url_login, data=login_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json().get("status"))
        self.assertIn("登陆成功", response.json().get("msg"))


    # 账号不存在
    def test02(self):
        # 发送验证码请求并断言
        response = self.session.get(url=self.url_ver)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录请求并断言
        login_data = {
            "username": "17362955788",
            "password": "123456",
            "verify_code": "8888"
        }
        response = self.session.post(url=self.url_login, data=login_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, response.json().get("status"))
        self.assertIn("账号不存在", response.json().get("msg"))

    # 密码错误
    def test03(self):
        # 发送验证码请求并断言
        response = self.session.get(url=self.url_ver)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers["Content-Type"])
        # 发送登录请求并断言
        login_data = {
            "username": "17362955793",
            "password": "111111",
            "verify_code": "8888"
        }
        response = self.session.post(url=self.url_login, data=login_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, response.json().get("status"))
        self.assertIn("密码错误", response.json().get("msg"))