"""
name:
date:
description
"""
import re
from abc import ABCMeta

from server.HTTPtolls import *


class Request(object):
    RE_URI = re.compile(r"^(GET|PUT|POST|PATCH|DELETE) ((/[\w|=]+)+)(\?\w+=\w+(&\w+=\w+)*)? (HTTP/1.1|HTTP/1.0)")
    RE_CONTENT_TYPE = re.compile("Content-Type: (application/x-www-form-urlencoded)", re.M)
    RE_DATA = re.compile("\n(.*)$")

    def __init__(self, data):
        self.request = data

    @classmethod
    def validate(cls, request):  # FIXME: add content type validation
        if cls.__validate_request_line(request):
            return OK
        else:
            logging.debug('general validation failed')
            return BAD_REQUEST

    @classmethod
    def __validate_request_line(cls, request):
        """
        validate the URI structure
        :param str request: the client request
        :return: True if the structure is valid, False otherwise
        """
        return bool(cls.RE_URI.search(request))

    def __validate_content_type(self):
        """
        validate the request content type is existing an matching
        :param str request: the client request
        :return: True if request have valid content type, False otherwise
        """
        return bool(self.RE_CONTENT_TYPE.search(self.request))

    def get_URI(self):
        """
        get the request URL
        :return: the request URI
        :rtype: str
        """
        return self.RE_URI.search(self.request).group(2)

    def get_verb(self):
        """
        return the http verb of the request
        :return: the client request HTTP verb
        :rtype: str
        """
        return self.RE_URI.search(self.request).group(1)

    def get_data_as_dictionery(self):
        """
        return the request data as dictionary
        :return dict: the request data
        """
        data = self.RE_DATA.search(self.request).group(1)
        if data is '':
            return None
        else:
            return json.loads(data)


class AuthenticatedRequestScema(Request):
    __metaclass__ = ABCMeta
    RE_VALIDATE = None

    @classmethod
    def is_fit(cls, request):
        return cls.validate_Authentication(request)

    @classmethod
    def validate_Authentication(cls, request):
        """
        validate Autentication header structure
        :param str request: the client request
        :return: True if structure is valid, false otherwise
        """
        return bool(cls.RE_VALIDATE.search(request))

    @abstractmethod
    def get_user_id(self):
        """
        get the user id
        :return: user id
        :rtype: str
        """
