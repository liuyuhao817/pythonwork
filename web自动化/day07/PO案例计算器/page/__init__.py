"""以下为服务器域名地址"""
url = "http://cal.apple886.com/"

"""以下为计算器配置数据"""
from selenium.webdriver.common.by import By

# 由于数字键，有一定规律，所以暂时不用定位此键，用到时再考虑此键怎么解决
# clac_num = By.CSS_SELECTOR,"#simple9"

# 加号
clac_add = By.CSS_SELECTOR,"#simpleAdd"

# 等号
clac_eq = By.CSS_SELECTOR,"#simpleEqual"

# 获取结果
clac_result = By.CSS_SELECTOR,"#resultIpt"

# 清屏
clac_clear = By.CSS_SELECTOR,"#simpleClearAllBtn"