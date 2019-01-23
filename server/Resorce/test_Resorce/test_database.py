"""
name:
date:
description
"""
import sys
import time
from server.Resorce import database


import pytest
from server.Autentication.JWT import validate, create


@pytest.fixture(autouse=True)
def run_around_tests():
    yield
    database.delete_user('aaaaaaaaaaaaaaaaaaaaaaaa')



@pytest.mark.parametrize("userID,result", [
    ('aaaaaaaaaaaaaaaaaaaaaaaa', True),
    ('aaaaaaaaaaaaaaaaaaaaaaa1', False),
])
def test_add_user(userID, result):
    assert database.add_user(userID) is result