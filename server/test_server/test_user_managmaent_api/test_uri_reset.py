import json

import pytest
import requests

from Autentication.Password import database
from server.Autentication.JWT import create, validate

@pytest.fixture(autouse=True)
def run_around_tests():
    id = database.add('username', 'Secretpass123#', 'question', 'ans')
    print id
    yield
    database._immidiate_delete(str(id))


URI = 'http://127.0.0.1:50007'


def test_GET_valid():
    responce = requests.get(URI + '/reset', json={'username': 'username'})
    assert responce.status_code == 200


def test_GET_without_data():
    responce = requests.get(URI + '/reset')
    assert responce.status_code == 442
    data = json.loads(responce.text)
    assert 'username' in data


def test_GET_username_not_found():
    responce = requests.get(URI + '/reset', json={'username': 'usernameDINT_EXZIST'})
    assert responce.status_code == 442
    data = json.loads(responce.text)
    assert 'username' in data

def test_PATCH_valid_request():
    responce = requests.patch(URI + '/reset',
                              json={'username': 'username', 'NewUsername': 'aa',
                                    'NewPassword': 'Qazwsx12#', 'answer': 'ans'})
    assert responce.status_code == 200
    assert not database.validate('aa', 'Qazwsx12#') == database.USERNAME_OR_PASSWORD_INCORRECT


def test_PATCH_wrong_answear():
    responce = requests.patch(URI + '/reset',
                              json={'username': 'username', 'NewUsername': 'aa',
                                    'NewPassword': 'Qazwsx12#', 'answer': 'WRONG'})
    assert responce.status_code == 442
    print json.loads(responce.text)
    assert 'answer' in json.loads(responce.text)


def test_PATCH_wrong_username():
    responce = requests.patch(URI + '/reset',
                              json={'username': 'WRONG', 'NewUsername': 'aa',
                                    'NewPassword': 'Qazwsx12#', 'answer': 'ans'})
    assert responce.status_code == 442
    print json.loads(responce.text)
    assert 'username' in json.loads(responce.text)



def test_PATCH_new_pass_dont_in_password_cratirions():
    responce = requests.patch(URI + '/reset',
                              json={'username': 'username', 'NewUsername': 'aa',
                                    'NewPassword': 'Qazwsx12', 'answer': 'ans'})
    assert responce.status_code == 442
    print json.loads(responce.text)
    assert 'password' in json.loads(responce.text)

def test_use_jwt_after_password_reset():

    id = database.add('username2', 'Secretpass123#', 'question', 'ans')
    jwt = create(str(id))
    responce = requests.patch(URI + '/reset',
                              json={'username': 'username2', 'NewUsername': 'aa',
                                    'NewPassword': 'Qazwsx12#', 'answer': 'ans'})
    assert responce.status_code == 200
    assert validate(jwt) is False
    database.delete_user(id)


