"""
Xpath 和 Css 定位
为什么使用Xpath和css定位？
    1. id,name,class：依赖于元素这三个对应的属性，如果元素没有以上三个属性，定位方法不能使用。
    2. link_text,partial_link_text：只适合超链接
    3. tag_name:只能找页面唯一元素，或者 页面中多个相同元素中的第一个元素
什么是Xpath定位？
    说明：基于元素的路径
xpath介绍
    xpath是XML  Path简称 (xml是一种标记语言，焦点：数据存储于传递(配置文件) 后缀.XML)
Xpath常用的定位策略：
    1. 路径
        1). 绝对路径：语法：以单斜杠开头逐级开始编写，不能跳级。如：/html/body/div/p[1]/input
        2). 相对路径  语法：以双斜杠开头，双斜杠后边跟元素名称，不知元素名称可以使用*代替。 如： //input //*
    2. 路径结合属性
        语法：在Xpath中，所有的属性必须使用@符号修饰 如：//*[@id='id值']
    3. 路径结合逻辑(多个属性)
        语法：//*[@id="id值" and @属性='属性值']
    4. 路径结合层级
        语法：//*[@id='父级id属性值']/input
提示：
    1. 一般见识使用指定标签名称，不使用*代替，效率比较慢。
    2. 无论是绝对路径和相对路径，/后面必须为元素的名称或者*
    3. 扩展：在工作中，如果能使用相对路径绝对不使用绝对路径。
"""
"""
练习
需求：打开注册A.html页面，完成以下操作
    1).使用绝对路径定位用户名输入框，并输入：admin
    2).暂停2秒
    3).使用相对路径定位用户名输入框，并输入：123
"""
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
driver=webdriver.Firefox()

# 打开url
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

# 使用相对路径定位用户名输入框，并输入：admin
driver.find_element_by_xpath("//p[@id='p1']/input").send_keys("admin")
# 暂停2秒
sleep(2)
# 使用相对路径定位用户名输入框，并输入：123
driver.find_element_by_xpath("//input[@id='passwordA']").send_keys("123456")

# 暂停三秒
sleep(3)

# 关闭浏览器驱动对象
driver.quit()