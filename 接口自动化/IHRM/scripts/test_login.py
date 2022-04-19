# 导包
import json
import unittest

from 接口自动化.IHRM import app
from 接口自动化.IHRM.api.login import LoginApi
from parameterized import parameterized

# 构建测试数据
def build_data():
    # 指定文件路径
    json_file = "D:\python_work\接口自动化\IHRM\data\login.json"
    # 打开json文件
    test_data = []
    with open(json_file, encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            login_data = case_data.get("login_data")
            status_code = case_data.get("status_code")
            success = case_data.get("success")
            code = case_data.get("code")
            message = case_data.get("message")
            test_data.append((login_data, status_code, success, code, message))
        print("test_data = {}".format((login_data, status_code, success,code, message)))
    return test_data


# 定义测试类
class TestLogin(unittest.TestCase):

    # 前置方法
    def setUp(self) -> None:
        # 实例化接口类
        self.login = LoginApi()

    # # 后置处理
    # def tearDown(self) -> None:
    #     pass

    @parameterized.expand(build_data)
    def test01_login(self,login_data, status_code, success, code, message):
        # 调用登录
        response = self.login.login(login_data=login_data)
        # 断言
        self.assertEqual(status_code,response.status_code)
        self.assertEqual(success,response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))

        #保存token信息
        # app.TOKEN = "Bearer " + response.json().get("data")
        # app.headers_data["Authorization"] = app.TOKEN

