"""
什么是验证码？
    一种随机生成信息(文字、数字、图片)
验证码作用 ：   防止恶意请求
说明：Selenium中并没有对验证码处理的方法，在这里我们介绍一下针对验证码的几种常用处理方式
方式：
1). 去掉验证码    (测试环境下-采用)
2). 设置万能验证码   (生产环境和测试环境下-采用)
3). 验证码识别技术    (通过Python-tesseract来识别图片类型验证码；识别率很难达到100%)
4). 记录cookie   (通过记录cookie进行跳过登录)
提示
    1. 去掉验证码、设置万能验证码：都是开发来完成，我们在这里不做讲解
    2. 验证码识别技术：成功率不高，验证码种类繁多，不太适合
    3. 记录cookie：比较实用
cookie 介绍：
    1. Cookie是由Web服务器生成的，并且保存在用户浏览器上的小文本文件，它可以包含用户相关的信息。
    2. Cookie数据格式：键值对组成（python中的字典）
    3. Cookie产生：客户端请求服务器，如果服务器需要记录该用户状态，就向客户端浏览器颁发一个Cookie数据
    4. Cookie使用：当浏览器再次请求该网站时，浏览器把请求的数据和Cookie数据一同提交给服务器，服务器检
方法：
    1. driver.get_cookies() # 获取所有的cookie       get_cookie(name)  获取指定cookie
    2. driver.add_cookies({字典}) # 设置cookie     add_cookie({name="",value=""})
步骤：
    1. 打开百度url driver.get("http://www.baidu.com")
    2. 设置cookie信息： driver.add_cookie({"name":"BDUSS","value":"根据实际情况编写"})
    3. 暂停2秒以上
    4. 刷新操作
注意：
    1. 以上百度BDUSS所需格式为百度网站特有，别的网站请自行测试。
    2. 必须进行刷新操作。
"""
# 1、导包
import time
from time import sleep
from selenium import webdriver


# 2、获取浏览器驱动对象
driver = webdriver.Firefox()

# 最大化浏览器页面
driver.maximize_window()

# 设置隐式等待  30秒
driver.implicitly_wait(30)

# 打开URL
url = r"http://www.baidu.com/"
driver.get(url)
# 设置cookie信息
driver.add_cookie({"name":"BDUSS","value":"UNJNC1KVWFMQXkwazRrTXgxTkhXVnJTZGQtQ1VxUFpCekRLMXl3U0tsMy1JWHRpRUFBQUFBJCQAAAAAAAAAAAEAAAAtvMlXx-W7tvPPxM~DzgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP6UU2L-lFNiT"})

sleep(2)
# 刷新，必需刷新才能看到效果
driver.refresh()
"""
需求：使用cookie实现跳过登录
1). 手动登录百度，获取cookie
2). 使用获取到的cookie，达到登录目的，然后就可以执行登录之后的操作
"""

# 获取所有cookie信息
cookies = driver.get_cookies()
print(cookies)

# 获取指定cookie信息
cookie = driver.get_cookie("BDUSS")
print(cookie)

sleep(2)
# 关闭浏览器驱动对象
driver.quit()