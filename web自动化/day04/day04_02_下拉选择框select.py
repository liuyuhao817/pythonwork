"""
 Select类        说明：Select类是Selenium为操作select标签特殊封装的。
实例化对象：
    select = Select(element)         element: <select>标签对应的元素，通过元素定位方式获取，
如何使用Select类
操作：
    1. 导包：from  selenium.webdriver.support.select import Select
    2. 实例化：s = Select(element)
    3. 调用方法：s.select_by_index()
提供哪些方法
    1. select_by_index() # 通过下标定位
    2. select_by_value() # 通过value值
    3. select_by_visible_text() #显示文本
注意事项
    1. 实例化select时，需要的参数为 select标签元素
    2. 调用Select类下面的方法，是通过索引、value属性值、显示文本去控制，而不需要click事件
"""
# 1、导包
from time import sleep
from selenium import webdriver


# 2、获取浏览器驱动对象
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()

# 最大化浏览器页面
driver.maximize_window()

# 设置隐式等待  5秒
driver.implicitly_wait(5)

# 打开URL
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

"""
目标：使用select类实现操作option选择
需求
    暂停2秒
    1、定位上海
    2、暂停2秒
    3、定位广州
"""
e1 = driver.find_element_by_css_selector("#selectA")
# sleep(2)
"""# # 通过下标 切换到上海"""
# Select(e1).select_by_index(1)

"""# 通过value值形式访问"""
# # 通过Select引用对象
# sel = Select(e1)
# # 切换上海
# sel.select_by_value("sh")
# sleep(2)
# # 切换广州
# sel.select_by_value("gz")

"""通过 显示文本切换"""
sleep(2)
# 通过Select引用对象
sel = Select(e1)
# 切换上海
sel.select_by_visible_text("A上海")
sleep(2)
# 切换广州
sel.select_by_visible_text("A广州")


sleep(2)
# 关闭浏览器驱动对象
driver.quit()
