from selenium import webdriver
from selenium.webdriver.common.by import By

from web.po.firstpo.test_hgwz import Test_hgwz

class Test_main():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")

    def teardown(self):
        self.driver.quit()

    def sendkeys(self):
        self.driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("霍格沃兹学院")


        self.driver.find_element(By.CSS_SELECTOR, "#su").click()


    def click_first_link(self):
        #click
        self.driver.find_element_by_xpath('*[ @ id = "menu-item-679"] / a')


        return Test_hgwz()


