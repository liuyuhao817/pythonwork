import unittest

class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        """每个测试方法执行之前都会调用的方法"""
        print("每个方法执行前")

    def tearDown(self) -> None:
        """每个测试方法执行之后都会调用的方法"""
        print('每个方法执行后')

    @classmethod
    def setUpClass(cls) -> None:
        """测试类中的所有方法执行前都会执行的方法"""
        print("类中所有方法执行前")

    @classmethod
    def tearDownClass(cls) -> None:
        """测试类中的所有方法执行后执行的方法"""
        print("类中所有方法执行后")

    def test_1(self):
        print('测试方法1')

    def test_2(self):
        print('测试方法2')
        
# 方法级别和类级别的 前后的方法,不需要同时出现,根据用例代码的需要自行的选择使用
 # Fixture_jichu.py::TestLogin::test_1                  类中所有方法执行前
 # PASSED                               [    50%]       每个方法执行前
                                                        # 测试方法1
# 每个方法执行后
# Fixture_jichu.py::TestLogin::test_2 PASSED    [100%]  每个方法执行前
                                                        # 测试方法2
                                                        # 每个方法执行后
#                                                       类中所有方法执行后