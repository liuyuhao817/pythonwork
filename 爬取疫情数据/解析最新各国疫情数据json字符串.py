#1、导入相关模块
import re
import requests
from bs4 import BeautifulSoup
import json

#2、发送请求，获取疫情首页内容
response = requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")
home_page = response.content.decode()
# print(home_page)

#3、使用beautifulsoup提取疫情数据
soup = BeautifulSoup(home_page,"lxml")
script = soup.find(id = "getListByCountryTypeService2true")
temt = script.text
# print(temt)

#4、使用正则表达式，提取json字符串
json_str = re.findall(r"\[.+\]",temt)[0]
# print(json_str)

#5、把json字符串转换为python类型的数据
last_day_corona_virus = json.loads(json_str)
print(last_day_corona_virus)