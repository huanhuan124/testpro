import os

from selenium import webdriver


class Base():

    # def __init__(self):
    #     self.driver = None

    def setup(self):

        # 运用多浏览器时，提示找不到driver？？？？未找到原因
        # browser = os.getenv("browser")
        # # self.driver = None
        #
        # if browser == 'firefox':
        #     self.driver = webdriver.Firefox()
        #
        # elif browser == 'chrome':
        #     print("chrome^^^^^^^^^^^^^^^^^^")
        #     self.driver == webdriver.Chrome()
        #     print(self.driver)


        self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()