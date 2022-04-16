import unittest

from parameterized import parameterized

from web自动化.day08.TPshop.base.get_driver import GetDriver
from web自动化.day08.TPshop.page.page_login import PageLogin
from web自动化.day08.TPshop.tools.read_json import read_json


def get_data():
    datas = read_json('login.json')
    arrs = []
    for data in datas.values():
        arrs.append((data["username"], data["password"], data["verify_code"], data["expect_result"], data["success"]))
    return arrs

class TestLogin(unittest.TestCase):

    login = None

    @classmethod
    def setUpClass(cls) -> None:

        # 实例化
        cls.login = GetDriver().get_driver()
        #初始化页面对象
        cls.Login = PageLogin(cls.login)
        #登录
        cls.login.page_click_login_link()

    @classmethod
    def tearDownClass(cls) -> None:
        #关闭浏览器
        GetDriver().quit_driver()

    @parameterized.expand(get_data())
    def test_login(self, username, password, verify_code, expect_result, success):
        #调用登录业务方法
        self.Login.page_login(username, password, verify_code)
        #断言
        if success:
            try:
                #判断安全退出是否存在
                self.assertTrue(self.login.page_is_login_success())
                #点击退出
                self.login.page_click_logout()
                try:
                    # 判断是否成功安全退出
                    self.assertTrue(self.login.page_is_logout_success())
                except Exception as e:
                    #截图
                    self.login.page_get_screenshot()
                #点击登录链接
                self.login.page_click_login_link()
            except Exception as e:
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
