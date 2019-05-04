"""
name:
date:
description
"""
import base64
import requests
from .connection import Request

class Delete(object):
    @classmethod
    def handle(cls, username, password):
        return cls.DELETE(username, password)

    @classmethod
    def DELETE(cls, username, password):
        auto = base64.b64encode(username + ':' + password)
        responce = conn = Request().get_conn().delete(Request.URI + '/delete', headers={'Authorization': 'Basic {0}'.format(auto)}, )
        if responce.status_code == 200:
            return True
        elif responce.status_code == 442:
            return {'general': 'wrong username or password'}
        else:
            return {'general': 'general error'}