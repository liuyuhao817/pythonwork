from selenium.webdriver.common.by import By

from web自动化.day07.PO案例计算器 import page
from web自动化.day07.PO案例计算器.base.base import Base


class PageClac(Base):

    # 点击数字方法
    def page_click_num(self,num):
        for n in str(num):
            # 拆开单个按键定位方式
            loc = By.CSS_SELECTOR,"#simple{}".format(n)
            self.base_click(loc)

    # 点击加号方法
    def page_click_add(self):
        self.base_click(page.clac_add)

    # 点击等号
    def page_click_eq(self):
        self.base_click(page.clac_eq)

    # 获取结果方法
    def page_get_value(self):
        return self.base_get_value(page.clac_result)

    # 点击清屏方法
    def page_click_clear(self):
        self.base_click(page.clac_clear)

    # 截屏
    def page_get_image(self):
        self.base_get_image()

    # 根据加法组装业务方法
    def page_add_clac(self,num1,num2):
        self.page_click_num(num1)
        self.page_click_add()
        self.page_click_num(num2)
        self.page_click_eq()