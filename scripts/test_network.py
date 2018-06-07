import os,sys
sys.path.append(os.getcwd())

from page.network_page import NetWork
from base.base_driver import init_driver


class TestNetwork:

    def setup(self):
        self.driver = init_driver()
        self.networkpage = NetWork(self.driver)


    def test_mobile_network_2g(self):
        self.networkpage.click_more()
        self.networkpage.click_network()
        self.networkpage.click_frist_button()
        self.networkpage.click_2g()


    def test_mobile_network_3g(self):
        self.networkpage.click_more()
        self.networkpage.click_network()
        self.networkpage.click_frist_button()
        self.networkpage.click_3g()

   def test_mobile_network_3g(self):

        self.networkpage.click_more()

        self.networkpage.click_network()

        self.networkpage.click_frist_button()

        self.networkpage.click_3g()
