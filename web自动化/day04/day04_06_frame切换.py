"""
提示：常用的frame表单有两种：frame、iframe
为什么要切换？
    当前主目录内没有iframe表单页面元素信息，不切换，找不到元素。
如何切换？   切换到指定frame的方法
    方法：driver.switch_to.frame("id\name\element")
为什么要回到主目录           即 主--》A--》主--》B才行
    iframe或frame只有在主目录才有相关元素信息，不回到主目录，切换语句会报错。
如何回到主目录   恢复默认页面方法
    方法：driver.switch_to.default_content()
提示：  切换frame时，可以使用name、id、iframe元素
"""
# 1、导包
from time import sleep
from selenium import webdriver


# 2、获取浏览器驱动对象
driver = webdriver.Firefox()

# 最大化浏览器页面
driver.maximize_window()

# 设置隐式等待  30秒
driver.implicitly_wait(30)

# 打开URL
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册实例.html"
driver.get(url)

"""
案例：打开‘注册实例.html’页面，完成以下操作
    1). 填写主页面的注册信息
    2). 填写注册页面A中的注册信息
    3). 填写注册页面B中的注册信息
"""
"""填写主页面"""
# 用户名
driver.find_element_by_css_selector("#user").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#password").send_keys("123456")
# 电话
driver.find_element_by_css_selector(".tel").send_keys("18611111111")
# 邮件
driver.find_element_by_css_selector("#email").send_keys("123@qq.com")

"""填写注册A"""
# 切换到frameA
driver.switch_to.frame("myframe1")
# 用户名
driver.find_element_by_css_selector("#userA").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
# 电话
driver.find_element_by_css_selector(".telA").send_keys("18611111111")
# 邮件
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")

"""填写注册B"""
# 恢复默认页面  即回到主目录
driver.switch_to.default_content()
# 切换到frameB
driver.switch_to.frame("myframe2")
# 用户名
driver.find_element_by_css_selector("#userB").send_keys("admin")
# 密码
driver.find_element_by_css_selector("#passwordB").send_keys("123456")
# 电话
driver.find_element_by_css_selector(".telB").send_keys("18611111111")
# 邮件
driver.find_element_by_css_selector("#emailB").send_keys("123@qq.com")

sleep(2)
# 关闭浏览器驱动对象
driver.quit()