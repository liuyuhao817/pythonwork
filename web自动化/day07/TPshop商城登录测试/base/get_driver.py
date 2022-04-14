from selenium import webdriver
from web自动化.day07.TPshop商城登录测试 import page

class GetDriver:

    # 设置类属性
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 实例化浏览器
            cls.driver = webdriver.Firefox()
            # 最大化
            cls.driver.maximize_window()
            #打开浏览器
            cls.driver.get(page.url)
        # 永远保持只有一个实例对象 无论获取多少次
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 注意此处有大坑
            # 关闭后要再将driver置空
            cls.driver = None