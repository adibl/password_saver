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
    database.__add_id('aaaaaaaaaaaaaaaaaaaaaaaa', 'username', 'Secretpass123')
    yield
    id = database.validate('username', 'Secretpass123')
    database._immidiate_delete(id)


@pytest.fixture
def JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa', 25)

@pytest.fixture
def session():
    s = requests.Session()
    s.verify = False
    return s

URI = 'https://127.0.0.1:50007'


def test_GET_valid_request(session):
    auto = base64.b64encode('username:Secretpass123')
    responce = session.get(URI + '/login', headers={'Authorization': 'Basic {0}'.format(auto)})
    assert responce.status_code == 200
    data = json.loads(responce.text)
    print data
    assert AUTENTICATION in data
    assert validate(data[AUTENTICATION])


def test_GET_unvalid_username(session):
    auto = base64.b64encode('u:Secretpass123')
    responce = session.get(URI + '/login', headers={'Authorization': 'Basic {0}'.format(auto)})
    assert responce.status_code == 442


def test_GET_unvalid_password(session):
    auto = base64.b64encode('username:Secretpass123456789')
    responce = session.get(URI + '/login', headers={'Authorization': 'Basic {0}'.format(auto)})
    assert responce.status_code == 442


def test_GET_JWT_autentication(session):
    auto = base64.b64encode('username:Secretpass123456789')
    responce = session.get(URI + '/login',
                            headers={'Authorization': 'Bearer {0}'.format(create('aaaaaaaaaaaaaaaaaaaaaaaa'))})
    assert responce.status_code == 401
