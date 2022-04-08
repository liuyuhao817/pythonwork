"""
为什么要设置元素等待
    由于电脑配置或网络原因，在查找元素时，元素代码未在第一时间内被加载出来，而抛出未找到元素异常。
什么是元素等待
    元素在第一次未找到时，元素等待设置的时长被激活，如果在设置的有效时长内找到元素，继续执行代码，如果超出设置的时长未找打元素，抛出未找到元素异常。
元素等待分类  1. 隐式等待  2. 显示等待
隐式等待   方法：driver.implicitly_wait(30) # 一般情况下设置30秒
    特色：1. 针对所有元素生效。2. 一般情况下为前置必写代码(1.获取浏览器驱动对象；2. 最大化浏览器；3. 设置隐式等待)
显示等待
方法：WebDriverWait(driver,timeout=10, poll_frequency=0.5).until(lambda x:x.find_element_by_id("#user")).send_keys("admin")
参数：timeout: 超时时间   poll_frequency:访问频率，默认0.5秒找一次元素
    x: x为driver,它是WebDriverWait类将传入的driver赋值给类self._driver，until方法调用了self._driver;
提示：
WebDriverWait(driver,timeout=10, poll_frequency=0.5).until(lambda x:x.find_element_by_id("#user"))返回的一个元素。
显示等待与隐式等待区别：1. 显示等待：针对单个元素生效    2. 隐式等待：针对全局元素生效
"""

# 导包
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
# 获取浏览器驱动对象
driver=webdriver.Firefox()
# 将浏览器最大化
driver.maximize_window()
# # 设置隐式等待  10秒
# driver.implicitly_wait(10)

# 打开url
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

"""
目标：显式等待的使用
操作：1、导包 WebDriverWait()类
     2、实例化WebDriverWait()类并调用until(method)方法
     method ：匿名函数
     lambda x:x.find_element_by_id()
"""
#实例化WebDriverWait()并调用until(method)方法
# 调用until方法返回的必是一个元素
el=WebDriverWait(driver,timeout=10,poll_frequency=0.5).until(lambda x:x.find_element_by_id("#user"))
# 输入值
el.send_keys("admin")

# 4).间隔3秒，关闭浏览器驱动对象
sleep(3)
driver.quit()