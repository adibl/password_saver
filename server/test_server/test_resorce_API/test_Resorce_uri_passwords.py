"""
name:
date:
description
"""
import json
import time

import pytest
import requests

from server.Autentication.JWT import create
from server.Autentication.Password import database as pass_database
from server.Resorce import database
import ssl
IP = '127.0.0.1'
PORT = 50007
URI = 'https://127.0.0.1:50007'


@pytest.fixture(autouse=True)
def run_around_tests():
    print pass_database.__add_id('aaaaaaaaaaaaaaaaaaaaaaaa', 'adi', 'secpass')
    time.sleep(1)
    print database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam', 'adibl', '1234')
    print database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'gmail', 'adibl', 'abcdef')
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

    sertificate = ssl.get_server_certificate((IP, PORT), ssl_version=ssl.PROTOCOL_SSLv23)
    with open('cert.cert', 'wb') as handle:
        handle.write(sertificate)
    responce = session.get(URI + '/passwords', headers={'Authorization': 'Bearer {0}'.format(JWT), })
    assert responce.status_code == 200
    data = json.loads(responce.text)
    assert data['records'] == [{"username": "adibl", "program_id": "steam", 'sec_level': 0},
                               {"username": "adibl", "program_id": "gmail", 'sec_level': 0}]


@pytest.mark.run(order=0)
def test_GET_unvalid_user(JWT, session):
    responce = session.get(URI + '/passwords',
                            headers={'Authorization': 'Bearer {0}'.format(create('111111111111111111111111', 25)), })
    assert responce.status_code == 401


@pytest.mark.run(order=1)
def test_POST_valid_requet(JWT, session):
    responce = session.post(URI + '/passwords', headers={'Authorization': 'Bearer {0}'.format(JWT)},
                             json={'username': 'adibl', 'password': 'pass', 'program_id': 'steam2'})
    assert responce.status_code == 200
    time.sleep(1)
    responce = session.get(URI + '/passwords/steam2', headers={'Authorization': 'Bearer {0}'.format(JWT), })
    assert responce.status_code == 200
    data = json.loads(responce.text)
    assert type(data) is dict
    assert data == {'username': 'adibl', 'password': 'pass', 'program_id': 'steam2', 'sec_level': 0}


@pytest.mark.run(order=1)
def test_POST_data_is_missing(JWT, session):
    responce = session.post(URI + '/passwords', headers={'Authorization': 'Bearer {0}'.format(JWT)},
                             json={'username': 'adibl'})
    assert responce.status_code == 442
    data = json.loads(responce.text)
    assert type(data) is dict
    assert ['password', 'program_id'] == data.keys()
