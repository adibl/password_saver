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
("GET /client/try HTTP/1.1\r\nAuthorization: Bearer {0}\r\nContent-Type: application/json\r\n".format(valid_JWT()), 200),
("GET /client/try HTTP/1.1\r\nAuthorization: Bearer {0}\r\nContent-Type: application/json\r\n".format('aa.ff.vvvvdvvd'), 401),
])
def test_valid_JWT(packege, is_valid):
    assert validate.ValidateAuthentication(packege).validate() == is_valid


@pytest.mark.parametrize("packege,JWT", [
    ("Authorization: Bearer A.BCD.EFG\n", "A.BCD.EFG"),
    ("Authorization: Bearer ABCDEFGfdhghf6756756.sdfgs.dfgd\n", "ABCDEFGfdhghf6756756.sdfgs.dfgd"),
])
def test_get_JWT(packege, JWT):
    assert validate.ValidateAuthentication(packege).get_JWT() == JWT