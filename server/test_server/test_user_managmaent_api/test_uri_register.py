
import pytest
import requests
import base64
from server.Autentication.JWT import create
from Autentication.Password import database
import time
import json
from bson import json_util


@pytest.fixture()
def delete_user():
    yield
    id = database.validate('username', 'Secretpass123')
    database._immidiate_delete(id)
    id = database.validate('username', 'Secretpass')
    database._immidiate_delete(id)


@pytest.fixture
def JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa', 25)

URI = 'http://127.0.0.1:50007'


def test_GET_valid_request(delete_user):
    auto = base64.b64encode('username:Secretpass123')
    responce = requests.get(URI + '/register', headers={'Authorization': 'Basic {0}'.format(auto)})
    assert responce.status_code == 200


def test_GET_unvalid_JWT_autentication(JWT, delete_user):
    responce = requests.get(URI + '/register', headers={'Authorization': 'Bearer {0}'.format(JWT)})
    assert responce.status_code == 401

def test_GET_username_already_exzist(delete_user):
    auto = base64.b64encode('username:Secretpass123')
    responce = requests.get(URI + '/register', headers={'Authorization': 'Basic {0}'.format(auto)})
    time.sleep(1)
    responce = requests.get(URI + '/register', headers={'Authorization': 'Basic {0}'.format(auto)})
    assert responce.status_code == 442
    data = json.loads(responce.text)
    assert 'username' in data

def test_GET_pass_is_not_valid(delete_user):
    auto = base64.b64encode('username:Secretpass')
    responce = requests.get(URI + '/register', headers={'Authorization': 'Basic {0}'.format(auto)})
    time.sleep(1)
    responce = requests.get(URI + '/register', headers={'Authorization': 'Basic {0}'.format(auto)})
    assert responce.status_code == 442
    data = json.loads(responce.text)
    assert 'password' in data
