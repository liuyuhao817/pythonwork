"""
这个代码是用来学习TestSuite和TestRunner的使用
"""
#导包
import unittest

from unittest_test.addtest import TestAdd

# 实例化套件对象
suite=unittest.TestSuite()
# 将测试用例测试类中的所有方法添加
suite.addTest(unittest.makeSuite(TestAdd))
# 实例化运行对象
runner=unittest.TextTestRunner()
# 使用运行对象去运行套件对象
runner.run(suite)



