"""
应用场景：失败截图，让错误看的更直观
方法：
    driver.get_screenshot_as_file(imagepath)
参数：
    imagepath：为图片要保存的目录地址及文件名称
如： 当前目录 ./test.png    上一级目录 ../test.png
扩展：
    1. 多条用例执行失败，会产生多张图片，可以采用时间戳的形式，进去区分。
操作：
    driver.get_screenshot_as_file("../image/%s.png"%(time.strftime("%Y_%m_%d %H_%M_%S")))
    strftime:将时间转为字符串函数
注意：	%Y_%m_%d %H_%M_%S：代表，年 月 日 时 分 秒
"""
# 1、导包
import time
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
需求：打开‘注册A.html’页面，完成以下操作
1). 填写注册信息
2). 截图保存
"""
current_handle = driver.current_window_handle
driver.find_element_by_partial_link_text("注册A网页").click()
handles = driver.window_handles
for handle in handles:
    if handle != current_handle:
        driver.switch_to.window(handle)
        driver.find_element_by_css_selector("#userA").send_keys("admin")
        # driver.get_screenshot_as_file("./admin.jpg")
        #动态获取文件名，使用时间戳
        driver.get_screenshot_as_file("./%s.jpg"%time.strftime("%Y_%m_%d %H_%M_%S"))
sleep(2)
# 关闭浏览器驱动对象
driver.quit()