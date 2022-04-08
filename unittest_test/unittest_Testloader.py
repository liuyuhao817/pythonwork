"""TestLoader的使用"""
# 1、导包
import unittest
# 2、实例化加载对象并添加用例
# unittest.TestLoader().discover('用例所在路径','用例的代码文件名')   *是通配符
# suite=unittest.TestLoader().discover('./case','unittest*.py')
# 使用默认的加载对象加载用例
suite=unittest.defaultTestLoader.discover('./case','unittest*.py')
# 实例化运行对象
# runner=unittest.TextTestRunner()
# runner.run(suite)
unittest.TextTestRunner().run(suite)