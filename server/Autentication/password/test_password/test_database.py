"""
name:
date:
description
"""
import time
from server.Autentication.password import database
import pytest
import bson
import server.Resorce.database as resorce_database

def test_immidiate_delete():
    identifier = database.add('user', 'password')
    resorce_database.add_record(identifier, 'try', 'try', 'try')
    time.sleep(1)
    database._immidiate_delete(identifier)
    time.sleep(1)
    assert database.validate('user', 'password') is None
    assert resorce_database.get_record(identifier, 'try') is None

    database._immidiate_delete(identifier)


def test_add_user():
    ret = database.add('user', 'password')
    time.sleep(1)
    identifier = ret
    ret = database.validate('user', 'password')
    print identifier
    print ret
    assert ret == identifier

    database._immidiate_delete(identifier)


def test_add_user_username_already_exzist():
    identifier = database.add('user', 'password')
    time.sleep(1)
    assert database.add('user', 'password') == database.USERNAME_ALREADY_EXZIST

    database._immidiate_delete(identifier)

def test_delete_user():
    identifier = database.add('user', 'password')
    resorce_database.add_record(identifier, 'try', 'try', 'try')
    time.sleep(1)
    database.delete_user(identifier)
    time.sleep(0.5)
    assert 'delete_time' in resorce_database.get_all_records(identifier)

    database._immidiate_delete(identifier)
