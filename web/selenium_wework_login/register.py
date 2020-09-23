from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Register:

    def __init__(self,driver:WebDriver):
        self._driver = driver

    def register(self):
        sleep(2)
        self._driver.find_element_by_id("corp_name").send_keys("abc")
        sleep(2)
        self._driver.quit()

        # self._driver.find_element_by_id().send_keys()
