#1、获取第三方的测试运行类模块，将其放在代码的目录里
# 2、导包
import unittest
from HTMLTestRunnerCN import HTMLTestReportCN
# 3、使用套件对象，加载对象 去添加用例方法
suite=unittest.defaultTestLoader.discover('./case','unittest*.py')
# 4、实例化第三方的运行对象，并允许套件对象
# HTMLTestRunner()
# stream=sys.stdout 测试报告的文件对象  注意点：要是有wb打开
# verbosity=1, 可选 是报告的详细程度 默认1
# title=None, 可选  测试报告的标题
# description=None 可选 描述信息
# tester = None    可选 测试人
# 写入文件

file='reportCN.html' #报告的后缀是html
with open(file,'wb') as f:
    runner=HTMLTestReportCN(f,1,'测试报告','python 3.10','刘育豪') #运行对象
    #运行对象执行套件
    runner.run(suite)