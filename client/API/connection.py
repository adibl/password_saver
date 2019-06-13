"""
name:
date:
description
"""
import sys
import requests
import ssl
if len(sys.argv) == 3:
    IP = sys.argv[1]
    PORT = sys.argv[2]
else:
    IP = '127.0.0.1'
    PORT = 50007
CERTIFICATION_PATH = r'certification.cert'

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