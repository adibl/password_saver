"""
name:
date:
description
"""

import base64

import pytest
import requests

from Autentication.Password import database
from server.Autentication.JWT import create, validate
from server.HTTPtolls import *


@pytest.fixture(autouse=True)
def run_around_tests():
    database.__add_id('aaaaaaaaaaaaaaaaaaaaaaaa', 'username', 'Secretpass123#')
    yield
    id = database.validate('username', 'Secretpass123#')
    if not (id == database.USERNAME_OR_PASSWORD_INCORRECT or id is None):
        database._immidiate_delete(id)

@pytest.fixture
def session():
    s = requests.Session()
    s.verify = False
    return s

URI = 'https://127.0.0.1:50007'


def test_DELET_valid_request(session):
    auto = base64.b64encode('username:Secretpass123#')
    responce = session.delete(url=URI + '/delete', headers={'Authorization': 'Basic {0}'.format(auto)})
    assert responce.status_code == 200
    assert database.validate('username', 'Secretpass123#') ==  database.USERNAME_OR_PASSWORD_INCORRECT


def test_DELET_worng_password(session):
    auto = base64.b64encode('username:SomeWrongPass')
    responce = session.delete(url=URI + '/delete', headers={'Authorization': 'Basic {0}'.format(auto)})
    assert responce.status_code == 442


def test_DELET_wrong_username(session):
    auto = base64.b64encode('usernameSecretpass123#')
    responce = session.delete(url=URI + '/delete', headers={'Authorization': 'Basic {0}'.format(auto)})
    assert responce.status_code == 400

