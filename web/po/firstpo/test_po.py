import time

from web.po.firstpo.test_main import Test_main


class Test_po:

    #fail 提示找不到driver
    def testpo(self):
        main = Test_main()

        main.sendkeys()
        time.sleep(2)
        main.click_first_link()
        time.sleep(3)
        main.click_first_link().get_text()
        time.sleep(2)