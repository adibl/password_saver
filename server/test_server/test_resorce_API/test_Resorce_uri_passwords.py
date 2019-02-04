"""
name:
date:
description
"""
import requests
import pytest
from server.Resorce import database
from server.Autentication.JWT import create
URI = 'http://127.0.0.1:50007'

@pytest.fixture(autouse=True)
def run_around_tests():
    database.add_user('aaaaaaaaaaaaaaaaaaaaaaaa')
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam', 'adibl', '1234')
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'gmail', 'adibl', 'abcdef')
    yield
    database._immidiate_delete('aaaaaaaaaaaaaaaaaaaaaaaa')

@pytest.fixture
def JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa', 25)

@pytest.mark.run(order=0)
def test_GET_valid_requet(JWT):
    responce = requests.get(URI + '/passwords', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(JWT), })
    assert responce.status_code == 200


@pytest.mark.run(order=1)
def test_POST_valid_requet(JWT):
    responce = requests.post(URI + '/passwords', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(JWT)}, data={'username': 'adibl', 'password': 'pass', 'program_id': 'steam'})
    assert responce.status_code == 200
    responce = requests.get(URI + '/passwords/steam', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(JWT), })
    print responce


