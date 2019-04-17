
import base64

import requests
import json
from client.window_order import fsm
import os
URI = 'http://127.0.0.1:50007'


class Record(object):
    FILE_NAME = 'token.txt'


    @classmethod
    def GET(cls, url):
        auto = cls.read_jwt()
        encode_url =base64.urlsafe_b64encode(url)
        responce = requests.get(URI + '/passwords/' + encode_url, headers={'Authorization': 'Bearer {0}'.format(auto)})
        if responce.status_code == 200:
            return json.loads(responce.text)
        else:
            return {'general': 'general error'}

    @classmethod
    def PATCH(cls, url, **kargs):
        auto = cls.read_jwt()
        encode_url = base64.urlsafe_b64encode(url)
        responce = requests.patch(URI + '/passwords/' + encode_url, headers={'Authorization': 'Bearer {0}'.format(auto)},
                                json=kargs)
        if responce.status_code == 200:
            return True
        else:
            return {'general': 'general error'}

    @classmethod
    def read_jwt(cls):
        with open(cls.FILE_NAME, 'rb')as handel:
            jwt = handel.read()
        return jwt