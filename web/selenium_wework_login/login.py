from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from web.selenium_wework_login.register import Register


class Login:


    def __init__(self,driver:WebDriver):
        self._driver = driver

    def goto_register(self):
        #click register
        self._driver.find_element_by_css_selector(".login_registerBar_link").click()
        return Register(self._driver)
        # pass

    def scan_login(self):
        pass