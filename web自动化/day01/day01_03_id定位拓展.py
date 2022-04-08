#导包
from selenium import webdriver
from time import sleep
# 获取浏览器对象
driver=webdriver.Firefox()
#打开url
# 注意\在pycharm是转义字符
url=r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)
# 查找元素 用户名 并输入admin
driver.find_element_by_id("userA").send_keys("admin")
# 查找元素 密码 并输入123456
driver.find_element_by_id("passwordA").send_keys("123456")
# 暂停3秒
sleep(3)
# 关闭浏览器驱动对象
driver.quit()