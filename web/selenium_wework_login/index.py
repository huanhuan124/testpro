from time import sleep

from selenium import webdriver

from web.selenium_wework_login.login import Login
from web.selenium_wework_login.register import Register


class Index:

    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get("https://work.weixin.qq.com/")
        sleep(2)

    def goto_login(self):
        #click login
        self._driver.find_element_by_css_selector(".index_top_operation_loginBtn").click()

        return Login(self._driver)

    def goto_register(self):
        #click register   index_head_info_pCDownloadBtn
        self._driver.find_element_by_css_selector(".index_head_info_pCDownloadBtn").click()

        return Register(self._driver)