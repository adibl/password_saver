"""
name:
date:
description
"""
import pytest

from server import request
from server.Autentication.JWT import create
from server.HTTPtolls import *


def valid_JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa')


@pytest.mark.parametrize("packege,uri", [
    ("GET /client/try?id=123 HTTP/1.1\r\n", "/client/try"),
    ("DELETE /client/try HTTP/1.1", "/client/try"),
    ("POST /client/try?id=123&sdfg=hyjydghj HTTP/1.1", "/client/try"),
])
def test_get_URI(packege, uri):
    assert request.Request(packege).get_URI() == uri


@pytest.mark.parametrize("packege,is_valid", [
    ("GET /client/try?id=123 HTTP/1.1\r\nAuthorization: Bearer {0}\r\nContent-Type: application/json\r\n".format(valid_JWT()), OK),
    ("POST /client/try?id=123 HTTP/1.1\r\nAuthorization: Bearer {0}\r\nContent-Type: application/xml\r\n".format(valid_JWT()), OK),
    ("AAA /client/try?id=123 HTTP/1.1\r\nAuthorization: Bearer {0}\r\nContent-Type: application/json\r\n".format(valid_JWT()), BAD_REQUEST),
    ("GET /client/try?id123 HTTP/1.1\r\nAuthorization: Bearer {0}\r\nContentType: application/json\r\n".format(valid_JWT()), BAD_REQUEST),
    ("GET /client/try?id=123 HTTP/1.1\r\nuthorization: Bearer {0}\r\nContent-Type: application/json\r\n".format(valid_JWT()), OK),
])
def test_validate_request(packege, is_valid):
    assert request.Request.validate(packege) == is_valid
