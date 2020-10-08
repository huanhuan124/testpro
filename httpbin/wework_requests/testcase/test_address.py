from httpbin.wework_requests.api.address import Address


class Test_address:

    def setup(self):
        self.address = Address()




    def test_getuser(self):

        assert 0 == self.address.getuser('zenghuan')['errcode']

    def test_post_createuser(self):

        assert 0 == self.address.post_createuser('a666','小六','13012123030')

    def test_post_updateuser(self):
        assert 0 == self.address.post_updateuser('a666','小六123','13012123030')

    def test_get_deleteuser(self):
        assert 0 == self.address.get_deleteuser('a666')
