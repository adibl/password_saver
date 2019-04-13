"""
name:
date:
description
"""
import base64

import requests
import json
from client.window_order import fsm

URI = 'http://127.0.0.1:50007'

class Login(object):

    @classmethod
    def handle(cls, username, password):
        return cls.GET(username, password)


    @classmethod
    def GET(cls, username, password):
        auto = base64.b64encode(username + ':' + password)
        responce = requests.get(URI + '/login', headers={'Authorization': 'Basic {0}'.format(auto)},)
        if responce.status_code == 200:
            fsm.logedin()
            return True
        elif responce.status_code == 442:
            return json.loads(responce.text)
        else:
            return {'general': 'general error'}