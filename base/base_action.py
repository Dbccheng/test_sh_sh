from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.driver.find_element(loc[0], loc[1]).click()

    def input(self, loc, text):
        self.driver.find_element(loc[0], loc[1]).send_keys(text)


    def find_element(self,loc):
        WebDriverWait(self,5,1).until(lambda x:x.find_element(loc[0], loc[1]))

