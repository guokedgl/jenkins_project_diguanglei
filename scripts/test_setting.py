import pytest

from base.base_driver import BaseDriver
from page.page_setting import PageSetting
from tools.read_setting_yaml import read_setting
import time


class TestSetting:
    def setup(self):
        self.driver = BaseDriver.get_driver()
        self.setting = PageSetting()

        time.sleep(1)

    def teardown(self):
        BaseDriver.quit_driver()

    @pytest.mark.parametrize("args", read_setting("page_setting_data", "test_setting"))
    def test_setting(self, args):
        self.setting.page_setting(args["name"])
