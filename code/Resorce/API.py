"""
name:
date:
description
"""
import __validate

import logging
from code import setup_logging
setup_logging()

def handle_client(data):
    """
    :param data:
    :return:
    """
    data = data.replace('\r\n', '\n')
    code = __validate.validate_request(data)
    if code == __validate.OK:
        responce = prosses_request(data)
    elif code == __validate.BAD_REQUEST:
        responce = bad_request(data)
    elif code == __validate.METHOD_NOT_ALLOWED:
        responce = method_not_allowed(data)
    elif code == __validate.NOT_FOUND:
        responce = not_found(data)
    else:
        responce = bad_request(data)
    return responce


def not_found(request):
    s = ''
    s += "HTTP/1.1 404 NOT FOUND\r\n"
    return s


def prosses_request(request):
    return "HTTP/1.1 200 OK\r\n\r\n"


def method_not_allowed(request):
    s = ''
    s += "HTTP/1.1 405 METHOD NOT ALLOWED\r\n"
    s += "Access-Control-Request-Method: " + " ".join(
        __validate.URI_PREMITED_LIST[__validate.get_URI(request)]) + '\r\n'
    s += '\r\n'
    return s


def bad_request(request):
    s = ""
    s += "HTTP/1.1 400 BAD REQUEST\r\n"
    s += "\r\n"
    return s
