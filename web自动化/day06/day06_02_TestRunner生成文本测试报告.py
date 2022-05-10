#导包
import unittest

# 定义测试套件
suite = unittest.defaultTestLoader.discover("./","day06_01_unittest跳过.py")

# 执行
with open("../day06/report.txt","w",encoding="utf-8") as f:
    unittest.TextTestRunner(stream=f,verbosity=2).run(suite)