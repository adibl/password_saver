"""
name:
date:
description
"""
import sys
import time
sys.path.insert(0, "D:/adi/Documents/password_saver/code/JWT")  # FIXME: make this unesesery
from jwcrypto import jwk, jwt, jwe


import pytest
from server.Autentication.JWT import validate, create

@pytest.mark.parametrize("userID,result", [
    ('aaaa', True),
    ('asdfsdfsd', True),
])
def test_create(userID, result):
    assert validate(create('sdfsdf')) is not False


@pytest.mark.parametrize("userID, timeout,result", [
    ('aaaa', 5, True),
    ('asdfsdfsd', 3, True),
    ('asdfsdfsd', 11, False),
])
def test_validate_timeout(userID, timeout,result):

    token = create('sdfsdf', timeout=timeout/60)
    time.sleep(10)
    assert validate(token) is not False

