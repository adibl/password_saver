"""
name:
date:
description
"""
import validate

def handle_client(data):
    """
    :param data: the client request
    :return: the needed responce
    """
    data = data.replace('\r\n', '\n')
    code = validate.validate_request(data)
    if code == validate.OK:
        responce = prosses_request(data)
    elif code == validate.BAD_REQUEST:
        responce = bad_request(data)
    elif code == validate.METHOD_NOT_ALLOWED:
        responce = method_not_allowed(data)
    elif code == validate.NOT_FOUND:
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
        validate.URI_PREMITED_LIST[validate.get_URI(request)]) + '\r\n'
    s += '\r\n'
    return s


def bad_request(request):
    s = ""
    s += "HTTP/1.1 400 BAD REQUEST\r\n"
    s += "\r\n"
    return s
