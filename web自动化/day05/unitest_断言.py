"""
什么是断言？   让程序代替人为判断执行结果是否与预期结果相等的过程
为什么要断言？
    自动化脚本执行时都是无人值守，需要通过断言来判断自动化脚本的执行是否通过
    注：自动化脚本不写断言，相当于没有执行测试一个效果。
常用断言
    1. self.assertEqual(ex1, ex2)  #判断ex1 是否相等ex2
    2. self.assertIn(ex1 ,ex2) # ex2是否包含ex1 注意：所谓的包含不能跳字符
    3. self.assertTrue(ex) # 判断ex是否为True
"""
import unittest

class Test01(unittest.TestCase):

    def test01(self):
        # 断言是否为True
        # flag = True
        # self.assertTrue(flag)
        # 断言是否为false
        # flag = False
        # self.assertFalse(flag)

        # 判断两个字符串是否相等
        # self.assertEqual("你好","您好")

        # 判断后边的字符串是否包含前面的字符串
        # self.assertIn("hello banma","hello banma,wahaha")

        # 判断是否为None
        flag = None
        self.assertIsNone(flag)
        # self.assertIsNotNone(flag)