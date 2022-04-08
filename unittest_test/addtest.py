"""
案例练习
"""
import unittest


from unittest_test.tools import add

# 自定义测试类
class TestAdd(unittest.TestCase):
    # 书写测试方法，也就是测试用例的代码
    def test_method(self):
        # 判断实际结果和预期结果是否相等
        if add(1,2)==3:
            print("测试通过")
        else:
            print("测试失败")

    def test_method1(self):
        # 判断实际结果和预期结果是否相等
        if add(5,8)==13:
            print("测试通过")
        else:
            print("测试失败")

    def test_method2(self):
        # 判断实际结果和预期结果是否相等
        if add(10,20)==30:
            print("测试通过")
        else:
            print("测试失败")
