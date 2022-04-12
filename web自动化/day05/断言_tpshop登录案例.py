"""
需求：使用UnitTest框架对tpshop项目测试
1). 点击登录，进入登录页面
2). 输入用户名和密码，不输入验证码，直接点击登录按钮
3). 获取错误提示信息
4). 断言错误提示信息是否为“验证码不能为空!”，如果断言失败则保存截图
扩展：
1. 图片名称为动态-时间
"""
import time
import unittest
from selenium import webdriver
class TestLogin(unittest.TestCase):
    def setUp(self):
        # 获取浏览器驱动对象
        self.driver = webdriver.Firefox()
        # 打开url
        self.driver.get("http://localhost")
        # 设置隐式等待
        self.driver.implicitly_wait(10)
        # 设置页面最大化
        self.driver.maximize_window()
    def tearDown(self):
        # 关闭浏览器驱动
        self.driver.quit()
    def test_login(self):
        driver = self.driver
        # 点击登录按钮
        driver.find_element_by_link_text("登录").click()
        # 输入用户名
        driver.find_element_by_id("username").send_keys("1380001111")
        # 输入密码
        driver.find_element_by_id("password").send_keys("123456")
        # 输入验证码
        driver.find_element_by_css_selector("#verify_code").send_keys("")
        # 点击登录按钮
        driver.find_element_by_css_selector("[name='sbtbutton']").click()
        # 获取错误提示信息
        msg = driver.find_element_by_css_selector(".layui-layer-content").text
        print("msg=", msg)
        try:
            # 断言
            self.assertIn("验证码不能为空", msg)
        except AssertionError as e:
            # 保存截图
            img_path = "../day05/img{}.png".format(time.strftime("%Y%m%d-%H%M%S"))
            driver.get_screenshot_as_file(img_path)
            # 抛出异常
            raise e


if __name__ == '__main__':
    unittest.main()