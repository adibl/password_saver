"""
name:
date:
description
"""
import base64

import requests
import json
from client.window_order import fsm
import os
URI = 'http://127.0.0.1:50007'


class Passwords(object):
    FILE_NAME = 'token.txt'

    @classmethod
    def handle(cls, url, username, password):
        return cls.POST(url, username, password)


    @classmethod
    def POST(cls, url, username, password):
        auto = cls.read_jwt()
        print base64.urlsafe_b64encode(url)
        encode_url =base64.urlsafe_b64encode(url)
        responce = requests.post(URI + '/passwords', headers={'Authorization': 'Bearer {0}'.format(auto)}
                                , json={'username': username, 'password': password, 'program_id': encode_url}) #FIXME: encode
        if responce.status_code == 200:
            return True
        elif responce.status_code == 442:
            return json.loads(responce.text)
        else:
            return {'general': 'general error'}

    @classmethod
    def read_jwt(cls):
        with open(cls.FILE_NAME, 'rb')as handel:
            jwt = handel.read()
        return jwt
