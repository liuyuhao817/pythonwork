"""
1. CSS（Cascading Style Sheets）是一种语言，它用来描述HTML元素的显示样式；
2. 在CSS中，选择器是一种模式，用于选择需要添加样式的元素；
3. 在Selenium中也可以使用这种选择器来定位元素。
提示：
    1. 在selenium中推荐使用CSS定位，因为它比XPath定位速度要快
    2. css选择器语法非常强大，在这里我们只学习在测试中常用的几个
CSS定位方法:
    element = driver.find_element_by_css_selector(css_selector)
CSS常用定位方法
    1. id选择器  前提：元素是必须有id属性   语法：#id  如：#passwordA
    2. class选择器  前提：元素是必须有class属性  语法：.class  如：.telA
    3. 元素选择器  语法：element  如：input
    4. 属性选择器  语法：[属性名=属性值]
    5. 层级选择器  语法： 1. p>input    2. p input   提示：>与空格的区别，大于号必须为子元素，空格则不用。
扩展：
    1. [属性^='开头的字母'] # 获取指定属性以指定字母开头的元素
    2. [属性$='结束的字母'] # 获取指定属性以指定字母结束的元素
    3. [属性*='包含的字母'] # 获取指定属性包含指定字母的元素
"""
# class 用 .class属性值 id用 #id属性值  其余属性直接用[属性名=='属性值']  元素用元素名 直接写就行 层级 不需要写/ 直接写元素名 元素名
"""
案例需求：
    # 1、使用id选择器 定位用户名，输入admin
    # 2、使用属性选择器，定位密码框 输入123456
    # 3、使用class选择器 定位电话号码 18611111111
    # 4、使用元素选择器  定位span 获取文本值
    # 5、使用层级选择器  定位email 输入123@qq.com
"""
# 导包
from selenium import webdriver
from time import sleep

# 获取浏览器驱动对象
driver=webdriver.Firefox()

# 打开url
url = r"D:\python_heima_shipk\软件测试\二\8天web自动化全套测试—资料\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

# 1、使用id选择器 定位用户名，输入admin
driver.find_element_by_css_selector("#userA").send_keys("admin")
sleep(1)
# 2、使用属性选择器，定位密码框 输入123456
driver.find_element_by_css_selector("[id='passwordA']").send_keys("123456")
sleep(1)
# 3、使用class选择器 定位电话号码 18611111111
driver.find_element_by_css_selector(".telA").send_keys("18611111111")
sleep(1)
# 4、使用元素选择器  定位span 获取文本值     获取文本值方法 元素.text  写入内容send_keys()  点击 click()
span_text=driver.find_element_by_css_selector("span").text
sleep(1)
print(f"获取{span_text}成功")
# 5、使用层级选择器  定位email 输入123@qq.com
driver.find_element_by_css_selector("p>input#emailA").send_keys("123@qq.com")
sleep(1)

# 关闭浏览器驱动
driver.quit()

