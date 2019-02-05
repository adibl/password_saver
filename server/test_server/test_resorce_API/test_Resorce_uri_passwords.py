"""
name:
date:
description
"""
import requests
import pytest
from server.Resorce import database
from server.Autentication.JWT import create
import json


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
    responce = requests.get(URI + '/passwords', headers={'Authorization': 'Bearer {0}'.format(create('aaaaaaaaaaaaaaaaaaaaaaaa', 25)), })
    assert responce.status_code == 200
    data = json.loads(responce.text)
    assert type(data) is list
    assert data == [{"username": "adibl", "program_id": "steam"}, {"username": "adibl", "program_id": "gmail"}]


@pytest.mark.run(order=0)
def test_GET_unvalid_user(JWT):
    responce = requests.get(URI + '/passwords', headers={'Authorization': 'Bearer {0}'.format(create('aaaaaaaaaaaaaaaaaa111111', 25)), })
    assert responce.status_code == 404



@pytest.mark.run(order=1)
def test_POST_valid_requet(JWT):
    responce = requests.post(URI + '/passwords', headers={'Authorization': 'Bearer {0}'.format(JWT)}, data={'username': 'adibl', 'password': 'pass', 'program_id': 'steam2'})
    assert responce.status_code == 200
    responce = requests.get(URI + '/passwords/steam2', headers={'Authorization': 'Bearer {0}'.format(JWT), }) #FIXME: use untested uri
    assert responce.status_code == 200
    data = json.loads(responce.text)
    assert type(data) is list
    assert data == [{'username': ['adibl'], 'password': ['pass'], 'program_id': ['steam2']}]


