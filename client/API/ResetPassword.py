"""
name:
date:
description
"""
import base64
import json

import requests
from .connection import Request


class ForgotPassword(object):

    @classmethod
    def handle(cls, username):
        return cls.GET(username)

    @classmethod
    def GET(cls, username):
        responce = conn = Request().get_conn().get(Request.URI + '/reset', json={'username': username})
        if responce.status_code == 200:
            data = json.loads(responce.text)
            if 'question' in data:
                return True, data['question']
            else:
                return False, {'general': 'general error'}
        elif responce.status_code == 442:
            return False, json.loads(responce.text)
        else:
            return False, {'general': 'general error'}

    @classmethod
    def PATCH(cls, username, answer, new_username=None, new_password=None):
        d = {"username": username, 'answer': answer}
        if not new_password in [None, '']:
            d['NewPassword'] = new_password
        if not new_username in [None, '']:
            d['NewUsername'] = new_username
        responce = conn = Request().get_conn().patch(Request.URI + '/reset',json=d)
        if responce.status_code == 200:
            return True
        elif responce.status_code == 442:
            return json.loads(responce.text)
        else:
            return {'general': 'general error'}
