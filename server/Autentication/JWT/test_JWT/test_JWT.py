"""
name:
date:
description
"""
import time


import pytest
from server.Autentication.JWT import validate, create

@pytest.mark.parametrize("userID,result", [
    ('aaaaaaaaaaaaaaaaaaaaaaaa', True),
    ('aaaaaaaaaaaaaaaaaaaaaaaa', True),
])
def test_create(userID, result):
    assert validate(create(userID)) is not False


@pytest.mark.parametrize("userID, timeout,result", [
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 5, True),
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 3, True),
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 11, False),
])
def test_validate_timeout(userID, timeout,result):

    token = create('aaaaaaaaaaaaaaaaaaaaaaaa', timeout=timeout/60)
    time.sleep(10)
    assert validate(token) is not False

