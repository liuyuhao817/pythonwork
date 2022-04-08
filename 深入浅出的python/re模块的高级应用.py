#1.导入正则模块
import re
# 2.通过match方法验证正则
# re.match("正则表达式","要验证或要检测的字符串")
# match()方法如果匹配成功 返回match.object对象 如果失败返回None
#         "正则字符串" "要检测内容"
# result = re.match("\w{4,20}@163[.]com$","Hello@163.com")
# match 和 search 区别
# match 从需要检测的字符串开头位置匹配 如果失败返回none
# search 从需要检测的字符串搜索满足正则的内容 有则返回match.object对象
# search使用
# result = re.search("163","Hello@163.com")

# findall()  在需要匹配的字符串中查找所有满足正则的内容，返回值是列表
# result = re.findall("\d+", "阅读次数:9999,转发次数：6666,评论次数：38")

# sub("正则表达式", "新的内容", "要替换的字符串") 字符串替换（按照正则，查找字符串并且替换为指定的内容）返回值是替换后的字符串
# result = re.sub("\d+", "10000", "阅读次数:9999,转发次数：6666,评论次数：38")

# # split("正则表达式", "待拆分的字符串")  按照正则拆分字符串，返回值是一个列表
# result = re.split(":| ", "info:hello@163.com zhangsan lisi")

# 贪婪和非贪婪 (默认贪婪)
# 贪婪：默认，表示在满足正则的情况尽可能多的取内容
# 非贪婪：表示在满足正则的情况下，尽可能少的取内容
# 贪婪的转变为非贪婪： 在 *  ?  + {} 的后面再加上 ？就可以了
result = re.match("aaa(\d+?)", "aaa123456")
# 3.判断验证是否成功
if result:
    # 4.如果成功，获取匹配结果
    print("匹配成功", result.group())#aaa1
    print("匹配成功",result.group(1))#1
else:
    print("匹配失败")

