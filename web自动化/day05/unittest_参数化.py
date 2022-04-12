"""
为什么要参数化?    解决冗余代码问题；
什么是参数化?    说明：根据需求动态获取参数并引用的过程
参数化应用场景
    场景：解决相同业务逻辑，不同测试数据问题。
应用：
    安装插件通过命令安装：pip install parameterized
验证：     pip show parameterized
通过pycharm:File-->setting-->Project 工程名称
应用插件
    1. 导包 from parameterized import parameterized
    2. 修饰测试函数 @parameterized.expand([数据])
    3、在测试函数中使用变量接收传递过来的值
数据格式：
    1. 单个参数：类型为列表  []
    2. 多个参数：类型为列表嵌套元祖   [(),(),()]   [[],[],[]]
    3. 在测试函数中的参数设置变量引用参数值，注意：变量的数量必须和数据值的个数相同
"""
# 导包
import unittest
from parameterized import parameterized


def add(x, y):
    return x + y
# 构建测试数据
def build_data():
    return [(1, 1, 2), (1, 0, 1), (0, 0, 0)]

# 定义测试类并继承
class Test01(unittest.TestCase):
    # 定义测试方法 注意以test开头
    # 单个参数使用方法
    # @parameterized.expand(['1','2','3'])
    # def test_add(self,x):
    #     print("num：",x)

    # 多个参数使用方法
    # @parameterized.expand([(1,2,3),(4,5,9),(7,8,15)])
    # def test_add_more(self, x,y,z):
    #     print(f"num：{x}+{y}={z}")

    data = [[1, 2, 3], [4, 5, 9], [7, 8, 15]]
    # data = [(1, 2, 3), [4, 5, 9], [7, 8, 15]]
    # data = [(1, 2, 3), (4, 5, 9), (7, 8, 15)]
    @parameterized.expand(data)
    def test_add_more(self, x, y, z):
        print(f"num：{x}+{y}={z}")

    # @parameterized.expand(build_data())
    # def test_add_3(self, x, y, expect):
    #     print("x={} y={} expect={}".format(x, y, expect))
    #     result = add(x, y)
    #     # self.assertEqual(result, expect)
    #     assert result == expect