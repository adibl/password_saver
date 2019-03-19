import requests
import pytest
from server.Autentication.password import database
import server.Resorce.database as resorce_database
from server.Autentication.JWT import create
import json
from bson import json_util
import time

URI = 'http://127.0.0.1:50007'

def test_POST_valid_request():
    responce = requests.post(URI, {'username': 'user', 'password': 'secpass'})
    assert responce.status_code == 200
