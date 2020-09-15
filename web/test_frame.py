from selenium import webdriver

from web.base import Base


class Test_Frame(Base):

    def testFrame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to_default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
