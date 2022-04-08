import re
#1.导入正则模块
# 2.通过match方法验证正则
# # re.match("正则表达式","要验证或要检测的字符串")
# # match()方法如果匹配成功 返回match.object对象 如果失败返回None
# #   "正则字符串" \ 表转移字符 有特殊用法  \\ 表正则里面的\      "要检测内容"
#\1表示引用第一个分组
# r作用 在正则表达式中加入r 表示此正则中的\不再具有python的转义字符的作用 而是单纯作为一个斜杠的原生含义

result = re.match(r"<([a-zA-z0-9]*)>.*</\1>","<html>text</html>")
# # 3.判断验证是否成功
if result:
    # 4.如果成功，获取匹配结果
    print("匹配成功",result.group())

else:
    print("匹配失败")
