"""
什么是数据驱动？说明：
    1. 通过测试数据控制用例的执行，直接影响测试结果；
    2. 数据驱动是最好结合PO+参数化技术使用；
数据驱动优点
    将维护关注点放到测试数上，而不去关注测试脚本代码；
数据驱动常用的格式
    1. JSON（重点） 2. XML 3. EXCEL 4. CSV 5. TXT
JSON操作：
    1、json转python对象   json.loads(json字符串)
    2、python对象转json   json.dumps(python对象)
    3、读取json文件       json.load(json文件)
    4、将python对象转换为json字符串写入json文件   json.dump(python对象,json文件)
JSON里面的属性名只能用双引号
json本质是一个字符串
"""
import json

# 把python字典类型转换为 JSON字符串
data = {
    'id': 1,
    'name': 'Tom',
    'address': '北京市海淀区',
    'school': None
}
print("转换前data格式：",type(data))
json_str01 = json.dumps(data)
print("转换之后格式：",type(json_str01))
print(json_str01)

# 把JSON字符串转换为python字典
json_str02 = '{"id": 1, "name": "Tom", "address": "北京市海淀区", "school": null}'
print("转换前格式：",type(json_str02))
dict_data = json.loads(json_str02)
print("转换后格式：",type(dict_data))
print(dict_data)

# 读取JSON文件  读取时不写 默认就是r
with open('./login.json',"r", encoding='UTF-8') as f:
    data = json.load(f) # 返回的数据类型为字典或列表
    print(data)


# 写入JSON文件
param = {'name': 'tom', 'age': 20}
with open('data2.json', 'w', encoding='UTF-8') as f:
    json.dump(param, f,ensure_ascii=False)
