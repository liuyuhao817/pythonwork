import time

from HTMLTestRunner import HTMLTestRunner
import unittest

# 封装测试套件
suite = unittest.defaultTestLoader.discover("./",'unittest_tpshop*.py')

# 指定报告路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 打开文件流
with open(report,"wb") as f:
    HTMLTestRunner(f).run(suite)