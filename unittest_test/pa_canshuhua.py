"""
参数化
在测试方法中, 使用 变量 来代替具体的测试数据, 然后使用传参的方法将测试数据传递给方法的变量
好处: 相似的代码不需要多次书写.
工作中场景:
    1. 测试数据一般放在 json 文件中
    2. 使用代码读取 json 文件,提取我们想要的数据 ---> [(), ()] or [[], []]
"""

# 1. 导包 unittest/ pa
import json
import unittest
from parameterized import parameterized
from unittest_test.tools import login

# 组织测试数据
# data=[
#     ('admin','123456','登录成功'),
#     ('root','123456','登录失败'),
#     ('admin','123123','登录失败'),
# ]
# 组织测试数据 [(), (), ()] or [[], [], []]
def build_data():
    with open('data.json', encoding='utf-8') as f:
        result = json.load(f) # [{}, {}, {}]
        data = []
        for i in result: # i {}
            data.append((i.get('username'), i.get('password'), i.get('expect')))
    return data

# 2. 定义测试类

class TestLogin(unittest.TestCase):
        # 4. 组织测试数据并传参
    @parameterized.expand(build_data())
    # 3. 书写测试方法(用到的测试数据使用变量代替)
    def test_login(self,username,password,expect):
        self.assertAlmostEqual(expect, login(username, password))
