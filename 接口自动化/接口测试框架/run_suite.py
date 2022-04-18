import time
import unittest
from 接口自动化.接口测试框架.scripts.test01_login import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner
# suite = unittest.defaultTestLoader.discover("./scripts","test01_login.py")

# 实例化测试套件
suite = unittest.TestSuite()
# 封装测试套件
suite.addTest(unittest.makeSuite(TestLogin))

report ="./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

with open(report,'wb') as f:
    HTMLTestRunner(f,title="接口测试报告").run(suite)