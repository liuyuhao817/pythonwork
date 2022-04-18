"""GET请求方法演练"""
# 1、导入requests库
import requests

# 2、调用get方法
url = "http://www.baidu.com"
# GET请求带参数
# 不推荐写法 静态
# url = "http://www.baidu.com/s?wd=python"
# 示例一：定义字典
# params = {"wd": "python"}  #http://www.baidu.com/?wd=python
# 示例二
# params = {"wd": "python,java"}  #http://www.baidu.com/?wd=python%2Cjava
# 示例三
params = {"wd": "python,java,php","test": "123"} #http://www.baidu.com/?wd=python%2Cjava%2Cphp&test=123
# 请求时带参数 params
response = requests.get(url, params=params)

# 3、获取请求的url地址
print(response.url)

# 4、打印响应状态码
print(response.status_code)

# 5、打印响应内容
print(response.text)

"""POST请求方法演练"""
# 调用post方法
# 请求url地址
# url = "http://ihrm-test.itheima.net/api/sys/login"

# 请求headers
# headers = {"Content-Type": "application/json"}
# 请求json数据   指明参数名 json
# json = {"mobile": "13800000002", "password": "123456"}
# response = requests.post(url, json=json, headers=headers)

# FROM表单数据传递  指明参数名是 data
url ='http://localhost/index.php?m=Home&c=User&a=do_login'
login_data = {
        "username": "17362955793",
        "password": "123456",
        "verify_code": "8888"
}
response = requests.post(url=url,data=login_data)
# 获取响应对象
print(response.json())  # 返回json格式的数据 type:dict
print(response.text)    # 返回字符串格式的数据 type:str
# 获取响应状态码
print(response.status_code)

"""PUT请求方法演练"""
# 调用put方法
# 请求url地址
url = "http://ihrm-test.itheima.net/api/sys/user"
# 请求headers
headers = {"Content-Type": "application/json"}
# 请求json数据
json = {"username": "李四",
        "mobile": "13800000002",
        "timeOfEntry": "2019-09-01",
        "formOfEmployment": 1,
        "departmentName": "测试部",
        "departmentId": "1063678149528784896",
        "correctionTime": "2019-09-02"
        }
response = requests.put(url, json=json, headers=headers)

# 获取响应对象
# print(response.json())  # 返回json格式的数据 type:dict
# print(response.text)    # 返回字符串格式的数据 type:str
# 获取响应状态码
# print(response.status_code)

"""DELETE请求方法演练"""
# 调用delete方法
# 请求url地址
url = "http://ihrm-test.itheima.net/api/sys/user/11"

response = requests.delete(url)

# 获取响应状态码
# print(response.status_code)

"""
常见响应信息
response.status_code  # 获取响应状态码
response.text  # 获取响应内容
response.json()  # 获取响应json数据
response.url  # 获取请求的url地址
response.headers  # 获取响应头信息
response.cookies  # 获取响应的cookie信息
response.content  # 获取响应的二进制内容
response.encoding  # 获取响应内容的编码方式
"""