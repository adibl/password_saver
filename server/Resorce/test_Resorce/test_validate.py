"""
name:
date:
description
"""
import pytest
from server.Resorce import validate
from server.Autentication.JWT import create
from HTTPtolls import *


def valid_JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa')


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
    assert validate.ValidateResorce(packege).__validate_URI() == is_valid