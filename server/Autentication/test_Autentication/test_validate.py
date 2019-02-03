"""
name:
date:
description
"""
import pytest
from server.Resorce import request as validate
from server.Autentication.JWT import create


def valid_JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa')

@pytest.mark.parametrize("packege,is_valid", [
("GET /client/try HTTP/1.1\nAuthorization: Bearer {0}\nContent-Type: application/json\n".format(valid_JWT()), 200),
("GET /client/try HTTP/1.1\nAuthorization: Bearer {0}\nContent-Type: application/json\n".format('aa.ff.vvvvdvvd'), 401),
])
def test_valid_JWT(packege, is_valid):
    assert validate.AuthenticatedRequest.validate(packege) == is_valid


@pytest.mark.parametrize("packege,JWT", [
    ("Authorization: Bearer A.BCD.EFG\n", "A.BCD.EFG"),
    ("Authorization: Bearer ABCDEFGfdhghf6756756.sdfgs.dfgd\n", "ABCDEFGfdhghf6756756.sdfgs.dfgd"),
])
def test_get_JWT(packege, JWT):
    assert validate.AuthenticatedRequest(packege).get_JWT() == JWT