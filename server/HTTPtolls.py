"""
name:
date:
description
"""
from abc import abstractmethod
import json
URI_PREMITED_LIST = {"/client/try": ["GET", "POST"]} # TODO: add security level to premited actions

OK = 200
METHOD_NOT_ALLOWED = 405
BAD_REQUEST = 400
NOT_FOUND = 404
UNAUTHORIZED = 401
USERNAME = 'username'
PASS = 'password'
PROGRAM = 'program_id'

class Responce(object):

    @classmethod
    def validate_erors(self, code):
        """
        get the request and the response code and bild the response package
        :param int code: the responce status code
        :param string data: the request
        :return int : the response
        """
        if code == BAD_REQUEST:
            responce = self.bad_request()
        elif code == NOT_FOUND:
            responce = self.not_found()
        elif code == UNAUTHORIZED:
            responce = self.unauthorized()
        else:
            responce = self.bad_request()
        return responce

    @staticmethod
    def not_found():
        s = ''
        s += "HTTP/1.1 404 NOT FOUND\r\n"
        s += "\r\n"
        return s

    @staticmethod
    def ok(data=None):
        s = ''
        s += "HTTP/1.1 200 OK\r\n"
        if data is not None:
            data = json.dumps(data)
            s += 'Content-Type: application/json\r\n'
            s += 'Content-Length: {0}\r\n'.format(len(data))
            s += '\r\n'
            s += data
        s += "\r\n"
        return s

    @staticmethod
    def bad_request():
        s = ""
        s += "HTTP/1.1 400 BAD REQUEST\r\n"
        s += "\r\n"
        return s

    @staticmethod
    def unauthorized():
        s = ''
        s += "HTTP/1.1 401 UNAUTHORIZED\r\n"
        s += '\r\n'
        return s

    @abstractmethod
    def handle_request(self):
        pass

    @abstractmethod
    def method_not_allowed(self):
        pass

    @abstractmethod
    def prosses_request(self):
        pass


class Uri(Responce):
    URI = NotImplemented #re compiled
    def __init__(self, request):
        """
        :param ResorceRequest request:
        """
        self.request = request

    @classmethod
    def is_uri(cls, uri):
        return cls.URI.match(uri)
