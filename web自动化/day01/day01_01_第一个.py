# selenium下载  pip install selenium
# 查看  pip show selenium  卸载   pip uninstall selenium

# 导包
from selenium import webdriver
import time
# 创建浏览器驱动对象    我只能用火狐，因为其他的没装驱动
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver = webdriver.Edge()
# 加载web页面
driver.get("http://www.baidu.com/")
# 暂停3秒
time.sleep(3)
# 关闭驱动对象
driver.quit()

# 导包
# from selenium import webdriver
# 获取浏览器驱动对象
# driver = webdriver.Firefox()
# 最大化网页
# driver.maximize_window()
# 隐式等待：当打开一个页面查找元素时，可能会因为各种原因无法第一时间找到该元素
# 这时设置一个等待时间，在这个时间内程序会持续对该元素进行查找，而不会立即报告异常
# 当在指定时间内还没找到所需元素时，程序才会报告异常，该等待是面向全体元素的。
# driver.implicitly_wait(30)
#
# url = "www.baidu.com"
# 加载web网页
# driver.get(url)
# 关闭浏览器驱动对象
# driver.quit()