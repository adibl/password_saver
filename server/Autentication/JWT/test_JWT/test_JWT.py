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
    ('aaaaaaaaaaaaaaaaaaaaaaa1', True),
])
def test_create(userID, result):
    t = create(userID)
    assert validate(t) is result


@pytest.mark.parametrize("userID, timeout,result", [
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 5, False),
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 3, False),
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 20, True),
])
def test_validate_timeout(userID, timeout, result):
    token = create('aaaaaaaaaaaaaaaaaaaaaaaa', timeout=timeout / 60.0)
    time.sleep(10)
    assert validate(token) is result
