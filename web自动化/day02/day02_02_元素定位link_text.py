"""
说明：link_text定位是专门用来定位超链接元素(<a>标签</a>)，并且是通过超链接的文本内容来定位元素
link_text定位方法
    element = driver.find_element_by_link_text(link_text)
    link_text：为超链接的全部文本内容
    注意：1link_text:只能使用精准匹配(a标签的全部文本内容)
"""

"""
案例
需求：打开注册A.html页面，完成以下操作
    1).使用link_text定位(访问 新浪 网站)超链接，并点击
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

# 使用link_text定位访问新浪网址   注意  这个是全部匹配 必须把a标签的文本内容写完整
# 点击方法为 clink
driver.find_element_by_link_text("访问 新浪 网站").click()

# 暂停三秒
sleep(3)

# 关闭浏览器驱动
driver.quit()