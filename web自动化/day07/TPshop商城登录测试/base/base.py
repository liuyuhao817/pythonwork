from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

class Base:
    # 初始化方法
    def __init__(self,driver):
        self.driver = driver

    # 查找元素方法 提供点击 输入 获取文本使用
    def base_find_element(self,loc,timeout=30,poll_frequency=0.5):
        # 使用了显示等待
        """
        :param loc:元素的配置信息 格式为元组 如 login_username = By.ID,"username"
        :param timeout: 默认超时时间为30 可以通过传入参数进行修改
        :param poll_frequency: 默认访问频率为0.5
        :return: 查找到的元素一定要进行返回
        """
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll_frequency).until(lambda x:x.find_element(*loc))

    # 点击方法
    def base_click(self,loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self,loc,value):
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self,loc):
        # 注意，一定要返回元素的文本信息
        return self.base_find_element(loc).text

    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/fail.png")

    # 封装判断元素是否存在
    def base_if_exist(self,loc):
        try:
            self.base_find_element(loc,timeout=2)
            # 找到元素
            return True
        except:
            # 没找到元素
            return False