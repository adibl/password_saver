"""
name:
date:
description
"""
import pytest
from Autentication.JWT.request import AuthenticatedRequestJWT
from server.Autentication.JWT import create

import time
from HTTPtolls import *


def valid_JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa')

@pytest.mark.parametrize("packege,is_valid", [
("GET /client/try HTTP/1.1\nAuthorization: Bearer {0}\nContent-Type: application/json\n".format(valid_JWT()), 200),
("GET /client/try HTTP/1.1\nAuthorization: Bearer {0}\nContent-Type: application/json\n".format('aa.ff.vvvvdvvd'), 401),
])
def test_valid_JWT(packege, is_valid):
    assert AuthenticatedRequestJWT.validate(packege) == is_valid


@pytest.mark.parametrize("userID, timeout,result", [
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 5, 401),
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 20, 200),
])
def test_validate_JWT_timeout(userID, timeout, result):
    token = create('aaaaaaaaaaaaaaaaaaaaaaaa', timeout=timeout/60.0)
    time.sleep(10)
    packege = "GET /client/try HTTP/1.1\nAuthorization: Bearer {0}\nContent-Type: application/json\n".format(token)
    assert AuthenticatedRequestJWT.validate(packege) == result

def test_get_user_id():
    token = create('aaaaaaaaaaaaaaaaaaaaaaaa', timeout=20 / 60.0)
    packege = "GET /client/try HTTP/1.1\nAuthorization: Bearer {0}\nContent-Type: application/json\n".format(token)
    assert AuthenticatedRequestJWT.validate(packege) == OK
    req = AuthenticatedRequestJWT(packege)
    assert req.get_user_id() == 'aaaaaaaaaaaaaaaaaaaaaaaa'