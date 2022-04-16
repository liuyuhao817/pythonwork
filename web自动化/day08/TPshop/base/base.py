import time

from selenium.webdriver.support.wait import WebDriverWait


class Base:

    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法封装
    def base_find_element(self, locator, timeout=30,poll_frequency=0.5):
        #显示等待 查找元素
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency).until(lambda x: x.find_element(*locator))

    #点击元素方法封装
    def base_click(self, locator):
        # 点击元素
        self.base_find_element(locator).click()

    #输入元素方法封装
    def base_input(self, locator, value):
        # 输入元素
        el = self.base_find_element(locator)
        # 清空文本框
        el.clear()
        # 输入文本
        el.send_keys(value)

    #获取元素文本方法封装
    def base_get_text(self, locator):
        # 获取元素文本
        return self.base_find_element(locator).text

    #截图方法封装
    def base_get_image(self):
        # 截图
        self.driver.get_screenshot_as_file("./image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    #判断元素是否存在方法封装
    def base_element_is_exist(self, locator):
        try:
            self.base_find_element(locator=locator,timeout=2)
            return True  # 元素存在返回True
        except:
            return False  # 元素不存在返回False

