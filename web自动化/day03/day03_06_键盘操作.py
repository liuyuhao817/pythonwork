"""
常用的键盘操作
1. send_keys(Keys.BACK_SPACE) 删除键(BackSpace)
2. send_keys(Keys.SPACE) 空格键(Space)
3. send_keys(Keys.TAB) 制表键(Tab)
4. send_keys(Keys.ESCAPE) 回退键(Esc)
5. send_keys(Keys.ENTER) 回车键(Enter)
6. send_keys(Keys.CONTROL,'a') 全选(Ctrl+A)
7. send_keys(Keys.CONTROL,'c') 复制(Ctrl+C)
键盘对应的方法在Keys类中
导包：from selenium.webdriver.common.keys import Keys
常用的快捷键：  CONTROL：Ctrl键
组合键：element.send_keys(Keys.XXX, 'a')
单键：element.send_keys(Keys.XXX)
"""
"""
需求：打开注册A页面，完成以下操作
    # 1). 输入用户名：admin1，暂停2秒，删除1
    # 2). 全选用户名：admin，暂停2秒
    # 3). 复制用户名：admin，暂停2秒
    # 4). 粘贴到密码框
"""
# 导包
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
# 获取浏览器驱动对象
driver=webdriver.Firefox()
# 将浏览器最大化
driver.maximize_window()
# 打开url
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

# 1). 输入用户名：admin1，暂停2秒，删除1
username = driver.find_element_by_css_selector("#userA")
username.send_keys("admin1")
sleep(1)

username.send_keys(Keys.BACK_SPACE)

# 2). 全选用户名：admin，暂停2秒
username.send_keys(Keys.CONTROL,"a")
sleep(2)
# 3). 复制用户名：admin，暂停2秒
username.send_keys(Keys.CONTROL,"c")
# 4). 粘贴到密码框
driver.find_element_by_css_selector("#passwordA").send_keys(Keys.CONTROL,"v")

# 间隔3秒，关闭浏览器驱动对象
sleep(3)
driver.quit()