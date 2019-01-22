"""
name:
date:
description
"""
import pytest

from server.Resorce import database

@pytest.fixture(scope="session", autouse=True)
def connect():
    global conn
    conn = database.connect()

@pytest.mark.parametrize("username,result", [
    ('adi2', True),

    ])
def test_add_user(username, result):
    assert database.add_customer(username)



@pytest.mark.parametrize("userID,progID, username, password", [
    ('dddddddddddddddddddddddd', 'ddddddddddddddddddddddda', 'bleyer23', '1234'),

    ])
def test_add_pass(userID,progID, username, password):
    database.add_customer(username)
    assert database.get_site(userID, progID) == (username, password)