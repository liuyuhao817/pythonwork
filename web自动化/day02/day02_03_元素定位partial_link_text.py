"""
说明：partial_link_text定位是对link_text定位的补充，link_text使用全部文本内容匹配元素，
    而partial_link_text可以使用局部来匹配元素，也可以使用全部文本内容匹配元素。
partial_link_text定位方法
    element = driver.find_element_by_partial_link_text(partial_link_text)
partial_link_text：可以传入a标签局部文本-能表达唯一性
注意：
    1. 可以使用精准或模糊匹配，如果使用模糊匹配最好使用能代表唯一的关键词
    2. 如果有多个值，默认返回第一个值
"""

"""
案例
需求：打开注册A.html页面，完成以下操作
    1).使用partial_link_text定位(访问 新浪 网站)超链接，并点击
    2).3秒后关闭浏览器窗口
"""
# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 打开url
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

# 使用partial_link_text定位访问新浪网址
# 点击方法为 clink
driver.find_element_by_partial_link_text("访问 新浪 网站").click()

# 暂停三秒
sleep(3)

# 关闭浏览器驱动
driver.quit()