import json
#1、把python转换为json字符串
#1.1、python类型字符串
json_str = '''[{"provinceName":"美国", "currentConfirmedCount":1179041,"confirmedCount":1643499},
  {"provinceName":"英国", "currentConfirmedCount":222227,"confirmedCount":259559}]'''
rs = json.loads(json_str)
#1.2、把python转换为json字符串
json_str = json.dumps(rs,ensure_ascii=False)
# print(json_str)

#2、把python以json格式存储到文件中
#2.1、构建要写入的文件对象
with open(r"D:\python_work\test1.json","w") as fp:
#2.2、把python以json格式存储到文件中
    json.dump(rs,fp,ensure_ascii=False)