# 导包
import time
import unittest
from 接口自动化.IHRM.scripts.test_login import TestLogin
from 接口自动化.IHRM.scripts.test_employee import TestEmployee
from 接口自动化.IHRM.tools.HTMLTestRunner import HTMLTestRunner
# 组装测试套件
suite = unittest.TestSuite()
# 登录接口测试用例
suite.addTest(unittest.makeSuite(TestLogin))
# 员工管理场景测试用例
# suite.addTest(TestLogin("test01_login"))
suite.addTest(unittest.makeSuite(TestEmployee))
# 指定测试报告的路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# 打开文件流
with open(report, "wb") as f:
    # 创建HTMLTestRunner运行器
    runner = HTMLTestRunner(f, title="API Report")
    # 执行测试套件
    runner.run(suite)

