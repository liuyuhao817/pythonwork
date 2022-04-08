#1、导入模块
from bs4 import BeautifulSoup
#2、创建beautifulsoup对象
#BeautifulSoup 作用：可以从html或xml中提取数据
#                      要解析的文档       指明解析器
soup = BeautifulSoup("<html>data<html>", "lxml")
print(soup)