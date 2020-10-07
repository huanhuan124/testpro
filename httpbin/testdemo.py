import requests
from jsonpath import jsonpath
from hamcrest import *
from requests.auth import HTTPBasicAuth

class Testdemo:

    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.cookies)
        assert r.status_code == 200

    def test_get_params(self):
        payload = {
            'name' : 'first',
            'age' : 12
        }
        r = requests.get("http://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post(self):
        dt = {
            'name':'second',
            'age':10
        }
        r = requests.post('http://httpbin.testing-studio.com/post', data=dt)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        header = {'h':"this is header test"}
        r = requests.get('http://httpbin.testing-studio.com/get',headers = header)
        print(r.text)
        print(type(r.text))
        print(r.json())
        print(type(r.json()))
        assert r.json()['headers']['H'] == "this is header test"

    def test_json(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.json()['category_list']['categories'][0]['name'])
        print(jsonpath(r.json(),'$..name')[0])
        assert jsonpath(r.json(),'$..name')[0] == '社区治理'
        assert_that(jsonpath(r.json(),'$..name')[1], equal_to('开源项目'))

    def test_coookie_byheaders(self):
        url = 'http://httpbin.testing-studio.com/cookies'
        header = {'Cookies':'zenghuan', 'User-Agent': 'python-requests/20201006'}
        r=requests.get(url, headers = header)
        print(r.request.headers)

    def test_cookie_bycookies(self):
        url = 'http://httpbin.testing-studio.com/cookies'
        header = {'User-Agent': 'python-requests/20201006'}
        cookie_data = {'teacher': 'AD', 'school': 'hgwz'}
        r = requests.get(url, headers=header,cookies = cookie_data)
        print(r.request.headers)


    def test_auth(self):
        url = 'http://httpbin.testing-studio.com/basic-auth/apple/12345'
        r =requests.get(url=url, auth = HTTPBasicAuth("apple",'12345'))
        print(r.text)
        print(r.content)
