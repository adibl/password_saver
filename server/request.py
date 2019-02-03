"""
name:
date:
description
"""
import re
import logging
from server.HTTPtolls import *


class Request(object):
    RE_URI = re.compile(r"^(GET|PUT|POST|PUTCH|DELETE) ((/\w+)+)(\?\w+=\w+(&\w+=\w+)*)? (HTTP/1.1|HTTP/1.0)")
    RE_CONTENT_TYPE = re.compile("Content-Type: (application/json|application/xml)", re.M)


    def __init__(self, data):
        self.request = data

    @classmethod
    def validate(clt, request):
        if clt.__validate_request_line(request) and clt.__validate_content_type(request):
            return OK
        else:
            logging.debug('general validation failed')
            return BAD_REQUEST

    @classmethod
    def __validate_request_line(clt, request):
        """
        validate the URI structure
        :param str request: the client request
        :return: True if the structure is valid, False otherwise
        """
        return bool(clt.RE_URI.search(request))

    @classmethod
    def __validate_content_type(clt, request):
        """
        validate the request content type is existing an matching
        :param str request: the client request
        :return: True if request have valid content type, False otherwise
        """
        return bool(clt.RE_CONTENT_TYPE.search(request))

    def get_URI(self):
        """
        get the request URL
        :param str request: the client request
        :return: the request URI
        :rtype: str
        """
        return self.RE_URI.search(self.request).group(2)

    def get_verb(self):
        """
        return the http verb of the request
        :param str request: the client request
        :return: the client request HTTP verb
        :rtype: str
        """
        return self.RE_URI.search(self.request).group(1)