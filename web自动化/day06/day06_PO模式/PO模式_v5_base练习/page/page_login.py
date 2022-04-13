from web自动化.day06.day06_PO模式.PO模式_v5_base练习.base.base import Base
from web自动化.day06.day06_PO模式.PO模式_v5_base练习 import page

class PageLogin(Base):

    # 点击登录链接
    def page_click_login(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.login_username,username)

    # 输入密码
    def page_input_password(self,password):
        self.base_input(page.login_pwd,password)

    # 输入验证码
    def page_input_verify_code(self,code):
        self.base_input(page.login_verify_code,code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取提示文本信息
    def page_get_error_info(self):
        return self.base_get_text(page.login_err_info)

    # 点击异常信息框  确定
    def page_click_error_btn(self):
        self.base_click(page.login_err_btn_ok)

    # 截图
    def page_get_screenshot(self):
        self.base_get_image()

    # 组装业务方法
    def page_login(self,username,password,code):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_verify_code(code)
        self.page_click_login_btn()