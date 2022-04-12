"""
说明：装置函数(setUp、tearDown)
级别：
    1). 函数级别 def setUp() / def tearDown()
            特性：几个测试函数，执行几次。每个测试函数执行之前都会执行 setUp，执行之后都会执行tearDwon
    2). 类级别 def setUpClass() / def tearDownClass()
            特性：测试类运行之前运行一次setUpClass 类运行之后运行一次tearDownClass
            注意：类方法必须使用 @classmethod修饰
    3). 模块级别：def setUpModule() / def tearDownModule()
            特殊：模块运行之前执行一次setUpModule ,运行之后运行一次tearDownModule
提示：
    无论使用函数级别还是类级别，最后常用场景为：
    初始化：
        1. 获取浏览器实例化对象
        2. 最大化浏览器
        3. 隐式等待
    结束：
        关闭浏览器驱动对象
"""

import unittest

class Test(unittest.TestCase):

    def setUp(self) -> None:
        print("setup被执行")

    def tearDown(self) -> None:
        print("teardown被执行")

    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass被执行")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass被执行")

    def test01(self):
        print("test01被执行")

    def test02(self):
        print("test02被执行")

