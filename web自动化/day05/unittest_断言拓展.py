"""
断言拓展：
    断言有两种实现方式
    1、使用unittest框架中的断言
    2、使用python自带断言
    1. assert str1 == str2 # 判断str1 是否与str2相等
    2. assert str1 in str2 # 判断str2 是否包含str1
    3. assert True/1 # 判断是否为True
"""

# 使用python自带断言 判断两个字符串是否相等
assert "hello" == 'hello'
# 不相等
# assert "hello" == "hi"


# 第二个字符串是否包含第一个字符串
# assert  "hello" in "hellos"
# assert  "hello" in "heloo"

# 判断是否为true  0为False  1为True
# assert True
# assert 0
# assert 1