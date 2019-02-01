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

    assert validate.ValidateAuthentication(packege).__validate_Authentication() == is_valid


@pytest.mark.parametrize("packege,JWT", [
    ("Authorization: Bearer A.BCD.EFG\n", "A.BCD.EFG"),
    ("Authorization: Bearer ABCDEFGfdhghf6756756.sdfgs.dfgd\n", "ABCDEFGfdhghf6756756.sdfgs.dfgd"),
])
def test_get_JWT(packege, JWT):
    assert validate.ValidateAuthentication(packege).get_JWT() == JWT