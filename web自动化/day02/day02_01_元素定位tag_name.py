"""
tag_name定位
说明：tag_name定位就是通过标签名来定位；
    HTML本质就是由不同的tag组成，每一种标签一般在页面中会存在多个，所以不方便进行精确定位，一般很少使用
tag_name (了解)
    说明：是通过元素的标签名称来定位，标签名(查看元素时尖括号(<)紧挨着的单词或字母就是标签名)  (标签名也就是元素名)
    方法：driver.find_element_by_tag_name("标签名")
    注意：如果页面中存在多个相同标签，默认返回第一个标签元素。
"""
"""
需求：打开注册A.html页面，完成以下操作
    1).使用tag_name定位用户名输入框，并输入：admin
    2).3秒后关闭浏览器窗口
"""
# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 打开url
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

# 使用tag_name定位用户名 输入admin
# 注意页面中如果存在多个相同的标签名称，默认返回第一个
driver.find_element_by_tag_name("input").send_keys("admin")

# 暂停三秒
sleep(3)

# 关闭浏览器驱动
driver.quit()