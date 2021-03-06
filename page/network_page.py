import os,sys

from base.base_action import BaseAction

sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By

class NetWork(BaseAction):
    # 点击更多
    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    # 点击移动网络
    mobile_network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    # 点击首选网络类型
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    # 点击2g
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    # 点击3g
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def click_more(self):
        self.click(self.more_button)

    def click_network(self):
        self.click(self.mobile_network_button)

    def click_frist_button(self):
        self.click(self.first_network_button)

    def click_2g(self):
        self.click(self.network_2g_button)

    def click_3g(self):
        self.click(self.network_3g_button)

