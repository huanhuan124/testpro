import time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options


class Test_remote:


    def setup(self):
        # 复用浏览器
        options = Options()
        options.debugger_address = "127.0.0.1:9225"
        self.driver = webdriver.Chrome(options=options)

    def test_fuyong_browser_weibo(self):

        # #复用浏览器
        # options = Options()
        # options.debugger_address="127.0.0.1:9225"
        # self.driver = webdriver.Chrome(options=options)

        # 1、首先在终端里面打开chrome的调试状态chrome  --remote-debugging-port=9222  端口可以随意指定，打开后会自动启动Chrome浏览器
        # 2、在浏览器输入目标URL，比如微博，然后登录
        # 3、这时候如果复用了浏览器就不需要再次登录，可以做其他的操作

        self.driver.find_element_by_xpath('//*[@id="plc_top"]/div/div/div[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="pl_feedtop_top"]/div[2]/div/input').clear()

        self.driver.find_element_by_xpath('//*[@id="pl_feedtop_top"]/div[2]/div/input').send_keys('糖葫芦')
        self.driver.find_element_by_xpath('//*[@id="pl_feedtop_top"]/div[2]/button').click()
        time.sleep(2)

        # / Applications


    def test_fuyong_browser_WeCom(self):
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        time.sleep(2)



