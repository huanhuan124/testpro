from selenium.webdriver.common.by import By

__author__ = 'zenghuan'

from selenium import webdriver

class TestSelenium:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.get("https://www.baidu.com/")
        #隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_selenium(self):
        self.driver.get("https://www.testerhome.com/")
        # time.sleep(1)
        self.driver.find_element_by_link_text("社团").click()
        #直接等待
        # time.sleep(1)
        #显示等待
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,'//*[@class="media-heading"]')) >= 1
        # WebDriverWait(self.driver,10).until(wait)


        self.driver.find_element_by_link_text("求职面试圈").click()
        # time.sleep(1)
        print("hello,succ")

    def testElementByID(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID,"kw").send_keys("霍格沃兹学院")
        self.driver.find_element(By.ID,"su").click()

    def testElementByXPATH(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹学院")
        self.driver.find_element(By.XPATH,'//*[@id="su"]').click()

    def testElementByCssSelector(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("霍格沃兹学院")
        self.driver.find_element(By.CSS_SELECTOR,"#su").click()


    # def test_po_hgwz(self):
    #     main = Test_main()
    #
    #     main.sendkeys()
    #     time.sleep(2)
    #     main.click_first_link()
    #     time.sleep(3)
    #     main.click_first_link().get_text()
    #     time.sleep(2)
