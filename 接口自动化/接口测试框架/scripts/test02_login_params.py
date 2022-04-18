# 1、导包
import requests
import unittest

import json
from 接口自动化.接口测试框架.api.login import LoginAPI
from parameterized import parameterized

# 构造测试数据
def build_data():
    json_file = "../data/login.json"
    test_data = []
    with open(json_file, encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            username = case_data.get("username")
            password = case_data.get("password")
            verify_code = case_data.get("verify_code")
            status_code = case_data.get("status_code")
            content_type = case_data.get("content_type")
            status = case_data.get("status")
            msg = case_data.get("msg")
            test_data.append((username, password, verify_code, status_code,content_type, status, msg))
            print("test_data = {}".format((username, password, verify_code,status_code, content_type, status, msg)))
    return test_data

# 2.创建测试类
class TestLogin(unittest.TestCase):
    # 2.1 前置处理
    def setUp(self):
        self.login_api = LoginAPI()  # 实例化接口类
        self.session = requests.Session()  # 创建session对象

    # 2.2 后置处理
    def tearDown(self):
        if self.session:
            self.session.close()

    # 2.3.创建测试用例
    @parameterized.expand(build_data)
    def test01_login(self, username, password, verify_code, status_code,content_type, status, msg):
        # 调用验证码接口
        response = self.login_api.get_verify_code(self.session)
        # 断言
        self.assertEqual(status_code, response.status_code)
        self.assertIn(content_type, response.headers.get("Content-Type"))
        # 调用登录接口
        response = self.login_api.login(self.session, username, password,verify_code)
        print(response.json())
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(status, response.json().get("status"))
        self.assertIn(msg, response.json().get("msg"))

