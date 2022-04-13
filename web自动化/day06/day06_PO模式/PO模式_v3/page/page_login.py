"""
页面对象层
页面对象编写技巧
    类名：使用大驼峰将模块名抄进来，有下划线去掉下划线
    方法：根据业务需求，每个操作步骤单独封装一个方法
        方法名 page_xxx
"""
from selenium import webdriver


class PageLogin:
    def __init__(self):
        # 获取driver对象
        self.driver = webdriver.Firefox()

        # 最大化浏览器
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(30)

        # 打开URL
        self.driver.get("http://127.0.0.1/")

    # 点击登录连接
    def page_click_login_link(self):
        self.driver.find_element_by_partial_link_text("登录").click()

    # 输入用户名
    def page_input_username(self,username):
        self.driver.find_element_by_css_selector("#username").send_keys(username)

    # 输入密码
    def page_input_pwd(self,password):
        self.driver.find_element_by_css_selector("#password").send_keys(password)

    # 输入验证码
    def page_input_verify_code(self,code):
        self.driver.find_element_by_css_selector("#verify_code").send_keys(code)

    # 点击登录
    def page_click_login_btn(self):
        self.driver.find_element_by_partial_link_text("登    录").click()

    # 获取异常消息
    def page_get_text(self):
        return self.driver.find_element_by_css_selector(".layui-layer-content").text

    # 点击提示框确定按钮
    def page_click_err_btn_ok(self):
        self.driver.find_element_by_css_selector(".layui-layer-btn0").click()

    # 组装登录业务方法 给业务层调用
    def page_login(self,username,password,code):
        self.page_click_login_link()
        self.page_input_username(username)
        self.page_input_pwd(password)
        self.page_input_verify_code(code)
        self.page_click_login_btn()
        self.page_click_login_btn()