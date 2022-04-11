"""
为什么要切换多窗口？
    页面存在多个窗口式，selenium默认焦点只会在主窗口上所有的元素，不切换切换窗口，无法操作除主窗口以外的窗口内元素
如何切换？
    思路：获取要切换的窗口句柄，调用切换方法进行切换。
什么是句柄？
    操作系统在生成对象时分配给对象的唯一标识
方法：
    1. driver.current_window_handle # 获取当前主窗口句柄
    2. driver.window_handles # 获取当前由driver启动所有窗口句柄
    3. driver.switch_to.window(handle) # 切换窗口
步骤：
    1. 获取当前窗口句柄
    2. 点击链接 启动另一个窗口
    3. 获取当前所有窗口句柄
    4. 遍历所有窗口句柄
    5. 判断当前遍历的窗口句柄不等于当前窗口句柄
    6. 切换窗口操作
"""
# 1、导包
from time import sleep
from selenium import webdriver


# 2、获取浏览器驱动对象
driver = webdriver.Firefox()

# 最大化浏览器页面
driver.maximize_window()

# 设置隐式等待  5秒
driver.implicitly_wait(5)

# 打开URL
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册实例.html"
driver.get(url)

"""
需求：打开‘注册实例.html’页面，完成以下操作
    1). 点击‘注册A页面’链接
    2). 在打开的页面中，填写注册信息
"""

# 获取当前窗口句柄  ---》判断只要不是当前主窗口的句柄，就一定是新开的窗口句柄
current_handle = driver.current_window_handle
print("当前窗口句柄是：",current_handle)

# 点击注册A网页
driver.find_element_by_partial_link_text("注册A网页").click()

# 获取所有窗口句柄
handles = driver.window_handles
print("所有窗口句柄：",handles)

# 判断不是当前句柄，切换
for handle in handles:
    if handle != current_handle:
        #切换
        driver.switch_to.window(handle)
        """填写注册A"""
        # 用户名
        driver.find_element_by_css_selector("#userA").send_keys("admin")
        # 密码
        driver.find_element_by_css_selector("#passwordA").send_keys("123456")
        # 电话
        driver.find_element_by_css_selector(".telA").send_keys("18611111111")
        # 邮件
        driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")


sleep(2)
# 关闭浏览器驱动对象
driver.quit()