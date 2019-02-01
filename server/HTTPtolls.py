"""
name:
date:
description
"""
URI_PREMITED_LIST = {"/client/try": ["GET", "POST"]} # TODO: add security level to premited actions

OK = 200
METHOD_NOT_ALLOWED = 405
BAD_REQUEST = 400
NOT_FOUND = 404
UNAUTHORIZED = 401

def code_to_responce(code, data):
    if code == OK:
        responce = prosses_request(data)
    elif code == BAD_REQUEST:
        responce = bad_request(data)
    elif code == METHOD_NOT_ALLOWED:
        responce = method_not_allowed(data, ['get']) #FIXME: add secend parameter as neded
    elif code == NOT_FOUND:
        responce = not_found(data)
    else:
        responce = bad_request(data)
    return responce

def not_found(request):
    s = ''
    s += "HTTP/1.1 404 NOT FOUND\r\n"
    return s


def method_not_allowed(request, alooed_metodes):
    s = ''
    s += "HTTP/1.1 405 METHOD NOT ALLOWED\r\n"
    s += "Access-Control-Request-Method: " + " ".join(alooed_metodes) + '\r\n'
    s += '\r\n'
    return s


def bad_request(request):
    s = ""
    s += "HTTP/1.1 400 BAD REQUEST\r\n"
    s += "\r\n"
    return s


def prosses_request(request):
    return "HTTP/1.1 200 OK\r\n\r\n"