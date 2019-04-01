
import pytest
import requests
import base64
from server.Autentication.JWT import create
from Autentication.Password import database
import time
import json
import pymongo


@pytest.fixture(autouse=True)
def run_around_tests():
    id = database.add('username', 'Secretpass123', 'question', 'ans')
    yield
    database._immidiate_delete(id)


@pytest.fixture
def JWT():
    return create('aaaaaaaaaaaaaaaaaaaaaaaa', 25)

URI = 'http://127.0.0.1:50007'

def test_GET_valid():
    responce = requests.get(URI + '/reset', json={'username': 'username'})
    assert responce.status_code == 200