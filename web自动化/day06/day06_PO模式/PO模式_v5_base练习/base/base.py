from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    # 初始化方法
    def __init__(self):
        #获取driver
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1")

    # 查找元素方法
    def base_find_element(self,loc,timeout=30,poll_frequency=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll_frequency).until(lambda x:x.find_element(*loc))

    # 点击方法
    def base_click(self,loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self,loc,value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        # 注意，一定要返回元素的文本信息
        return self.base_find_element(loc).text

    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/fail.png")