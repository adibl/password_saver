"""
name:
date:
description
"""

import requests
import ssl


class Singleton(type):
    URI = 'https://192.168.0.109:50007'
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Request(object):
    __metaclass__ = Singleton
    def __init__(self):
        s = requests.Session()
        sertificate = ssl.get_server_certificate(('192.168.0.109', 50007), ssl_version=ssl.PROTOCOL_SSLv23)
        with open('cert.cert', 'wb') as handle:
            handle.write(sertificate)
    def get_conn(self):
        s = requests.Session()
        s.verify = r'D:\adi\Documents\password_saver\server\test_server\test_resorce_API\cert.cert'
        return s