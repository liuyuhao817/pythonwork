from selenium.webdriver.common.by import By

url = "http://127.0.0.1"

# 登录链接
login_link = (By.PARTIAL_LINK_TEXT,"登录")
# 用户名
login_username = By.ID,"username"
#密码
login_pwd = By.ID,"password"
# 验证码
login_verify_code = By.ID,"verify_code"
# 登录按钮
login_btn = By.PARTIAL_LINK_TEXT,"登    录"
# 获取异常文本信息
login_err_info = By.CSS_SELECTOR,".layui-layer-content"
# 点击异常提示框 按钮
login_err_btn_ok = By.CSS_SELECTOR,".layui-layer-btn0"
# 安全退出
login_logout = By.PARTIAL_LINK_TEXT,"安全退出"