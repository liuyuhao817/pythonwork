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
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

# 将浏览器最大化
driver.maximize_window()
# 暂停2秒
sleep(2)
# 设置固定大小 300,200
driver.set_window_size(300,200)
# 暂停2秒
sleep(2)
# 移动浏览器窗口位置 x：320 y：150
driver.set_window_position(320,150)
# 暂停2秒
sleep(2)
# 最大化
driver.maximize_window()
# 点击 访问新浪网站  注意：要演示后退功能，必须先执行打开新的网站
driver.find_element_by_partial_link_text("访问").click()
# 暂停2秒
sleep(2)
# 刷新当前页面
driver.refresh()
# 暂停2秒
sleep(2)
# 执行后退  ----》注册页面A
driver.back()
# 暂停2秒
sleep(2)
# 执行前进 ----》新浪   注意：前进必须放在后退操作后
driver.forward()
# 间隔3秒，关闭浏览器驱动对象
sleep(3)
driver.quit()
