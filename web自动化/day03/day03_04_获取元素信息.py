"""
获取元素信息的常用方法
    1. size 返回元素大小
    2. text 获取元素的文本
    3. get_attribute("xxx") 获取属性值，传递的参数为元素的属性名
    4. is_displayed() 判断元素是否可见
    5. is_enabled() 判断元素是否可用
    6. is_selected() 判断元素是否选中，用来检查复选框或单选按钮是否被选中
提示：
    1. size、text：为属性，调用时无括号；如：xxx.siz
    2、get_attribute一般应用场景：判断一组元素是否为想要的元素或者判断元素属性值是否正确
    3. is_displayed、is_enabled、is_selected，在特殊应用场景中使用
"""
"""
需求：使用‘注册A.html’页面，完成以下操作：
    # 1).获取用户名输入框的大小
    # 2).获取页面上第一个超链接的文本内容
    # 3).获取页面上第一个超链接的地址
    # 4).判断页面中的span标签是否可见
    # 5).判断页面中取消按钮是否可用
    # 6).判断页面中'旅游'对应的复选框是否为选中的状态
"""
# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
driver=webdriver.Firefox()
# 将浏览器最大化
driver.maximize_window()
# 打开url
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册实例.html"
driver.get(url)
# 1).获取用户名输入框的大小
size = driver.find_element_by_css_selector("#user").size
print(f"用户名大小为：{size}")
# 2).获取页面上第一个超链接的文本内容
text = driver.find_element_by_css_selector("a").text
print(f"页面的第一个a标签的文本内容为{text}")
# 3).获取页面上第一个超链接的地址
attribute = driver.find_element_by_css_selector("a").get_attribute("href")
print(f"页面的第一个超链接地址{attribute}")
# 4).判断页面中的span标签是否可见
display = driver.find_element_by_css_selector("span").is_displayed()
print(f"span元素是否可见：{display}")
# 5).判断页面中取消按钮是否可用
enabled = driver.find_element_by_css_selector("#cancel").is_enabled()
print(f"取消按钮是否可用：{enabled}")
# 选中旅游按钮
driver.find_element_by_css_selector("#ly").click()
# 6).判断页面中'旅游'对应的复选框是否为选中的状态
selected = driver.find_element_by_css_selector("#ly").is_selected()
print(f"旅游复选框是否被选中：{selected}")

# 间隔3秒，关闭浏览器驱动对象
sleep(3)
driver.quit()