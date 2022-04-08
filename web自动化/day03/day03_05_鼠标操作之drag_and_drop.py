"""
鼠标操作的方法
说明：在Selenium中将操作鼠标的方法封装在ActionChains类中
导包 from selenium.webdriver import ActionChains
实例化对象：
action = ActionChains(driver)
方法：
    1. context_click(element) 右击 --> 模拟鼠标右键点击效果
    2. double_click(element) 双击 --> 模拟鼠标双击效果
    3. drag_and_drop(source, target) 拖动 --> 模拟鼠标拖动效果
    4. move_to_element(element) 悬停 --> 模拟鼠标悬停效果
    5. perform() 执行 --> 此方法用来执行以上所有鼠标操作
为了
更好的学习其他方法，我们先学习perform()执行方法,因为所有的方法都需要执行才能生效
selenium框架中虽然提供了，右击鼠标方法，但是没有提供选择右击菜单方法，可以通过发送快捷键的方式解决(经测试，谷歌浏览器不支持)
"""
# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
from selenium.webdriver import ActionChains

driver=webdriver.Firefox()
# 将浏览器最大化
driver.maximize_window()
# 打开url
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\drop.html"
driver.get(url)

# 实例化并获取ActionChains
action = ActionChains(driver)
source = driver.find_element_by_css_selector("#div1")
target = driver.find_element_by_css_selector("#div2")
action.drag_and_drop(source,target).perform()

# 拓展  通过坐标偏移量执行
action.drag_and_drop_by_offset(source,xoffset=360,yoffset=180).perform()

# 间隔3秒，关闭浏览器驱动对象
sleep(3)
driver.quit()