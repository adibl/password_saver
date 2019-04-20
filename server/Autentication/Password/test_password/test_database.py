"""
name:
date:
description
"""
import time

import pytest

import server.Resorce.database as resorce_database
from server.Autentication.Password import database
from server.database_errors import *


@pytest.fixture(autouse=True)
def run_around_tests():
    database.__add_id('aaaaaaaaaaaaaaaaaaaaaaaa', 'user', 'password')
    resorce_database.add_user('aaaaaaaaaaaaaaaaaaaaaaaa')
    time.sleep(2)
    yield
    database._immidiate_delete('aaaaaaaaaaaaaaaaaaaaaaaa')


def test_immidiate_delete():
    identifier = 'aaaaaaaaaaaaaaaaaaaaaaaa'
    assert resorce_database.add_record(identifier, 'try', 'try', 'try')
    time.sleep(1)
    database._immidiate_delete(identifier)
    time.sleep(1)
    assert database.validate('user', 'password') is database.USERNAME_OR_PASSWORD_INCORRECT
    assert resorce_database.get_record(identifier, 'try') is None


def test_add_user():
    identifier = 'aaaaaaaaaaaaaaaaaaaaaaaa'
    ret = database.validate('user', 'password')
    assert ret == identifier


def test_add_user_username_already_exzist():
    assert database.add('user', 'password', 'a', 'b') == DUPLIKATE_KEY_ERROR


def test_delete_user():
    identifier = 'aaaaaaaaaaaaaaaaaaaaaaaa'
    assert database.delete_user(identifier)
    time.sleep(1)
    ret = resorce_database.get_all_records(identifier)
    print ret
    assert 'delete_time' in ret
