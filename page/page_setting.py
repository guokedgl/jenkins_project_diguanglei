import page
from base.base import Base


class PageSetting(Base):
    # 点击放大镜
    def page_click_search(self):
        self.base_click(page.page_setting_search)

    # 搜索框输入内容
    def page_input_search_box(self, value):
        self.base_input(page.page_setting_input_box, value)

    # 点击收起
    def page_click_return(self):
        self.base_click(page.page_setting_return)

    # 组合方法
    def page_setting(self, value):
        self.page_click_search()
        self.page_input_search_box(value)
        self.page_click_return()
