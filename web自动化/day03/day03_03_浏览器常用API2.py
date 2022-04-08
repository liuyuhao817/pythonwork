"""
操作浏览器常用方法
    1. maximize_window() 最大化浏览器窗口 --> 模拟浏览器最大化按钮
    2. set_window_size(width, height) 设置浏览器窗口大小 --> 设置浏览器宽、高(像素点)
    3. set_window_position(x, y) 设置浏览器窗口位置 --> 设置浏览器位置
    4. back() 后退 --> 模拟浏览器后退按钮
    5. forward() 前进 --> 模拟浏览器前进按钮
    6. refresh() 刷新 --> 模拟浏览器F5刷新
    7. close() 关闭当前窗口 --> 模拟点击浏览器关闭按钮
    8. quit() 关闭浏览器驱动对象 --> 关闭所有程序启动的窗口
    9. title 获取页面title
    10. current_url 获取当前页面URL
提示:
    1. driver.title 和 driver.current_url 没有括号，应用场景：一般为判断上步操作是否执行成功。
    2. driver.maximize_window() # 一般为我的前置代码，在获取driver后，直接编写最大化浏览器
    3. driver.refresh() 应用场景，在后面的cookie章节会使用到。
    4. driver.close()与driver.quit()区别：
        close():关闭当前主窗口
        quit():关闭由driver对象启动的所有窗口
        提示：如果当前只有1个窗口，close与quit没有任何区别。
"""
# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
driver=webdriver.Firefox()

# 打开url
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册实例.html"
driver.get(url)
# 将浏览器最大化
driver.maximize_window()

# 输入用户名admin 目的：刷新完成--清空
driver.find_element_by_css_selector("#user").send_keys("admin")
# 暂停2秒
sleep(2)
# 刷新
driver.refresh()
# 获取title
title = driver.title
print(f"当前页面的title是{title}")
# 获取当前url
current_url = driver.current_url
print(f"当前页面的url地址为{current_url}")
# 点击注册A网页 打开新窗口
driver.find_element_by_partial_link_text("注册A网页").click()
# 暂停3秒
sleep(3)
# 关闭主窗口
driver.close()
# 间隔3秒，关闭浏览器驱动对象
sleep(3)
driver.quit()
