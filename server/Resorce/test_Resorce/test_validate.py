"""
name:
date:
description
"""

import pytest
import __validate as validate

@pytest.mark.parametrize("packege,is_valid", [
("GET /client/try?id=123 HTTP/1.1\nAuthorization: Bearer AB.CDE.FG\nContent-Type: application/json\n", True),
    ("Authorization: Bearer A.BCD.EFG", True),
    ("Authorization: Bearer ABCDEFGfdhghf6756756.sdfgs.dfgd", True),
    ("Authorization: Bearer AB.CDE.FG", True),
    ("Authorization: Bearer AB.CDE.FG", True),
    ("Authorization: Bearer AB.CDE.FG=", False),
    ("Authorizationx: Bearer ABCDEFG", False),
    ("Authorization: BearerABCDEFG", False),
    ("Authorization:Bearer ABCDEFG", False),
    ("Authorization:Bearer ABCDEFG:asd", False),

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
    ("GET /client/try?id=123 HTTP/1.1\nAuthorization: Bearer A.BCD.EFG\nContent-Type: application/json\n", validate.OK),
    ("POST /client/try?id=123 HTTP/1.1\nAuthorization: Bearer A.BCtrghD.EFG\nContent-Type: application/xml\n", validate.OK),
    ("GET /client/try/unoterized?id=123 HTTP/1.1\nAuthorization: Bearer A.BCD.EFG\nContent-Type: application/json\n", validate.NOT_FOUND),
    ("GET /client/try?id=123 HTTP/1.1\n Authorization: Bearer A.BCD.EFG\nContent-Type: blabla\n", (406, "Not Acceptable")),
    ("AAA /client/try?id=123 HTTP/1.1\nAuthorization: Bearer A.BCD.EFG\nContent-Type: application/json\n", validate.BAD_REQUEST),
    ("GET /client/try?id123 HTTP/1.1\nAuthorization: Bearer A.BCD.EFG\nContentType: application/json\n", validate.BAD_REQUEST),
    ("GET /client/try?id=123 HTTP/1.1\nuthorization: Bearer A.BCD.EFG\nContent-Type: application/json\n", validate.BAD_REQUEST),
    ("DELETE /client/try?id=123 HTTP/1.1\nAuthorization: Bearer A.BCD.EFG\nContent-Type: application/xml\n", validate.METHOD_NOT_ALLOWED),
])
def test_validate_request(packege, is_valid):
    assert validate.validate_request(packege) == is_valid