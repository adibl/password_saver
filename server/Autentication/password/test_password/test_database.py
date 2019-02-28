"""
name:
date:
description
"""
import time
from server.Autentication.password import database
import pytest
import bson


def test_add_user():
    ret = database.add('user', 'password')
    assert type(ret) is bson.objectid.ObjectId
    identifier = ret
    database._immidiate_delete(identifier)


def test_add_user_username_already_exzist():
    identifier = database.add('user', 'password')
    time.sleep(1)
    assert database.add('user', 'password') == database.USERNAME_ALREADY_EXZIST
    database._immidiate_delete(identifier)
