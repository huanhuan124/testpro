from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

from web.base import Base


class TestAlert(Base):

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(2)
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(2)