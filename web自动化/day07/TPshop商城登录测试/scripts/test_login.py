import unittest

from web自动化.day07.TPshop商城登录测试.base.get_driver import GetDriver
from web自动化.day07.TPshop商城登录测试.page.page_login import PageLogin
from parameterized import parameterized

from web自动化.day07.TPshop商城登录测试.tools.read_json import read_json


def get_data():
    # 定义一个空列表
    datas = read_json("login.json")
    arrs = []
    for data in datas.values():
        arrs.append((data["username"], data["password"], data["verify_code"], data["expect_result"], data["success"]))
    return arrs

# 新建测试类
class TestLogin(unittest.TestCase):

    login = None
    # setup
    @classmethod
    def setUpClass(cls) -> None:
        # 获取driver
        cls.login = GetDriver().get_driver()
        # 初始化页面对象
        cls.login = PageLogin(cls.login)
        # 点击登录连接
        cls.login.page_click_login_link()

    # teardown
    @classmethod
    def tearDownClass(cls) -> None:
        # 关闭driver驱动对象
        GetDriver().quit_driver()

    # 登录测试方法
    @parameterized.expand(get_data)
    def test_login(self,username,pwd,code,expect_result,success):
        # 调用登录方法
        self.login.page_login(username,pwd,code)
        if success:
            try:
                #判断安全退出是否存在
                self.assertTrue(self.login.page_is_login_success())
                #点击退出
                self.login.page_click_logout()
                try:
                    # 判断是否成功安全退出
                    self.assertTrue(self.login.page_is_logout_success())
                except:
                    #截图
                    self.login.page_get_screenshot()
                #点击登录链接
                self.login.page_click_login_link()
            except:
                # 截图
                self.login.page_get_screenshot()
        else:
            # 获取登录提示信息
            msg = self.login.page_get_error_info()
            try:
                # 断言
                self.assertEqual(msg,expect_result)
            except AssertionError:
                # 截图
                self.login.page_get_screenshot()
            # 点击确认框
            self.login.page_click_error_btn_ok()