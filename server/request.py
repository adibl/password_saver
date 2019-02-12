"""
name:
date:
description
"""
import re
import logging
from server.HTTPtolls import *
import json
from urlparse import parse_qs

#BaseHTTPRequestHandler
class Request(object):
    RE_URI = re.compile(r"^(GET|PUT|POST|PATCH|DELETE) ((/\w+)+)(\?\w+=\w+(&\w+=\w+)*)? (HTTP/1.1|HTTP/1.0)")
    RE_CONTENT_TYPE = re.compile("Content-Type: (application/x-www-form-urlencoded)", re.M)
    RE_DATA = re.compile("\n(.*)$")


    def __init__(self, data):
        self.request = data

    @classmethod
    def validate(clt, request): #FIXME: add content type validation
        if clt.__validate_request_line(request):
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

    def get_data_as_dictionery(self):
        """
        return the request data as dictionary
        :return dict: the request data
        """
        data = self.RE_DATA.search(self.request).group(1)
        if data is '':
            return None
        else:
            return parse_qs(data)
