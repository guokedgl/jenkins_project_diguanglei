from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import BaseDriver


class Base:
    # 初始化方法
    def __init__(self):
        self.driver = BaseDriver.get_driver()

    # 查找
    def base_find(self, loc, timeout=20, poll=0.2):
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击
    def base_click(self,loc):
        self.base_find(loc).click()

    # 输入
    def base_input(self,loc,value):
        self.base_find(loc).send_keys(value)
