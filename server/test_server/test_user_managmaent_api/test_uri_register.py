import base64
import json
import time

import pymongo
import pytest
import requests

from Autentication.Password import database
from server.Autentication.JWT import create


@pytest.fixture()
def delete_user():
    yield
    try:
        id = database.validate('username', 'Secretpass123#')
        if len(str(id)) > 10:
            database._immidiate_delete(id)

        id = database.validate('username', 'Secretpass')
        if len(str(id)) > 10:
            database._immidiate_delete(id)
    except pymongo.errors as err:
        pass


@pytest.fixture
def JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa', 25)

@pytest.fixture
def session():
    s = requests.Session()
    s.verify = False
    return s

URI = 'https://127.0.0.1:50007'


def test_POST_valid_request(delete_user, session):
    auto = base64.b64encode('username:Secretpass123#')
    responce = session.post(URI + '/register', headers={'Authorization': 'Basic {0}'.format(auto)},
                             json={'question': 'b', 'answer': 'c'})
    assert responce.status_code == 200


def test_POST_unvalid_JWT_autentication(JWT, delete_user, session):
    responce = session.post(URI + '/register', headers={'Authorization': 'Bearer {0}'.format(JWT)},
                             json={'question': 'b', 'answer': 'c'})
    assert responce.status_code == 401


def test_POST_username_already_exzist(delete_user, session):
    auto = base64.b64encode('username:Secretpass123#')
    responce = session.post(URI + '/register', headers={'Authorization': 'Basic {0}'.format(auto)},
                             json={'question': 'b', 'answer': 'c'})
    time.sleep(1)
    responce = session.post(URI + '/register', headers={'Authorization': 'Basic {0}'.format(auto)},
                             json={'question': 'b', 'answer': 'c'})
    assert responce.status_code == 442
    data = json.loads(responce.text)
    assert 'username' in data


def test_POST_pass_is_not_valid(delete_user, session):
    auto = base64.b64encode('username:Secretpass')
    responce = session.post(URI + '/register', headers={'Authorization': 'Basic {0}'.format(auto)},
                             json={'question': 'b', 'answer': 'c'})
    time.sleep(1)
    responce = session.post(URI + '/register', headers={'Authorization': 'Basic {0}'.format(auto)},
                             json={'question': 'b', 'answer': 'c'})
    assert responce.status_code == 442
    data = json.loads(responce.text)
    assert 'password' in data


def test_POST_without_question_and_pass_in_not_valid(delete_user, session):
    auto = base64.b64encode('username:Secretpass')
    responce = session.post(URI + '/register', headers={'Authorization': 'Basic {0}'.format(auto)})
    assert responce.status_code == 442
    data = json.loads(responce.text)
    assert 'question' in data
    assert 'answer' in data
