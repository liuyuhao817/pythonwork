import json

#1、把准备的json字符串转换为Python数据
#1.1、准备json字符串
json_str = '''[{"provinceName":"美国", "currentConfirmedCount":1179041,"confirmedCount":1643499},
  {"provinceName":"英国", "currentConfirmedCount":222227,"confirmedCount":259559}]'''
#1.2、把准备的json字符串转换为Python数据
rs = json.loads(json_str)
# print(rs)

#2、把json格式文件转换为python类型的数据
#2.1 构建指向改文件的文件对象
with open(r"D:\python_work\test.json",encoding="utf8") as fb:
# 2.2 加载该文件对象 转换为python类型的数据
    python_list = json.load(fb)
    print(python_list)
