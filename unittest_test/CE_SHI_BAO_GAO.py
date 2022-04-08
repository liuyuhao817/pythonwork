#1、获取第三方的测试运行类模块，将其放在代码的目录里
# 2、导包
import unittest
from HTMLTestRunner import HTMLTestRunner
# 3、使用套件对象，加载对象 去添加用例方法
suite=unittest.defaultTestLoader.discover('./case','unittest*.py')
# 4、实例化第三方的运行对象，并允许套件对象
# HTMLTestRunner()
# stream=sys.stdout 测试报告的文件对象  注意点：要是有wb打开
# verbosity=1, 可选 是报告的详细程度 默认1
# title=None, 可选  测试报告的标题
# description=None 可选 描述信息
file='report.html' #报告的后缀是html
with open(file,'wb') as f:
    runner=HTMLTestRunner(f,1,'测试报告','python 3.10') #运行对象
    #运行对象执行套件
    runner.run(suite)

"""
1. 组织用例文件(TestCase 里边), 书写参数化, 书写断言, 书写 Fixture, 书写 跳过, 如果单个测试测试文
件, 直接运行, 得到测试报告, 如果有多个测试文件, 需要组装运行生成测试报告
2. 使用 套件对象组装, 或者使用 加载对象组装
3. 运行对象 运行
    3.1 运行对象 = 第三方的运行类(文件对象(打开文件需要使用 wb 方式))
    3.2 运行对象.run(套件对象)
"""