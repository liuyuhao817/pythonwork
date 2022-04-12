"""
TestLoader：说明：
    1. 将符合条件的测试方法添加到测试套件中
    2. 搜索指定目录文件下指定字母开头的模块文件下test开始的方法，并将这些方法添加到测试套件中，最后返回测试套件
操作：
    1. 导包import unittest
    2. 调用TestLoader()
            写法1. suite = unittest.TestLoader().discover("指定搜索的目录文件","指定字母开头模块文件")
            写法2. suite = unittest.defaultTestLoader.discover("指定搜索的目录文件","指定字母开头模块文件") 【推荐】
            注意：如果使用写法1，TestLoader()必须有括号。
    3. 执行测试套件   unittest.TextTestRunner().run(suite)
TestSuite与TestLoader区别：
共同点：都是测试套件
不同点：实现方式不同
    TestSuite: 要么添加指定的测试类中所有test开头的方法，要么添加指定测试类中指定某个test开头的方法
    TestLoader: 搜索指定目录下指定字母开头的模块文件中以test字母开头的方法并将这些方法添加到测试套件中，最后返回测试套件
"""

# 导包
import unittest

# 调用方法
# loader = unittest.TestLoader().discover("../day05",pattern="unittest_testcase.py")
loader = unittest.defaultTestLoader.discover("../day05",pattern="unittest_testcase.py")

#执行套件方法
unittest.TextTestRunner().run(loader)