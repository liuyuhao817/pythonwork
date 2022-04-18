import requests

# 1). 访问百度首页的接口`http://www.baidu.com`，获取以下响应数据
response = requests.get("http://www.baidu.com")

# 2). 获取响应状态码
print(response.status_code)

# 3). 获取请求URL
print(response.url)

# 4). 获取响应字符编码
print(response.encoding)

# 5). 获取响应头数据
print(response.headers)
print(response.headers["Content-Type"])

# 6). 获取响应的cookie数据
print(response.cookies)
# 提取指定的cookie
print(response.cookies["BDORZ"])

# 7). 获取文本形式的响应内容
print(response.text)

# 8). 获取字节形式的响应内容
print(response.content)