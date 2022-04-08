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
