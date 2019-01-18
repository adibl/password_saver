"""
name: adi bleyer
date: =30.12.18
validate the request with re.
have defs to extract the data from the request.

"""
import re
# regex
URI_PREMITED_LIST = {"/client/try": ["GET", "POST"]} # TODO: add security level to premited actions
RE_URI = re.compile(r"^(GET|PUT|POST|PUTCH|DELETE) ((/\w+)+)(\?\w+=\w+(&\w+=\w+)*)? (HTTP/1.1|HTTP/1.0)")
RE_JWT = re.compile(r"^Authorization: Bearer (\w+\.\w+\.\w+\w)$", re.M)
RE_CONTENT_TYPE = re.compile("^Content-Type: (application/json|application/xml)$", re.M)
OK = 200
METHOD_NOT_ALLOWED = 405
BAD_REQUEST = 400
NOT_FOUND = 404

def validate_request(request):
    """
    valid the request:
    1.correct structure (http verb, url, http version, JWT token, content-type)
    2.premited URL
    3.valid JWT TODO: all
    4.premited HTTp verb TODO: add sec levels from JWT
    :param request: the client request
    :return: True if the request is valid and false otherwise
    """
    if __validate_URI(request) and __validate_Authentication(request) and __validate_content_type(request):
        uri = get_URI(request)
        verb = get_verb(request)
        jwt = get_JWT(request)
        if uri in URI_PREMITED_LIST.keys():
            if verb in URI_PREMITED_LIST[uri]:
                return OK
                # TODO: validate JWT
            else:
                return METHOD_NOT_ALLOWED
        else:
            return NOT_FOUND

    else:
        return BAD_REQUEST


def get_verb(request):
    """
    return the http verb of the request
    :param str request: the client request
    :return: the client request HTTP verb
    :rtype: str
    """
    return RE_URI.search(request).group(1)


def __validate_content_type(request):
    """
    validate the request content type is existing an matching
    :param str request: the client request
    :return: True if request have valid content type, False otherwise
    """
    return bool(RE_CONTENT_TYPE.search(request))


def __validate_URI(request):
    """
    validate the URI structure
    :param str request: the client request
    :return: True if the structure is valid, False otherwise
    """
    return bool(RE_URI.search(request))

def get_URI(request):
    """
    get the request URL
    :param str request: the client request
    :return: the request URI
    :rtype: str
    """
    return RE_URI.search(request).group(2)

def __validate_Authentication(request):
    """
    validate Autentication header structure
    :param str request: the client request
    :return: True if structure is valid, false otherwise
    """
    return bool(RE_JWT.search(request))


def get_JWT(request):
    """
    :param request: the client full request
    :return: JWT if fount False otherwise
    :rtype: str
    """
    if RE_JWT.search(request):
        return RE_JWT.search(request).group(1)
    return False

