# 导包
import unittest
from selenium import webdriver

# 创建测试类 并继承
class TestLogin(unittest.TestCase):
    driver = None
    # setup初始化
    @classmethod
    def setUpClass(cls) -> None:
        # 获取driver对象
        cls.driver = webdriver.Firefox()

        # 最大化浏览器
        cls.driver.maximize_window()
        # 隐式等待
        cls.driver.implicitly_wait(30)

        # 打开URL
        cls.driver.get("http://127.0.0.1/")

        # 点击登录连接
        cls.driver.find_element_by_partial_link_text("登录").click()

    # 结束teardown
    @classmethod
    def tearDownClass(cls) -> None:
        # 关闭浏览器
        cls.driver.quit()

    # 清空操作
    def tearDown(self) -> None:
        self.driver.find_element_by_css_selector("#username").clear()
        self. driver.find_element_by_css_selector("#password").clear()
        self.driver.find_element_by_css_selector("#verify_code").clear()

    # 新建测试方法  密码错误
    def test_login_username_not_exist(self):
        driver = self.driver
        # 输入用户名
        driver.find_element_by_css_selector("#username").send_keys("17362955793")

        # 输入密码
        driver.find_element_by_css_selector("#password").send_keys("123456789")

        # 输入验证码
        driver.find_element_by_css_selector("#verify_code").send_keys("8888")

        # 点击登录按钮
        driver.find_element_by_partial_link_text("登    录").click()

        # 获取错误提示信息
        msg = driver.find_element_by_css_selector(".layui-layer-content").text

        # 断言
        try:
            self.assertEqual(msg,"密码错误!")
            # 点击确定
            driver.find_element_by_css_selector(".layui-layer-btn0").click()
        except AssertionError as e:
            # 截图
            driver.get_screenshot_as_file("../image/report.png")

    # 新建测试方法 用户名不存在
    def test_login_password_error(self):
        driver = self.driver
        # 输入用户名
        driver.find_element_by_css_selector("#username").send_keys("17300001111")

        # 输入密码
        driver.find_element_by_css_selector("#password").send_keys("123456")

        # 输入验证码
        driver.find_element_by_css_selector("#verify_code").send_keys("8888")

        # 点击登录按钮
        driver.find_element_by_partial_link_text("登    录").click()

        # 获取错误提示信息
        msg = driver.find_element_by_css_selector(".layui-layer-content").text

        # 断言
        try:
            self.assertEqual(msg, "账号不存在!")
            # 点击确定
            driver.find_element_by_css_selector(".layui-layer-btn0").click()
        except AssertionError as e:
            # 截图
            driver.get_screenshot_as_file("../image/report.png")

