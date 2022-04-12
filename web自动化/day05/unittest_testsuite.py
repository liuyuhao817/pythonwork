"""
TestSuite:说明：测试套件
步骤：
    1. 导包
    2. 获取测试套件对象 suite = unittest.TestSuite()
    3. 调用addTest()方法 添加测试用例
添加测试用例方法：
    1. suite.addTest(类名("方法名称")) # 添加指定类中指定的测试方法
    2. suite.addTest(unittest.makeSuite(类名)) # 添加指定类中所有已test开头的方法
TextTestRunner:说明：执行测试套件方法
步骤：
    1. 导包
    2. 实例化后去执行套件对象 runner = unittest.TextTestRunner()
    3. 调用run方法去执行 runner.run(suite)
"""
# 导包
import unittest
from web自动化.day05.unittest_testcase import Test01
# 实例化suite
suite = unittest.TestSuite()

# 调用添加方法
# suite.addTest(类名("方法名称")) # 添加指定类中指定的测试方法
# suite.addTest(Test01("test_add"))

# suite.addTest(unittest.makeSuite(类名)) # 添加指定类中所有已test开头的方法
suite.addTest(unittest.makeSuite(Test01))

# 执行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)