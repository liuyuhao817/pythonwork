import unittest

from web自动化.day07.PO案例计算器.base.get_driver import GetDriver
from web自动化.day07.PO案例计算器.page.page_calc import PageClac
from parameterized import parameterized

from web自动化.day07.PO案例计算器.tools.read_json import read_json


def get_data():
    datas = read_json("calc.json")     # 这时的datas是这种  {"":{},"":{},"":{}}
    arrs = []
    for data in datas.values():    # 这时的data是将value从datas中取出的value  {"":"","":"","":""}  {}  {}
        arrs.append((data["a"],data["b"],data["expect"]))  #再将data的value值获取到 组装成元组加入arrs列表中
    return arrs      #[(),(),()]

class TestClac(unittest.TestCase):

    driver = None
    # setup
    @classmethod
    def setUpClass(cls) -> None:

        # 获取driver
        cls.driver = GetDriver().get_driver()
        # 初始化页面对象
        cls.clac = PageClac(cls.driver)

    # teardown
    @classmethod
    def tearDownClass(cls) -> None:
        # 关闭driver
        GetDriver().quit_driver()

    # 测试方法
    @parameterized.expand(get_data)
    def test_add_clac(self,a,b,expect):
        # 调用计算器业务方法
        self.clac.page_add_clac(a,b)
        try:
            # 断言
            self.assertEqual(self.clac.page_get_value(),str(expect))
        except AssertionError:
            # 截图
            self.clac.page_get_image()