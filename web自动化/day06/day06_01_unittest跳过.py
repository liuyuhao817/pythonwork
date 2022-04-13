"""
跳过用例
分类：
    1. 直接跳过
        语法：@unittest.skip(说明)    场景：一般适合功能未实现完成用例
    2. 条件满足跳过
        语法：@unittest.skipIf(条件, 原因)    场景：一般判断条件满足，就不执行；如：达到指定版本，此功能失效；
提示：以上两种方式，都可以修饰函数和类；
"""

import unittest

verson = 35

class Test01(unittest.TestCase):

    # @unittest.skip("该方法暂未是实现完成")
    def test01(self):
        print("test01")

    @unittest.skipIf(verson>30,"该版本大于30跳过")
    def test02(self):
        print("test02")

@unittest.skip("没原因，就想跳过")
class TestSkip2(unittest.TestCase):

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")