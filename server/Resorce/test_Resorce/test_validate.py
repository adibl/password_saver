"""
name:
date:
description
"""
import pytest
from server.Resorce.request import ResorceRequest
from server.Autentication.JWT import create
from server.HTTPtolls import *


def valid_JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa')


@pytest.mark.parametrize("packege,is_valid", [
    ("GET /passwords?id=123 HTTP/1.1", True),
    ("DELETE /false HTTP/1.1", False),
    ("POST /passwords/steam?id=123&sdfg=hyjydghj HTTP/1.1", True),
    ("GET /passwords/blabla?id=123 HTTP/1.1\nAuthorization: Bearer A.BCD.EFG\nContent-Type: application/json\n", True),
])
def test_validate_URI(packege, is_valid):
    assert ResorceRequest.IsResorceURL(packege) == is_valid