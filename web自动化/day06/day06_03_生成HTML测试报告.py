"""
HTML报告：根据TextTestRunner改编而来
操作：
    1. 导包   from  xx.HTMLTestRunner import HTMLTestRunner
    2. 定义测试套件
        suite = unittest.defaultTestLoader.discover("../case", pattern="test*.py")
    3. 实例化HTMLTestRunner类,并调用run方法执行测试套件。
        with open(报告存放路径, "wb") as f:    #注意：生成html报告，必须使用wb，以二进制形式写入
            # 实例化HTMLTestRunner类
            HTMLTestRunner(stream=f).run(测试套件)
        # HTMLTestRunner() 参数说明  HTMLTestRunner(f,1,'测试报告','python 3.10')
        # stream=sys.stdout 测试报告的文件对象  注意点：要是有wb打开
        # verbosity=1, 可选 是报告的详细程度 默认1
        # title=None, 可选  测试报告的标题
        # description=None 可选 描述信息
"""
#导包
import time
import unittest
from HTMLTestRunnerCN import HTMLTestReportCN
# 定义测试套件
suite = unittest.defaultTestLoader.discover("./",pattern="day06_01_unittest跳过.py")

report = "../day06/reportCN{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
# 执行
with open(report,"wb") as f:
    HTMLTestReportCN(stream=f,description="操作系统Windows11",verbosity=2,title="xx项目自动化测试报告").run(suite)