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
显式与隐式区别
1. 作用域：隐式为全局元素，显式等待为单个元素有效
2. 使用方法：隐式等待直接通过驱动对象调用，而显式等待方法封装在WebDriverWait类中
3. 达到最大超时时长后抛出的异常不同：隐式为NoSuchElementException，显式等待为TimeoutException
"""

# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
driver=webdriver.Firefox()
# 将浏览器最大化
driver.maximize_window()
# 设置隐式等待  10秒
driver.implicitly_wait(10)

# 打开url
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

# 目标：隐式等待使用
# 给一个错误id 不能找到，如果直接抛出异常，说明等待失效，如果在设置的指定时长外抛出异常，说明等待生效
driver.find_element_by_css_selector("#user")

# 4).间隔3秒，关闭浏览器驱动对象
sleep(3)
driver.quit()