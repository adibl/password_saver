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

class Login(object):
    FILE_NAME = 'token.txt'

    @classmethod
    def handle(cls, username, password):
        return cls.GET(username, password)


    @classmethod
    def GET(cls, username, password):
        auto = base64.b64encode(username + ':' + password)
        responce = requests.get(URI + '/login', headers={'Authorization': 'Basic {0}'.format(auto)},)
        if responce.status_code == 200:
            cls.save_jwt_in_file(responce.text)
            fsm.logedin()
            return True
        elif responce.status_code == 442:
            return json.loads(responce.text)
        else:
            return {'general': 'general error'}

    @classmethod
    def save_jwt_in_file(cls, body):
        data = json.loads(body)
        JWT = data['Autentication']
        try:
            os.remove(cls.FILE_NAME)
        except OSError:
            pass
        with open(cls.FILE_NAME, 'wb')as handle:
            handle.write(JWT)



