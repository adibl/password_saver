"""
name:
date:
description
"""
from server.Resorce import database
import pytest


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
    result2 = database.get_record(userID, progID)
    if result:
        assert result2 == [{'username': username, 'password': password, 'program_id': progID}]
    else:
        assert result2 is None