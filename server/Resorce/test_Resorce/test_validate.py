"""
name:
date:
description
"""

import pytest
from server.Resorce import validate as validate
from server.Autentication.JWT import create

def valid_JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa')

@pytest.mark.parametrize("packege,is_valid", [
("GET /client/try?id=123 HTTP/1.1\nAuthorization: Bearer {0}\nContent-Type: application/json\n".format(valid_JWT()), True),
    ("Authorization: Bearer {0}".format(valid_JWT()), True),
    ("Authorizationx: Bearer {0}".format(valid_JWT()), False),
    ("Authorization: Bearer{0}".format(valid_JWT()), False),
])
def test_valid_JWT(packege, is_valid):

    assert validate.__validate_Authentication(packege) == is_valid


@pytest.mark.parametrize("packege,JWT", [
    ("Authorization: Bearer A.BCD.EFG\n", "A.BCD.EFG"),
    ("Authorization: Bearer ABCDEFGfdhghf6756756.sdfgs.dfgd\n", "ABCDEFGfdhghf6756756.sdfgs.dfgd"),
])
def test_get_JWT(packege, JWT):
    assert validate.get_JWT(packege) == JWT


@pytest.mark.parametrize("packege,is_valid", [
    ("GET /client/try?id=123 HTTP/1.1", True),
    ("DELETE /client/try HTTP/1.1", True),
    ("POST /client/try?id=123&sdfg=hyjydghj HTTP/1.1", True),
    (" GET /client/try?id=123 HTTP/1.1", False),
    ("GET/client/try?id=123 HTTP/1.1", False),
    ("GET client/try?id=123 HTTP/1.1", False),
    ("GET /client/try? HTTP/1.1", False),
    ("AAA /client/try HTTP/1.1", False),
    ("GET /client/try?id=123 HTTP/1.1\nAuthorization: Bearer A.BCD.EFG\nContent-Type: application/json\n", True),
])
def test_validate_URI(packege, is_valid):
    assert validate.__validate_URI(packege) == is_valid

@pytest.mark.parametrize("packege,uri", [
    ("GET /client/try?id=123 HTTP/1.1\r\n", "/client/try"),
    ("DELETE /client/try HTTP/1.1", "/client/try"),
    ("POST /client/try?id=123&sdfg=hyjydghj HTTP/1.1", "/client/try"),
])
def test_get_URI(packege, uri):
    assert validate.get_URI(packege) == uri


@pytest.mark.parametrize("packege,is_valid", [
    ("GET /client/try?id=123 HTTP/1.1\nAuthorization: Bearer {0}\nContent-Type: application/json\n".format(valid_JWT()), validate.OK),
    ("POST /client/try?id=123 HTTP/1.1\nAuthorization: Bearer {0}\nContent-Type: application/xml\n".format(valid_JWT()), validate.OK),
    ("GET /client/try/unoterized?id=123 HTTP/1.1\nAuthorization: Bearer {0}\nContent-Type: application/json\n".format(valid_JWT()), validate.NOT_FOUND),
    ("GET /client/try?id=123 HTTP/1.1\n Authorization: Bearer {0}\nContent-Type: blabla\n".format(valid_JWT()), (406, "Not Acceptable")),
    ("AAA /client/try?id=123 HTTP/1.1\nAuthorization: Bearer {0}\nContent-Type: application/json\n".format(valid_JWT()), validate.BAD_REQUEST),
    ("GET /client/try?id123 HTTP/1.1\nAuthorization: Bearer {0}\nContentType: application/json\n".format(valid_JWT()), validate.BAD_REQUEST),
    ("GET /client/try?id=123 HTTP/1.1\nuthorization: Bearer {0}\nContent-Type: application/json\n".format(valid_JWT()), validate.BAD_REQUEST),
    ("DELETE /client/try?id=123 HTTP/1.1\nAuthorization: Bearer {0}\nContent-Type: application/xml\n".format(valid_JWT()), validate.METHOD_NOT_ALLOWED),
])
def test_validate_request(packege, is_valid):
    assert validate.validate_request(packege) == is_valid