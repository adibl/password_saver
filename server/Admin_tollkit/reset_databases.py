"""
name:
date:
description
"""
import pymongo

from server.Autentication.JWT.database import create_database as create_jwt
from server.Autentication.Password.database import create_database as create_password
from server.Resorce.database import create_database as create_resorce
import time

PORT = 27017
client = pymongo.MongoClient(port=27017)
db = client.Autentication
db.passwords.drop()
time.sleep(5)
create_password()
time.sleep(5)
db = client.Autentication
db.jwt_time.drop()
time.sleep(5)
create_jwt()
time.sleep(5)
db = client.Resorce
db.users.drop()
time.sleep(5)
create_resorce()
client.close()
