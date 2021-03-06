"""
name:
date:
description
"""
import base64
import json
import os

import requests
from .connection import Request


class Login(object):
    FILE_NAME = 'token.txt'

    @classmethod
    def handle(cls, username, password):
        return cls.GET(username, password)

    @classmethod
    def GET(cls, username, password):
        auto = base64.b64encode(username + ':' + password)
        responce = conn = Request().get_conn().get(Request.URI + '/login', headers={'Authorization': 'Basic {0}'.format(auto)}, )
        if responce.status_code == 200:
            cls.save_jwt_in_file(responce.text)
            return True
        elif responce.status_code == 442:
            return {'general': 'wrong username or password'}
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
