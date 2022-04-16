from web自动化.day08.TPshop import page
from web自动化.day08.TPshop.base.base import Base


class PageLogin(Base):

    #点击登录链接
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(page.login_pwd, password)

    # 输入验证码
    def page_input_verify_code(self, verify_code):
        self.base_input(page.login_verify_code, verify_code)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    #获取异常提示信息
    def page_get_error_info(self):
        return self.base_get_text(page.login_err_info)

    #点击异常提示信息 确定
    def page_click_error_info_btn(self):
        self.base_click(page.login_err_btn_ok)

    #截图
    def page_get_screenshot(self):
        self.base_get_image()

    #点击安全退出
    def page_click_logout_btn(self):
        self.base_click(page.login_logout)

    #判断是否退出成功
    def page_is_logout_success(self):
        self.base_element_is_exist(page.login_link)

    #组装业务方法
    def page_login(self,username,password,verify_code):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_verify_code(verify_code)
        self.page_click_login_btn()