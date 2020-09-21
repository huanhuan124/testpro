import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Test_cookies:


    # 先通过浏览器复用，拿到cookie存到cookies这个变量中，然后去掉浏览器复用，访问页面，把之前拿到cookie存到driver的cookie中
    # 再次访问页面，就可以自动登录
    def test_cookies(self):
        # 复用浏览器
        options = Options()
        options.debugger_address = "127.0.0.1:9225"
        #1
        # self.driver = webdriver.Chrome(options=options)
        #2 获取到cookie后在使用
        self.driver = webdriver.Chrome()
        # self.driver.get("https://work.weixin.qq.com/")
        print("1111111111")
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'T9TJEIcIeZlZdqE5_JLl8sz_Jd4dBa_i8HLEezgq7RylbdEFF9h_nSNmh1wLiGIgH9dSplB3LSS0ORY5ZlUamISacf25CGJ4ca23L347DmW2LTvyJMYxYnJMGi-QtcbHFt9UWyteOfYoQwFggPosYagSEwuEG6eF36Nh426okJmlJDAcIKtTHQVUZnWTtJLiRK5S9hNi0nMaTF8pWZGnbK1tPeaovtbvS29_6qsqupNTVCcekIx3hI_EL2PmBBDkc-M6mIFJHnwYCS18sj-jyQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'cJ_PGjqjYNtoEnJMNxJHZcZbsLEYFwU6ZQ0KZHx_hsu1k46fA2IMMX-6UQ4rEI63'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a513203'},
            {'domain': '.qq.com', 'expiry': 1600693651, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1603203979, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1603203979, 'httpOnly': False, 'name': 'wwrtx.i18n_lan_custom',
             'path': '/', 'secure': False, 'value': 'true'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851952704535'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851952704535'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325052164674'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1632229591, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1600609090,1600610369,1600610419'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1600693591'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '018819'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1600725126, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '87btsj3'},
            {'domain': '.qq.com', 'expiry': 1600780008, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1994764444.1600608321'},
            {'domain': '.qq.com', 'expiry': 1663765608, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1298625341.1600608321'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1632144319, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'}]

        # print(self.driver.get_cookies())
        # shelve

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(2)
        self.driver.quit()



    def test_shelev_cookies(self):
         # 复用浏览器
         options = Options()
         options.debugger_address = "127.0.0.1:9225"
         # 1
         # self.driver = webdriver.Chrome(options=options)
         # 2 获取到cookie后在使用
         self.driver = webdriver.Chrome()


         self.driver.get("https://work.weixin.qq.com/")
         db = shelve.open("cookies")
         # db['cookie'] = self.driver.get_cookies()

         cookies = db['cookie']

         for cookie in cookies:
             if "expiry" in cookie.keys():
                 cookie.pop("expiry")
             self.driver.add_cookie(cookie)

         self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
         sleep(2)
         db.close()
         self.driver.quit()

