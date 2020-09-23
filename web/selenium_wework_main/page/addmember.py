from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Addmember:

    def __init__(self,driver:WebDriver):
        self._driver = driver

    def addmember(self):
        sleep(3)
        self._driver.find_element_by_id("username").send_keys("abe")

        self._driver.find_element_by_id("memberAdd_acctid").send_keys("a125")
        self._driver.find_element_by_id("memberAdd_phone").send_keys("13100001113")
        self._driver.find_element_by_xpath('//*[@id="js_contacts54"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        # self._driver.find_element_by_css_selector("js_btn_save").click()
        sleep(2)
        # return True

    def get_member(self):
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(2)
        list = []
        elements = self._driver.find_elements_by_css_selector('.member_colRight_memberTable_td:nth-child(2)')
        for element in elements:
            list.append(element.get_attribute("title"))
        return list