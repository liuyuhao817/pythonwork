from selenium import webdriver

from web自动化.day08.TPshop.page import url


class GetDriver:

    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Firefox()

            cls.driver.maximize_window()

            cls.driver.get(url)

        return cls.driver

    @classmethod
    def quit_driver(cls):

        if cls.driver is not None:
            cls.driver.quit()
            # 关闭后要将driver设置为None
            cls.driver = None