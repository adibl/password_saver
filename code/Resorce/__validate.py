"""
name: adi bleyer
date: =30.12.18
the API of the resorce server, wrap everything.
get REST API request and return the response.
support multi ?????????
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
    if __validate_URI(request) and __validate_JWT(request) and __validate_content_type(request):
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
        print __validate_URI(request)
        print __validate_JWT(request)
        print __validate_content_type(request)
        return BAD_REQUEST


def get_verb(request):
    return RE_URI.search(request).group(1)


def __validate_content_type(request):
    return bool(RE_CONTENT_TYPE.search(request))


def __validate_URI(request):
    return bool(RE_URI.search(request))

def get_URI(request):
    return RE_URI.search(request).group(2)

def __validate_JWT(request):
    return bool(RE_JWT.search(request))


def get_JWT(request):
    """
    :param request: the client full request
    :return: string of the JWT if fount False otherwise
    """
    return RE_JWT.search(request).group(1)

