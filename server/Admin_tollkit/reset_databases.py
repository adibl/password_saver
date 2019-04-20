"""
name:
date:
description
"""
import pymongo

from server.Autentication.JWT.database import create_database as create_jwt
from server.Autentication.Password.database import create_database as create_password
from server.Resorce.database import create_database as create_resorce

CONN_STR = 'mongodb://admin:LBGpC.hSJ2xvDk_@passsaver-shard-00-00-k4jpt.mongodb.net:27017,passsaver-shard-00-01-k4jpt.mongodb.net:27017,passsaver-shard-00-02-k4jpt.mongodb.net:27017/test?ssl=true&replicaSet=passSaver-shard-0&authSource=admin&retryWrites=true'
client = pymongo.MongoClient(CONN_STR)
db = client.Autentication
db.passwords.drop()
create_password()
db = client.Autentication
db.jwt_time.drop()
create_jwt()
db = client.Resorce
db.users.drop()
create_resorce()
client.close()
