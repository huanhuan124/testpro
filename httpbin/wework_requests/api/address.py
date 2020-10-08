import requests

from httpbin.wework_requests.api.base import Base


class Address(Base):

    def __init__(self):
        contacts_secret = 'Pt8SBjBFzFLR-_iq9BxRtk47jw7ayhlmgk567ecCKZ0'
        companyID = 'wwed0f3dc9f8233774'
        # url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + companyID + '&corpsecret=' + contacts_secret

        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": companyID,
                "corpsecret": contacts_secret
            }

        }

        self.access_token = self.send(data)



    # def getaccesstoken(self):
    #     r = None
    #
    #     # 使用锁的时候，并行执行一直卡住？？？？
    #     # while FileLock("session.lock"):
    #     # 企业微信每一个功能都有一个单独的secret，要想使用企业微信api，必须先获得access_token
    #     contacts_secret = 'Pt8SBjBFzFLR-_iq9BxRtk47jw7ayhlmgk567ecCKZ0'
    #     companyID = 'wwed0f3dc9f8233774'
    #     url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + companyID + '&corpsecret=' + contacts_secret
    #
    #     r = requests.get(url)
    #     print("test_gettoken")
    #     # print(r.json()['access_token'])
        return r.json()['access_token']

    # 创建用户
    def post_createuser(self, userid, name, mobile):
        # data = {
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile,
        #     "department": [1],
        # }
        # access_token = test_getaccesstoken
        # print(access_token)

        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {
                "access_token": self.access_token
            },
            "json":{
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1],
            }

        }

        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_getaccesstoken}",
        #                   json=data)

        return self.send(data).json()

    # 获取用户详情
    def getuser(self, userid):
        # request('get', url, params=params, **kwargs)
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_getaccesstoken}&userid={userid}")

        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "access_token": self.access_token,
                "userid": userid
            }

        }

        return self.send(data).json()


    #更新用户
    def post_updateuser(self,userid,name):

        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {
                "access_token": self.access_token
            },
            "json": {
                "userid": userid,
                "name": name
            }

        }


        return self.send(data).json()

    #删除用户
    def get_deleteuser(self,userid):

        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": self.access_token,
                "userid": userid
            }

        }


        return self.send(data).json()