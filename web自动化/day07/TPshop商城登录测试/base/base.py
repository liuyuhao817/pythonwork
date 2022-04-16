from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from web自动化.day07.TPshop商城登录测试.tools.get_logger_ok import GetLogger
from web自动化.day07.TPshop商城登录测试.tools.logger_封装 import get_logger
# 没有使用单例
# log = get_logger()
# 使用单例
log = GetLogger().get_logger()

class Base:
    # 初始化方法
    def __init__(self,driver):
        log.info("初始化浏览器驱动{}".format(driver))
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
        log.info("开始查找元素{}".format(loc))
        # 显示等待
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll_frequency).until(lambda x:x.find_element(*loc))

    # 点击方法
    def base_click(self,loc):
        log.info("开始点击元素{}".format(loc))
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self,loc,value):
        log.info("开始输入{}".format(value))    # 注意，这里的value是字符串
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        log.info("正在给元素{}清空".format(loc))
        # 输入
        log.info("正在给元素{}输入{}".format(loc,value))
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self,loc):
        log.info("开始获取元素{}的文本".format(loc))
        # 注意，一定要返回元素的文本信息
        return self.base_find_element(loc).text

    # 截图方法
    def base_get_image(self):
        log.info("开始截图")
        self.driver.get_screenshot_as_file("../image/fail.png")

    # 封装判断元素是否存在
    def base_if_exist(self,loc):
        try:
            self.base_find_element(loc,timeout=2)
            log.info("判断元素{}存在".format(loc))
            # 找到元素
            return True
        except:
            log.info("判断元素{}不存在".format(loc))
            # 没找到元素
            return False