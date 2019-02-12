"""
name:
date:
description
"""
from server.Resorce import database
import pytest
import time


@pytest.fixture(autouse=True)
def run_around_tests():
    database.add_user('aaaaaaaaaaaaaaaaaaaaaaaa')
    yield
    database._immidiate_delete('aaaaaaaaaaaaaaaaaaaaaaaa')
    database._immidiate_delete('aaaaaaaaaaaaaaaaaaaaaaa1')



@pytest.mark.parametrize("userID,result", [
    ('aaaaaaaaaaaaaaaaaaaaaaa1', True),
    ('aaaaaaaaaaaaaaaaaaaaaaaa', False),
])
def test_add_user(userID, result):
    assert database.add_user(userID) is result


@pytest.mark.parametrize("userID, progID, username, password, result", [
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 'wertgdfsgf', 'dstsdf', 'sadfsxcvx', True),
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 'sdas', 'asdsad', 'asdsadsd', True),
])
def test_add_pass(userID, progID, username, password, result):
    database.add_record(userID, progID, username, password)
    time.sleep(1)
    result2 = database.get_record(userID, progID)
    if result:
        assert result2 == {'username': username, 'password': password, 'program_id': progID}
    else:
        assert result2 is None


def test_get_all_records():
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam', 'adibleyer', '123456')
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam2', 'adibleyer', '123456')
    time.sleep(1)
    result = database.get_all_records('aaaaaaaaaaaaaaaaaaaaaaaa')
    assert result == [
        {'username': 'adibleyer', 'program_id': 'steam'},
        {'username': 'adibleyer', 'program_id': 'steam2'}
    ]