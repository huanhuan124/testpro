import random
import re
import pytest
import requests
from filelock import FileLock


class Test_demo:

    #获取access_token
    @pytest.fixture(scope="session")
    def test_getaccesstoken(self):
        r = None

        # 使用锁的时候，并行执行一直卡住？？？？
        # while FileLock("session.lock"):
        # 企业微信每一个功能都有一个单独的secret，要想使用企业微信api，必须先获得access_token
        contacts_secret = 'Pt8SBjBFzFLR-_iq9BxRtk47jw7ayhlmgk567ecCKZ0'
        companyID = 'wwed0f3dc9f8233774'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + companyID + '&corpsecret=' + contacts_secret

        r = requests.get(url)
        print("test_gettoken")
        # print(r.json()['access_token'])
        return r.json()['access_token']

    #获取用户详情
    def test_getuser(self,userid,test_getaccesstoken):
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_getaccesstoken}&userid={userid}")
        print(r.json())
        return r.json()

    #创建用户
    def test_post_createuser(self,userid,name,mobile,test_getaccesstoken):
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": [1],
        }
        # access_token = test_getaccesstoken
        # print(access_token)
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_getaccesstoken}",json=data)
        print(r.json())
        return r.json()

    #更新用户
    def test_post_updateuser(self,userid,name,test_getaccesstoken):
        data = {
            'userid': userid,
            'name': name

        }

        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_getaccesstoken}", json=data)
        print(r.json())
        return r.json()

    #删除用户
    def test_get_deleteuser(self,userid,test_getaccesstoken):

        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_getaccesstoken}&userid={userid}")
        print(r.json())
        return r.json()


    #准备大量数据，这个不能和pytest-xdist并行一起使用，会报错，因为这些数据都是在间隔0.1s的时候产生的，并行的时候数据会重复
    def test_create_data(self):
        data = [(str(random.randint(0,9999)),'test'+str(random.randint(0,9999)),str(random.randint(13811110000,13811119999))) for x in range(10)]
        print(data)
        print(type(data))
        return data



    def test_create_data2(self):
        data = [("test" + str(x), "testxxx", "138%08d" % x) for x in range(10)]
        print(data)
        return data


    # @pytest.mark.parametrize(['userid','name', 'mobile'], [("zhangsan", "张三", "13718984822")])
    @pytest.mark.parametrize("userid, name, mobile", test_create_data2(self=""))
    def test_all(self,userid,name,mobile,test_getaccesstoken):

        #测试创建用户，异常处理意见存在当前要创建的用户或者手机号被占用
        try:

            assert 'created' == self.test_post_createuser(userid,name,mobile,test_getaccesstoken)['errmsg']
            assert name == self.test_getuser(userid,test_getaccesstoken)['name']
            # assert name == self.test_getuser(userid)['name']
        except AssertionError as e:
            # if self.test_post_createuser(userid,name,mobile)['errcode'] == '60104':

            if "mobile existed" in e.__str__():
                print("先删除")
                #如果手机号被使用了，找出使用的手机号的userid，进行删除
                # re_userid = re.findall(":(.*)'$",e.__str__())[0]
                re_userid = re.findall(":(.*)", e.__str__())[0]
                print("111111111",re_userid)
                if re_userid.endswith("'") or re_userid.endswith('"'):
                    re_userid = re_userid[:-1]
                    print("2222222", re_userid)
                    assert 'deleted' == self.test_get_deleteuser(re_userid,test_getaccesstoken)['errmsg']
                    assert 60111 == self.test_getuser(re_userid,test_getaccesstoken)['errcode']
                    assert 'created' == self.test_post_createuser(userid, name, mobile,test_getaccesstoken)['errmsg']
                    assert name == self.test_getuser(userid,test_getaccesstoken)['name']




        #测试更新用户
        # assert 'updated' == self.test_post_updateuser(userid,'张三2',test_getaccesstoken)['errmsg']
        # assert '张三2' == self.test_getuser(userid,test_getaccesstoken)['name']

        #测试删除用户
        # assert 'deleted' == self.test_get_deleteuser(userid,test_getaccesstoken)['errmsg']
        # assert 60111 == self.test_getuser(userid,test_getaccesstoken)['errcode']



