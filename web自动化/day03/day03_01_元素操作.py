"""
元素操作常用方法
    1. click() 单击元素
    2. send_keys(value) 模拟输入
    3. clear() 清除文本  谨记 在一个页面输入过一次内容后 如果想要再次输入内容 一定要执行清空命令
"""
"""
案例模拟：
    需求：打开注册A页面，完成以下操作
        1).通过脚本执行输入用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com
        2).间隔3秒，修改电话号码为：18600000000
        3).间隔3秒，点击‘注册’按钮
        4).间隔3秒，关闭浏览器
        5).元素定位方法不限
"""

# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
driver=webdriver.Firefox()

# 打开url
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

# 1).通过脚本执行输入用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com
driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
driver.find_element_by_css_selector(".telA").send_keys("18611111111")
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")

# 2).间隔3秒，修改电话号码为：18600000000
sleep(3)
driver.find_element_by_css_selector(".telA").clear()  #clear()方法 清空文本内容  若不清空直接输入 会在原内容追加
driver.find_element_by_css_selector(".telA").send_keys("18600000000")

# 3).间隔3秒，点击‘注册’按钮
sleep(3)
driver.find_element_by_css_selector('[title="加入会员A"]').click()

# 4).间隔3秒，关闭浏览器驱动对象
sleep(3)
driver.quit()