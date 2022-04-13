# 业务层
#导包
import unittest

from parameterized import parameterized

from web自动化.day06.day06_PO模式.PO模式_v3.page.page_login import PageLogin
# 新建测试类
class TestLogin(unittest.TestCase):
    # 初始化方法
    def setUp(self) -> None:
        # 获取登录页面对象
        self.login = PageLogin()
    # 结束方法
    def tearDown(self) -> None:
    #     关闭浏览器驱动对象
        self.login.driver.quit()

    # 新建测试方法
    @parameterized.expand([("12855555555","123456","8888","账号不存在!"),("17362955793","123456789","8888","密码错误!")])
    def test_login(self,username,password,code,expect):
        # 调用测试登录方法
        self.login.page_login(username,password,code)
        # 获取登录后消息
        msg = self.login.page_get_text()
        try:
            # 断言
            self.assertEqual(msg,expect)
            # 点击确定
            self.login.page_click_err_btn_ok()
        except AssertionError as e:
            # 截图
            self.login.page_login().get_screenshot_as_file("../image/report.png")
            pass