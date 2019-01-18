"""
name:
date:
description
"""
import pytest

from server.Resorce import database

@pytest.fixture(scope="session", autouse=True)
def connect():
    database.connect()

@pytest.mark.parametrize("username,result", [
    ('adi', True),

    ])
def test_add_user(username, result):
    assert database.add_customer(username)