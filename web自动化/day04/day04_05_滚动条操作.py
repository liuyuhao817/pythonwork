"""
为什么要操作滚动条
    在web自动化中有些特殊场景，如：滚动条拉倒最底层，指定按钮才可用。
如何操作
第一步：设置操作滚动条操作语句
    如：js = "window.scrollTo(0,10000)"
    0: 左边距 --》水平滚动条    10000：上边距 -->垂直滚动条
第二步：调用执行js方法，将设置js语句传入方法中
    方法：driver.execute_script(js)
说明：
    在selenium中没有直接提供定位滚动条组件方法，但是它提供了执行js语句方法，可以通过js语句来控制滚动条操作。
"""
# 1、导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
# 2、获取浏览器驱动对象
driver = webdriver.Firefox()

# 最大化浏览器页面
driver.maximize_window()

# 设置隐式等待  5秒
driver.implicitly_wait(5)

# 打开URL
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

"""
需求：打开注册页面A，暂停2秒后，滚动条拉到最底层
"""
sleep(2)
# 第一步 设置js控制滚动条语句
js = "window.scrollTo(0,10000)"
# 第二步 调用执行js语句方法
driver.execute_script(js)

sleep(2)
# 关闭浏览器驱动对象
driver.quit()
