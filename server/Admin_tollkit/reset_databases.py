"""
name:
date:
description
"""
from server.Autentication.Password.database import create_database as create_password
from server.Autentication.JWT.database import create_database as create_jwt
from server.Resorce.database import create_database as create_resorce
import pymongo
import time

CONN_STR = 'mongodb://admin:LBGpC.hSJ2xvDk_@passsaver-shard-00-00-k4jpt.mongodb.net:27017,passsaver-shard-00-01-k4jpt.mongodb.net:27017,passsaver-shard-00-02-k4jpt.mongodb.net:27017/test?ssl=true&replicaSet=passSaver-shard-0&authSource=admin&retryWrites=true'
client = pymongo.MongoClient(CONN_STR)
db = client.Autentication
db.passwords.drop()
#time.sleep(1)
create_password()
#time.sleep(1)
db = client.Autentication
db.jwt_time.drop()
#time.sleep(1)
create_jwt()
#time.sleep(1)
db = client.Resorce
db.users.drop()
#time.sleep(1)
create_resorce()
client.close()