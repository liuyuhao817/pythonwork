import unittest
from web自动化.day06.day06_PO模式.PO模式_v5_base练习.page.page_login import PageLogin
from parameterized import parameterized

def get_data():
    return [("12855555555","123456","8888","账号不存在!"),("17362955793","123456789","8888","密码错误!")]

class TestLogin(unittest.TestCase):
    login = None
    @classmethod
    def setUpClass(cls) -> None:
        # 实例化 获取页面对象
        cls.login = PageLogin()
        # 点击登录连接
        cls.login.page_click_login()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.login.driver.quit()

    @parameterized.expand(get_data())
    def test_login(self,username,password,code,expect_result):
        # 调用登录方法
        self.login.page_login(username, password, code)
        # 获取登录提示信息
        msg = self.login.page_get_error_info()
        try:
            # 断言
            self.assertEqual(msg, expect_result)
        except AssertionError:
            # 截图
            self.login.page_get_screenshot()


