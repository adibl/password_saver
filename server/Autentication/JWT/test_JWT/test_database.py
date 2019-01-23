"""
name:
date:
description
"""
import sys
import time
from server.Autentication.JWT import database


import pytest
from server.Autentication.JWT import validate, create


@pytest.fixture(autouse=True)
def run_around_tests():
    #database.delete_time('aaaaaaaaaaaaaaaaaaaaaaaa')
    yield
    database.delete_time('aaaaaaaaaaaaaaaaaaaaaaaa')

@pytest.mark.parametrize("userID,reset_time,result", [
    ('aaaaaaaaaaaaaaaaaaaaaaaa', int(time.time()) + 10000, True),
    ('aaaaaaaaaaaaaaaaaaaaaaaa', int(time.time()), False),
])
def test_insert_get(userID, reset_time, result):
    time.sleep(0.5)
    database.add_time(userID)
    time.sleep(0.5)
    print database.validate_time(userID, reset_time)
    assert database.validate_time(userID, reset_time) is result



@pytest.mark.parametrize("userID,reset_time,result", [
    ('aaaaaaaaaaaaaaaaaaaaaaaa', int(time.time()), True),
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 500, True),
])
def test_insert_not_found(userID, reset_time, result):
    assert database.validate_time(userID, time) is result