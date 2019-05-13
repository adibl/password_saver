"""
name:
date:
description
"""

import requests
import ssl
IP = '127.0.0.1'
PORT = 50007
CERTIFICATION_PATH = r'D:\adi\Documents\password_saver\openssl\certification.cert'

class Singleton(type):
    URI = 'https://{0}:{1}'.format(IP, str(PORT))
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Request(object):
    __metaclass__ = Singleton
    def __init__(self):
        s = requests.Session()
        sertificate = ssl.get_server_certificate((IP, PORT), ssl_version=ssl.PROTOCOL_SSLv23)
        with open(CERTIFICATION_PATH, 'wb') as handle:
            handle.write(sertificate)

    def get_conn(self):
        s = requests.Session()
        s.verify = False
        return s