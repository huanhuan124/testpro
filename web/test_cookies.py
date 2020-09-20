from selenium import webdriver
from selenium.webdriver.ie.options import Options


class Test_cookies:


    def test_cookies(self):
        # 复用浏览器
        options = Options()
        options.debugger_address = "127.0.0.1:9226"
        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://work.weixin.qq.com/")
        print("1111111111")
        print(self.driver.get_cookies())