"""
name:
date:
description
"""
import pytest
from server.Resorce.validate import ValidateResorce
from server.Autentication.JWT import create
from HTTPtolls import *


def valid_JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa')


@pytest.mark.parametrize("packege,is_valid", [
    ("GET /client/try?id=123 HTTP/1.1", 200),
    ("DELETE /client/try HTTP/1.1", 405),
    ("POST /client/try?id=123&sdfg=hyjydghj HTTP/1.1", 200),
    ("GET /client/try?id=123 HTTP/1.1\nAuthorization: Bearer A.BCD.EFG\nContent-Type: application/json\n", 200),
])
def test_validate_URI(packege, is_valid):
    assert ValidateResorce(packege)._ValidateResorce__validate_URI() == is_valid