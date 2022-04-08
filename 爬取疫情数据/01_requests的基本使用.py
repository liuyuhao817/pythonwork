#导入模块
import requests
#发送请求获取响应
response = requests.get('http://www.baidu.com')
# #print(response) #<Response [200]>
#获取响应数据
# response.encoding  查询网站编码方式
# print(response.encoding)  #ISO-8859-1
#修改显示的编码方式
# response.encoding = "utf-8"
# response.text  获取响应内容 响应体 str类型
# print(response.text)
# response.content 获取二进制的响应数据
# decode 解码 默认使用utf-8
print(response.content.decode(encoding='utf-8'))