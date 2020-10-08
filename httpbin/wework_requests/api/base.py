import requests
from requests import request


class Base:


    def send(self,data):
        # request('get', url, params=params, **kwargs)
        return requests.request(**data)
