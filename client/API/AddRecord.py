"""
name:
date:
description
"""
import base64
import json
import requests
import os
from .connection import Request

class Passwords(object):
    FILE_NAME = 'token.txt'

    @classmethod
    def handle(cls, url, username, password):
        return cls.POST(url, username, password)

    @classmethod
    def GET(cls):
        auto = cls.read_jwt()
        if auto is None:
            return {'general': 401}
        responce = conn = Request().get_conn().get(Request.URI + '/passwords', headers={'Authorization': 'Bearer {0}'.format(auto)})
        if responce.status_code == 200:
            return json.loads(responce.text)
        else:
            return {'general': responce.status_code}

    @classmethod
    def POST(cls, url, username, password):
        auto = cls.read_jwt()
        if auto is None:
            return {'general': 401}
        print base64.urlsafe_b64encode(url)
        encode_url = base64.urlsafe_b64encode(url)
        responce = conn = Request().get_conn().post(Request.URI + '/passwords', headers={'Authorization': 'Bearer {0}'.format(auto)}
                                 , json={'username': username, 'password': password,
                                         'program_id': encode_url})
        if responce.status_code == 200:
            return True
        elif responce.status_code == 442:
            return json.loads(responce.text)
        else:
            return {'general': 'general error'}

    @classmethod
    def read_jwt(cls):
        if os.path.isfile(cls.FILE_NAME):
            with open(cls.FILE_NAME, 'rb')as handel:
                jwt = handel.read()
            return jwt
        else:
            return None
