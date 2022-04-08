"""
断言：让程序代替人工自动的判断预期结果和实际结果是否相符.
断言的结果有两种:
    > True, 用例通过
    > False, 代码抛出异常, 用例不通过
在 unittest 中使用断言, 都需要通过 self.断言方法 来试验

self.assertEqual(预期结果, 实际结果) # 判断预期结果和实际结果是否相等
    1. 如果相等, 用例通过
    2. 如果不相等,用例不通过, 抛出异常

self.assertIn(预期结果, 实际结果) # 判断预期结果是否包含在实际结果中
    1. 包含 ,用例通过
    2. 不包含, 用例不通过, 抛出异常
assertIn('admin', 'aaaaaadminnnnnnn') # 包含
assertIn('admin', 'addddddmin') # 不是包含
"""
import unittest
from tools import login
class TestLogin(unittest.TestCase):
    def test_username_password_ok(self):
        """正确的用户名和密码: admin, 123456, 登录成功"""
        self.assertEqual('登录成功', login('admin', '123456'))
    def test_username_error(self):
        """错误的用户名: root, 123456, 登录失败"""
        self.assertEqual('登录失败', login('root', '123456'))
    def test_password_error(self):
        """错误的密码: admin, 123123, 登录失败"""
        self.assertEqual('登录失败', login('admin', '123123'))
    def test_username_password_error(self):
        """错误的用户名和错误的密码: aaa, 123123, 登录失败"""
    # self.assertEqual('登录失败', login('aaa', '123123'))
        self.assertIn('失败', login('aaa', '123123'))


