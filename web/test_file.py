

from selenium import webdriver
from time import sleep

from web.base import Base


class TestFile(Base):

    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys("/Users/zenghuan/workspace/python_workspace/testpro/pic/鸢尾花.jpeg")
        sleep(2)