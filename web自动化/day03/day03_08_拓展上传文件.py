# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
driver=webdriver.Firefox()

# 打开url
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

# 错误的实现
# driver.find_element_by_css_selector("[name='upfilea']").click()

#正确实现，使用send_keys("文件路径及文件名")
driver.find_element_by_css_selector("[name='upfilea']").send_keys("C:\接口自动化.txt")

# 4).间隔3秒，关闭浏览器驱动对象
sleep(3)
driver.quit()