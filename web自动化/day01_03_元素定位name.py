# 导包
from selenium import webdriver
from time import sleep
# 获取浏览器对象
driver=webdriver.Firefox()
# 打开url
driver.get(r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html")
# 查找用户名 输入admin
driver.find_element_by_name("userA").send_keys("admin")
# 查找密码 输入 123456
driver.find_element_by_name("passwordA").send_keys("123456")
# 等待3秒
sleep(3)
# 关闭浏览器驱动
driver.quit()