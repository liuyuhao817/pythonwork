"""
元素定位：要使用web自动化操作元素，必须先找到这个元素
元素定位依赖于  标签名 属性 层级 路径
所有定位的前提都是元素都必须有这个属性
定位方法：
    1、id
    2、name
    3、class_name（使用元素的class属性定位）
    4、teg_name（标签名称<标签名..../>）
    5、link_text（定位超链接a标签）
    6、partial_link_text（定位超链接a标签模糊）
    7、xpath（基于元素定位）
    8、css（元素选择器）
        提示：
            id: 一般为唯一标识符。
            name:可以重名
            class:多个命名。
1. 基于元素属性特有定位方式(id\name\class_name)
2. 基于元素标签名称定位：tag_name
3. 定位超链接文本(link_text、partial_link_text)
4. 基于元素路径定位(xpath)
5. 基于选择器(css)
"""

from selenium import webdriver
from time import sleep
#获取浏览器对象  获取火狐浏览器驱动对象
driver = webdriver.Firefox()
#打开url
# 注意\在pycharm是转义字符
url=r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)
#查找用户名元素
username=driver.find_element_by_id("userA")
#查找密码元素
password=driver.find_element_by_id("passwordA")
#用户名输入admin       输入方法：send_keys("输入内容")
username.send_keys("admin")
#密码输入123456
password.send_keys("123456")

sleep(3)

driver.quit()


"""
1、导包
2、获取浏览器驱动
3、打开url
4、查找用户元素
5、输入
6、关闭驱动
"""
