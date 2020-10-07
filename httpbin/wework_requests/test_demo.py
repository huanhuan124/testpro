
import requests

class Test_demo:

    def test_getaccesstoken(self):

        #企业微信每一个功能都有一个单独的secret，要想使用企业微信api，必须先获得access_token
        contacts_secret = 'Pt8SBjBFzFLR-_iq9BxRtk47jw7ayhlmgk567ecCKZ0'
        companyID = 'wwed0f3dc9f8233774'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='+companyID+'&corpsecret='+contacts_secret

        r = requests.get(url)
        print(r.json()['access_token'])
        return r.json()['access_token']

    def test_getuser(self):
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.test_getaccesstoken()}&userid=a124")
        print(r.json())

    def test_post_createuser(self):
        data = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "13718984826",
            "department": [1],
        }
        # access_token = self.test_getaccesstoken()
        # print(access_token)
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_getaccesstoken()}",json=data)
        print(r.json())