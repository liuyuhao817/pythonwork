"""
定义测试用例
    1. 导包：import unittest
    2. 定义测试类：新建测试类必须继承unittest.TestCase
    3. 定义测试方法：测试方法名称命名必须以test开头
运行：
    1. 运行测试类所有的测试方法，光标定位到类当前行右键运行
    2. 运行单个测试方法：光标放到测试方法当前行。
"""
"""
案例：定义一个实现加法操作的函数，并对该函数进行测试
"""
# 1、导包
import unittest

# 2、编写求和函数
def add(x,y):
    return x+y

# 定义测试类并继承
class Test01(unittest.TestCase):
    # 定义测试方法  注意以test开头
    def test_add(self):
        # 调用 要使用的函数
        result = add(1,1)
        print("结果为：",result)

    def test_add1(self):
        # 调用 要使用的函数
        result = add(3,1)
        print("结果为：",result)
