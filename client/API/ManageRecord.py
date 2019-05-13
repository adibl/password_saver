import base64
import json

from .connection import Request


class Record(object):
    FILE_NAME = 'token.txt'

    @classmethod
    def GET(cls, url):
        auto = cls.read_jwt()
        encode_url = base64.urlsafe_b64encode(url)
        responce = conn = Request().get_conn().get(Request.URI + '/passwords/' + encode_url, headers={'Authorization': 'Bearer {0}'.format(auto)})
        if responce.status_code == 200:
            return json.loads(responce.text)
        else:
            return {'general': 'general error'}

    @classmethod
    def PATCH(cls, url, **kargs):
        auto = cls.read_jwt()
        encode_url = base64.urlsafe_b64encode(url)
        responce = conn = Request().get_conn().patch(Request.URI + '/passwords/' + encode_url,
                                  headers={'Authorization': 'Bearer {0}'.format(auto)},
                                  json=kargs)
        if responce.status_code == 200:
            return True
        else:
            return {'general': 'general error'}

    @classmethod
    def DELETE(cls, url):
        auto = cls.read_jwt()
        encode_url = base64.urlsafe_b64encode(url)
        responce = conn = Request().get_conn().delete(Request.URI + '/passwords/' + encode_url,
                                  headers={'Authorization': 'Bearer {0}'.format(auto)})
        if responce.status_code == 200:
            return True
        else:
            return {'general': 'general error'}

    @classmethod
    def read_jwt(cls):
        with open(cls.FILE_NAME, 'rb')as handel:
            jwt = handel.read()
        return jwt
