"""
为什么要处理警告框？
    如果页面由弹出框，不处理，接下来的将不生效。
网页中常用的弹出框有三种
    1. alert 警告框
    2. confirm 确认框
    3. prompt 提示框
如何处理      以上三种对话框，处理方法都一样。
步骤：
    1. 切换到对话框
            方法：driver.switch_to.alert
    2. 处理对话框
            alert.text # 获取文本
            alert.accept() # 同意
            alert.dismiss() # 取消
提示：无论以上哪个对话框，都可以使用取消、同意，因为调用的是后台的事件，跟页面显示的按钮数量无关。
2.4 注意：
    1. driver.switch_to.alert 方法适合以上三种类型对话框，调用时没有括号
    2. 获取文本的方法，调用时没有括号 如：alert.text
    3. 在项目中不是所有的小窗口都是以上三种对话框。
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
需求：打开注册A.html页面，完成以下操作：
    1).点击 alert 按钮
    2).关闭警告框
    3).输入用户名：admin
"""
# 定位alert按钮，并点击
driver.find_element_by_css_selector("#alerta").click()
sleep(2)
# 如果页面由弹出框，不处理，接下来的将不生效
# 定位 用户名 输入admin
driver.find_element_by_css_selector("#userA")

sleep(2)
# 关闭浏览器驱动对象
driver.quit()
