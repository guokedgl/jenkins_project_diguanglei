from selenium.webdriver.common.by import By

# 设置数据：
# 放大镜
page_setting_search = By.XPATH, "//*[@content-desc='搜索']"

# 搜索输入框
page_setting_input_box = By.XPATH, "//*[@text='搜索…']"

# 返回键（收起）
page_setting_return = By.XPATH, "//*[@content-desc='收起']"
