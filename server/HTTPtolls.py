"""
name:
date:
description
"""
from abc import abstractmethod
import json
import logging

OK = 200
METHOD_NOT_ALLOWED = 405
BAD_REQUEST = 400
NOT_FOUND = 404
UNAUTHORIZED = 401
UNEXPECTED_ENTITY = 442
INTERNAL_ERROR = 500
USERNAME = 'username'
PASS = 'password'
PROGRAM = 'program_id'
AUTENTICATION = 'Autentication'
QUESTION = 'auto_question'

class Responce(object):

    @classmethod
    def validate_erors(cls, code):
        """
        get the request and the response code and bild the response package

        :param int code: the responce status code
        :return: the response
        :rtype str:
        """
        if code == BAD_REQUEST:
            responce = cls.bad_request()
        elif code == NOT_FOUND:
            responce = cls.not_found()
        elif code == UNAUTHORIZED:
            responce = cls.unauthorized()
        elif code == UNEXPECTED_ENTITY:
            responce = cls.unexpected_entity('unknoen')
        elif code == METHOD_NOT_ALLOWED:
            responce = cls.method_not_allowed('unknoen')
        elif code == INTERNAL_ERROR:
            responce = cls.internal_eror()
        else:
            logging.critical('code {0} is not valid'.format(code))
            responce = cls.bad_request()
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
    def internal_eror():
        s = ""
        s += "HTTP/1.1 500 INTERNAL SERVER EROR\r\n"
        s += "\r\n"
        return s

    @staticmethod
    def unauthorized(header=''):
        s = ''
        s += "HTTP/1.1 401 UNAUTHORIZED\r\n"
        s+= header
        s+= '\r\n'
        s += '\r\n'
        return s

    @staticmethod
    def unexpected_entity(data=None):
        s = ''
        s += "HTTP/1.1 442 UNEXPECTED ENTITY\r\n"
        if data is not None:
            data = json.dumps(data)
            s += 'Content-Type: application/json\r\n'
            s += 'Content-Length: {0}\r\n'.format(len(data))
            s += '\r\n'
            s += data
        s += "\r\n"
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
    METODES = NotImplemented

    def __init__(self, request):
        """
        :param Request request: the request to handle
        """
        self.request = request

    @classmethod
    def is_uri(cls, uri):
        return cls.URI.match(uri)

    def handle_request(self):
        metode = self.request.get_verb()
        try:
            if metode == 'GET':
                return self.GET()
            elif metode == 'PATCH':
                return self.PATCH()
            elif metode == 'POST':
                return self.POST()
            elif metode == 'DELETE':
                return self.DELETE()
            else:
                return self.not_found()
        except NotImplementedError as err:
            return self.method_not_allowed()


    def method_not_allowed(self):
        s = ''
        s += "HTTP/1.1 405 NOT FOUND\r\n"
        s+= 'Allow:' + ' '.join(self.METODES) + '\r\n'
        s += "\r\n"
        return s

    def GET(self):
        raise NotImplementedError

    def PATCH(self):
        raise NotImplementedError

    def POST(self):
        raise NotImplementedError

    def DELETE(self):
        raise NotImplementedError
