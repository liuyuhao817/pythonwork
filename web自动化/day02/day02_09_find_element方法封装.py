"""
目标：find_element()
    driver.find_element(By.xxx, 'value')
参数说明：
    By.xxx :为By类的类型 如：By.ID
    value: 元素的定位值 如： "userA"
案例演示 需求：
    1、使用driver.find_element()方法
    2、输入用户名，admin
    3、输入密码 123456
"""

# 导包
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 打开url
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

# driver.find_element_by_id()
# driver.find_element_by_xxx他们的底层都是用了driver.find_element()
# 使用find_element()定位用户名
driver.find_element(By.ID,"userA").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,"#passwordA").send_keys("123456")

# 暂停
sleep(1)

# 关闭浏览器驱动
driver.quit()
