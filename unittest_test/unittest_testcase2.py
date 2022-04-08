"""
此文件的命名要符合命名规范，以字母数字下划线组成且不能以数字开头
代码的目的：学习TextCase测试用例模块的书写方法
"""
# 1、导包
import unittest
# 2、自定义测试类  需要继承unittest模块中的TestCase类
class TestDemo2(unittest.TestCase):

    # 3、书写测试方法  即用例代码
    #书写要求：测试方法必需以test_开头（本质以test开头）
    def test_method1(self):
        print('测试方法2-1')

    def test_method2(self):
        print('测试方法2-2')# 4、执行用例（方法）
# 4.1、将光标放在类名的后边运行，会执行类中所有的测试方法
# 4.2、将光标放在方法名后边运行，只会执行当前方法