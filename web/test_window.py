from time import sleep

from web.base import Base


class Test_window(Base):

    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        self.driver.switch_to.window(self.driver.window_handles[-1])
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("test")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13201010202")
        self.driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("13201010202")
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[0])
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("test")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("123456")



