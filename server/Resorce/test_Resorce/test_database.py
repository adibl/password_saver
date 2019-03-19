"""
name:
date:
description
"""
from server.Resorce import database
import pytest
import time
#TODO: handle ServerSelectionTimeoutError

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
@pytest.mark.run(order=0)
def test_add_user(userID, result):
    assert database.add_user(userID) is result


@pytest.mark.parametrize("userID, progID, username, password, result", [
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 'wertgdfsgf', 'dstsdf', 'sadfsxcvx', True),
    ('aaaaaaaaaaaaaaaaaaaaaaaa', 'sdas', 'asdsad', 'asdsadsd', True),
])
@pytest.mark.run(order=0)
def test_add_pass(userID, progID, username, password, result):
    database.add_record(userID, progID, username, password)
    time.sleep(1)
    result2 = database.get_record(userID, progID)
    if result:
        assert result2 == {'username': username, 'password': password, 'program_id': progID}
    else:
        assert result2 is None


@pytest.mark.run(order=1)
def test_add_exzisting_progID():
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam', 'adibleyer', '123456')
    time.sleep(1)
    ret = database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam', 'adibleyer', '123456')
    assert ret is False


@pytest.mark.run(order=1)
def test_change_record():
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam', 'adibleyer', '123456')
    time.sleep(1)
    database.cange_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam', password='changed')
    time.sleep(1)
    rec = database.get_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam')
    assert rec == {'username': 'adibleyer', 'password': 'changed', 'program_id': 'steam'}



@pytest.mark.run(order=1)
def test_get_all_records():
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam', 'adibleyer', '123456')
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam2', 'adibleyer', '123456')
    time.sleep(1)
    result = database.get_all_records('aaaaaaaaaaaaaaaaaaaaaaaa')
    assert result == [
        {'username': 'adibleyer', 'program_id': 'steam'},
        {'username': 'adibleyer', 'program_id': 'steam2'}
    ]


def test_delete_record():
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam', 'adibleyer', '123456')
    time.sleep(1)
    database.delete_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam')
    time.sleep(1)
    result = database.get_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam')
    assert 'delete_time' in result


def test_delete_user():
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam', 'adibleyer', '123456')
    time.sleep(1)
    database.delete_user('aaaaaaaaaaaaaaaaaaaaaaaa')
    time.sleep(1)
    result = database.get_all_records('aaaaaaaaaaaaaaaaaaaaaaaa') #QUESTION: how I know if user will be deleted??
    assert 'delete_time' in result


