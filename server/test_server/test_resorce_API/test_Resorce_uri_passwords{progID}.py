"""
name:
date:
description
"""
import base64
import json
import time

import pytest
import requests

from server.Autentication.JWT import create
from server.Autentication.Password import database as pass_database
from server.Resorce import database

URI = 'https://127.0.0.1:50007'


@pytest.fixture(autouse=True)
def run_around_tests():
    pass_database.__add_id('aaaaaaaaaaaaaaaaaaaaaaaa', 'username', 'password')
    time.sleep(1)
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam', 'adibl', '1234')
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'gmail', 'adibl', 'abcdef', sec_level=1)
    time.sleep(1)
    yield
    pass_database._immidiate_delete('aaaaaaaaaaaaaaaaaaaaaaaa')
    time.sleep(1)


@pytest.fixture
def JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa', 25)

@pytest.fixture
def session():
    s = requests.Session()
    s.verify = False
    return s


@pytest.mark.run(order=0)
def test_GET_valid_requet(JWT, session):
    responce = session.get(URI + '/passwords/steam',
                            headers={'Authorization': 'Bearer {0}'.format(create('aaaaaaaaaaaaaaaaaaaaaaaa', 25)), })
    assert responce.status_code == 200
    data = json.loads(responce.text)
    assert type(data) is dict
    assert data == {"username": "adibl", "password": '1234', "program_id": "steam", 'sec_level': 0}


@pytest.mark.run(order=0)
def test_GET_unvalid_user(JWT, session):
    responce = session.get(URI + '/passwords/steam',
                            headers={'Authorization': 'Bearer {0}'.format(create('aaaaaaaaaaaaaaaaaa111111', 25)), })
    assert responce.status_code == 401


@pytest.mark.run(order=0)
def test_GET_unvalid_program(JWT, session):
    responce = session.get(URI + '/passwords/invalid',
                            headers={'Authorization': 'Bearer {0}'.format(create('aaaaaaaaaaaaaaaaaaaaaaaa', 25)), })
    assert responce.status_code == 404


@pytest.mark.run(order=1)
def test_DELETE_valid_request(JWT, session):
    responce = session.delete(URI + '/passwords/steam', headers={'Authorization': 'Bearer {0}'.format(JWT), })
    assert responce.status_code == 200

    # test that GET return the delete time
    responce = session.get(URI + '/passwords/steam', headers={'Authorization': 'Bearer {0}'.format(JWT)})
    assert responce.status_code == 404


@pytest.mark.run(order=1)
def test_DELETE_invalid_program_id(JWT, session):
    responce = session.delete(URI + '/passwords/invalid', headers={'Authorization': 'Bearer {0}'.format(JWT), })
    assert responce.status_code == 404


def test_metode_dont_allow(JWT, session):
    responce = session.post(URI + '/passwords/steam', headers={'Authorization': 'Bearer {0}'.format(JWT), })
    assert responce.status_code == 405
    assert responce.headers['Allow'] == 'GET PATCH DELETE'


@pytest.mark.run(order=1)
def test_PATCH_valid_request(JWT, session):
    responce = session.patch(URI + '/passwords/steam', headers={'Authorization': 'Bearer {0}'.format(JWT), },
                              json={'username': 'new_username'})
    assert responce.status_code == 200
    responce = session.get(URI + '/passwords/steam', headers={'Authorization': 'Bearer {0}'.format(JWT), })
    data = json.loads(responce.text)
    assert type(data) is dict
    assert data['username'] == 'new_username'


@pytest.mark.run(order=1)
def test_PATCH_invalid_program_id(JWT, session):
    responce = session.patch(URI + '/passwords/invalid', headers={'Authorization': 'Bearer {0}'.format(JWT), },
                              json={'username': 'new_username'})
    assert responce.status_code == 404


def test_passward_autentication(session):
    responce = session.get(URI + '/passwords/steam',
                            headers={'Authorization': 'Basic {0}'.format(base64.b64encode('username:password'))})
    assert responce.status_code == 200


def test_passward_autentication_invalid_username(session):
    responce = session.get(URI + '/passwords/steam',
                            headers={'Authorization': 'Basic {0}'.format(base64.b64encode('unvalid:password'))})
    assert responce.status_code == 442


def test_GET__high_sec_level(JWT, session):
    responce = session.get(URI + '/passwords/gmail',
                            headers={'Authorization': 'Basic {0}'.format(base64.b64encode('username:password'))})
    assert responce.status_code == 200

    responce = session.get(URI + '/passwords/gmail', headers={'Authorization': 'Bearer {0}'.format(JWT), })
    assert responce.status_code == 401
    assert responce.headers['SecLevel'] == '1'


def test_GET_low_sec_level(JWT, session):
    responce = session.get(URI + '/passwords/steam',
                            headers={'Authorization': 'Basic {0}'.format(base64.b64encode('username:password'))})
    assert responce.status_code == 200

    responce = session.get(URI + '/passwords/steam', headers={'Authorization': 'Bearer {0}'.format(JWT), })
    assert responce.status_code == 200
