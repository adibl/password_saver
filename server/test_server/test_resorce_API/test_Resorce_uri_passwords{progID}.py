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
from bson import json_util
import time


URI = 'http://127.0.0.1:50007'

@pytest.fixture(autouse=True)
def run_around_tests():
    database.add_user('aaaaaaaaaaaaaaaaaaaaaaaa')
    time.sleep(1)
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'steam', 'adibl', '1234')
    database.add_record('aaaaaaaaaaaaaaaaaaaaaaaa', 'gmail', 'adibl', 'abcdef')
    time.sleep(1)
    yield
    database._immidiate_delete('aaaaaaaaaaaaaaaaaaaaaaaa')
    time.sleep(1)

@pytest.fixture
def JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa', 25)

@pytest.mark.run(order=0)
def test_GET_valid_requet(JWT):
    responce = requests.get(URI + '/passwords/steam', headers={'Authorization': 'Bearer {0}'.format(create('aaaaaaaaaaaaaaaaaaaaaaaa', 25)), })
    assert responce.status_code == 200
    data = json.loads(responce.text)
    assert type(data) is dict
    assert data == {"username": "adibl", "password": '1234', "program_id": "steam"}


@pytest.mark.run(order=0)
def test_GET_unvalid_user(JWT):
    responce = requests.get(URI + '/passwords/steam', headers={'Authorization': 'Bearer {0}'.format(create('aaaaaaaaaaaaaaaaaa111111', 25)), })
    assert responce.status_code == 401


@pytest.mark.run(order=0)
def test_GET_unvalid_program(JWT):
    responce = requests.get(URI + '/passwords/invalid', headers={'Authorization': 'Bearer {0}'.format(create('aaaaaaaaaaaaaaaaaaaaaaaa', 25)), })
    assert responce.status_code == 404

@pytest.mark.run(order=1)
def test_DELETE_valid_request(JWT):
    responce = requests.delete(URI + '/passwords/steam', headers={'Authorization': 'Bearer {0}'.format(JWT), })
    assert responce.status_code == 200

    #test that get return the delete time
    responce = requests.get(URI + '/passwords/steam', headers={'Authorization': 'Bearer {0}'.format(JWT)})
    assert responce.status_code == 200
    data = json.loads(responce.text, object_hook=json_util.object_hook)
    assert 'delete_time' in data

    responce = requests.get(URI + '/passwords', headers={'Authorization': 'Bearer {0}'.format(JWT)})
    assert responce.status_code == 200
    data = json.loads(responce.text, object_hook=json_util.object_hook)
    print data
    for program in data['records']:
        if program['program_id'] == 'steam':
            assert 'delete_time' in program


def test_metode_dont_allow(JWT):
    responce = requests.post(URI + '/passwords/steam', headers={'Authorization': 'Bearer {0}'.format(JWT), })
    assert responce.status_code == 405
    assert responce.headers['Allow'] == 'GET PATCH DELETE'

@pytest.mark.run(order=1)
def test_PATCH_valid_request(JWT):
    responce = requests.patch(URI + '/passwords/steam', headers={'Authorization': 'Bearer {0}'.format(JWT), }, json={'username': 'new_username'})
    assert responce.status_code == 200
    responce = requests.get(URI + '/passwords/steam', headers={'Authorization': 'Bearer {0}'.format(JWT), })
    data = json.loads(responce.text)
    assert type(data) is dict
    assert data['username'] == 'new_username'