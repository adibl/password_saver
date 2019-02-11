"""
name:
date:
description
"""
import time
from server.Autentication.JWT import database
import pytest


@pytest.fixture(autouse=True)
def run_around_tests():
    #database.delete_time('aaaaaaaaaaaaaaaaaaaaaaaa')
    yield
    database.delete('aaaaaaaaaaaaaaaaaaaaaaaa')

@pytest.mark.parametrize("userID,reset_time,result", [
    ('aaaaaaaaaaaaaaaaaaaaaaaa', int(time.time()) + 10000, True),
    ('aaaaaaaaaaaaaaaaaaaaaaaa', int(time.time()), False),
])
def test_insert_get(userID, reset_time, result):
    time.sleep(0.5)
    database.add(userID)
    time.sleep(0.5)
    assert database.validate(userID, reset_time) is result



@pytest.mark.parametrize("userID,reset_time,result", [
    ('aaaaaaaaaaaaaaaaaaaaaaaa', int(time.time()), True),
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 500, True),
])
def test_insert_not_found(userID, reset_time, result):
    assert database.validate(userID, time) is result