"""
对于一些未完成的或者不满足测试条件的测试函数和测试类, 不想执行,可以使用跳过
使用方法, 装饰器完成   代码书写在 TestCase 文件
# 直接将测试函数标记成跳过
    @unittest.skip('跳过额原因')
# 根据条件判断测试函数是否跳过 , 判断条件成立, 跳过
    @unittest.skipIf(判断条件, '跳过原因')
"""
import unittest

# 定义一个条件
version=30

class TestDemo(unittest.TestCase):
    @unittest.skip('没原因的单纯想跳过')
    def test_1(self):
        print('测试方法1')

    @unittest.skipIf(version>=30,'版本过高，不用测试')
    def test_2(self):
        print('测试方法2')

    def test_3(self):
        print('测试方法3')