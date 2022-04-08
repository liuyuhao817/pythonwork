"""
这个代码是用来学习TestSuite和TestRunner的使用
"""
# 1、导包
import unittest
# 2、实例化（创建对象）套件对象
from unittest_test.case.unittest_testcase1 import TestDemo1
from unittest_testcase2 import TestDemo2

suite=unittest.TestSuite()
# 3、使用套件对象添加用例方法
# 方式一  套件对象.addTest(测试类名("方法名"))  只能一次添加单个方法
# suite.addTest(TestDemo1('test_method1'))
# suite.addTest(TestDemo1('test_method2'))
# suite.addTest(TestDemo2('test_method1'))
# suite.addTest(TestDemo2('test_method2'))

# 方式二 将一个测试类中所以的方法进行添加 套件对象.addTest(unittest.makeSuite((测试类名)))
suite.addTest(unittest.makeSuite(TestDemo1))
suite.addTest(unittest.makeSuite(TestDemo2))

# 4、实例化运行对象
runner=unittest.TextTestRunner()
# 5、使用运行对象去执行套件对象
# 运行对象.run(套件对象)
runner.run(suite)
# 运行结果中 . 表示用例通过  F表示用例不通过 E表示用例代码有问题
