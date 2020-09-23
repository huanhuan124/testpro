from web.selenium_wework_main.page.main import Main


class Test_addmember:

    def setup(self):
        self.main = Main()

    def test_addmember(self):
        # main = Main()
        self.main.goto_addmember().addmember()
        assert "abe" in self.main.goto_addmember().get_member()