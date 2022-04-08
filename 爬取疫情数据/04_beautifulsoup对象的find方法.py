#1、导入模块
from bs4 import BeautifulSoup

#2、准备文档字符串
html = '''

'''
#3、创建BeautifulSoup对象
soup = BeautifulSoup(html,"lxml")

#4、查找title标签
title = soup.find("title")
print(title)
#5、查找a标签 默认返回查找到的第一个
a = soup.find("a")
print(a)
#查找所有的a标签   会返回一个列表
a_s = soup.find_all("a")
print(a_s)

#二、根据属性进行查找
#方式1、通过命名参数进行指定的
a = soup.find(id = "link1")
print(a)
#方式2、通过attrs来指定属性字典 进行查找
a = soup.find(attrs={"id":"link1"})
print(a)

#三、根据文本内容进行查找
text = soup.find(text="Elsie")
print(text)

#Tag对象 对应于原始文档中的xml或html标签
print(type(a))  #这里的a就是tag对象
print("标签名",a.name)
print("标签所有属性",a.attrs)
print("标签文本内容",a.text)