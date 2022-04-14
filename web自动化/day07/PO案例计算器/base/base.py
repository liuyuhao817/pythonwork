from selenium.webdriver.support.wait import WebDriverWait

class Base:

    # 初始化方法
    def __init__(self,driver):
        self.driver = driver

    # 查找元素
    def base_find_element(self,loc,timeout=30,poll_frequency=0.5):
        # 显式等待
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll_frequency).until(lambda x:x.find_element(*loc))
    # 点击
    def base_click(self,loc):
        # 调用查找元素进行点击
        self.base_find_element(loc).click()

    # 获取value属性方法封装
    def base_get_value(self,loc):
        # 使用get_attribute("value") 获取属性值
        # 一定要返回
        return self.base_find_element(loc).get_attribute("value")

    # 截图
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/file.png")

