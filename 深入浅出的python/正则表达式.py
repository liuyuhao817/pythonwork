'''
1.导入模块
2.通过match方法验证正则
3.判断验证是否成功
4.如果成功，获取匹配结果
'''
# #1.导入正则模块
# import re
# # 2.通过match方法验证正则
# # re.match("正则表达式","要验证或要检测的字符串")
# # match()方法如果匹配成功 返回match.object对象 如果失败返回None
# #         "正则字符串" "要检测内容"
# result = re.match("\w{4,20}@163[.]com$","Hello@163.com")
#
# # 3.判断验证是否成功
# if result:
#     # 4.如果成功，获取匹配结果
#     print("匹配成功",result.group())
# else:
#     print("匹配失败")

# # 分组匹配之|
# #1.导入正则模块
# import re
# # 2.通过match方法验证正则
# # re.match("正则表达式","要验证或要检测的字符串")
# # match()方法如果匹配成功 返回match.object对象 如果失败返回None
# #         "正则字符串" "要检测内容"
# # | 作用 或者关系 只要左右正则表达式有一个满足即为匹配成功
# result = re.match("^[0-9]?[0-9]$|^100$","15")
#
# # 3.判断验证是否成功
# if result:
#     # 4.如果成功，获取匹配结果
#     print("匹配成功",result.group())
# else:
#     print("匹配失败")

# # 分组匹配之()
# #1.导入正则模块
# import re
# # 2.通过match方法验证正则
# # re.match("正则表达式","要验证或要检测的字符串")
# # match()方法如果匹配成功 返回match.object对象 如果失败返回None
# #         "正则字符串" "要检测内容"
# result = re.match("(\d{3,4})-(\d{7,8})","010-12345678")
#
# # 3.判断验证是否成功
# if result:
#     # 4.如果成功，获取匹配结果
#     print("匹配成功",result.group())#010-12345678
#     print("前半段",result.group(1))#010
#     print("后半段",result.group(2))#12345678
# else:
#     print("匹配失败")

#分组匹配之\   引用
# import re
# #1.导入正则模块
# # 2.通过match方法验证正则
# # # re.match("正则表达式","要验证或要检测的字符串")
# # # match()方法如果匹配成功 返回match.object对象 如果失败返回None
# # #   "正则字符串" \ 表转移字符 有特殊用法  \\ 表正则里面的\      "要检测内容"
# #\1表示引用第一个分组
# result = re.match("<([a-zA-z0-9]*)>.*</\\1>","<html>text</html>")
# # # 3.判断验证是否成功
# if result:
#     # 4.如果成功，获取匹配结果
#     print("匹配成功",result.group())
#
# else:
#     print("匹配失败")


# # 分组匹配之别名
# import re
# #1.导入正则模块
# # 2.通过match方法验证正则
# # # re.match("正则表达式","要验证或要检测的字符串")
# # # match()方法如果匹配成功 返回match.object对象 如果失败返回None
# # #   "正则字符串" \ 表转移字符 有特殊用法  \\ 表正则里面的\      "要检测内容"
# # ?P<name> 表示给分组取别名 别名为name (写在要取别名的分组()里面) ?P=name 表示引用别名为name的分组 (写在使用的位置 加(表明这是一个整体)
# result = re.match("<(?P<name1>[a-zA-Z0-9]+)><(?P<name2>[a-zA-Z0-9]+)>.*</(?P=name2)></(?P=name1)>", "<html><h1>asdbj</h1></html>")
# # # 3.判断验证是否成功
# if result:
#     # 4.如果成功，获取匹配结果
#     print("匹配成功",result.group())
#
# else:
#     print("匹配失败")


