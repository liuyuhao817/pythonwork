"""
find_elements_by_xxx()
作用：
    1). 查找定位所有符合条件的元素
    2). 返回的定位元素格式为数组(列表)格式；
说明 : 列表数据格式的读取需要指定下标(下标从0开始)  可遍历
4.2 案例
需求：打开注册A.html页面，完成以下操作
    1).使用tag_name定位密码输入框(第二个input标签)，并输入：123456
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
# 使用elements 可以实现找到指定位置的元素 返回结果：类型为列表，要对列表进行访问和操作必须指定下标或进行遍历，[下标从0开始]
driver.find_elements_by_tag_name("input")[1].send_keys("123456")

# 暂停三秒
sleep(3)

# 关闭浏览器驱动
driver.quit()

