import os,sys
sys.path.append(os.getcwd())

from page.display_page import DispalyPage

from base.base_driver import init_driver


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display_page = DispalyPage(self.driver)

    def test_mobile_display_input(self):
        self.display_page.click_search()
        self.display_page.input_text('hello')
        self.display_page.click_back()