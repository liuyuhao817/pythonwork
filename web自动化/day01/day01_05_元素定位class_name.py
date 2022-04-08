# 导包
from selenium import webdriver
from time import sleep
# 获取浏览器对象
driver=webdriver.Firefox()
# 打开url
driver.get(r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html")
# 查找电话号码  输入18611111111
driver.find_element_by_class_name("telA").send_keys("18611111111")
# 查找邮箱 输入123@qq.com
driver.find_element_by_id("emailA").send_keys("123@qq.com")
# 等待三秒
sleep(3)
# 关闭浏览器驱动
driver.quit()