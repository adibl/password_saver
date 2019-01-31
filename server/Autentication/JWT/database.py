"""
name:
date:
description
"""
import pymongo
from bson.objectid import ObjectId
import time
from datetime import datetime
MAX_TIMEOUT = 25 #FIXME move to create file
CONN_STR = 'mongodb://admin:LBGpC.hSJ2xvDk_@passsaver-shard-00-00-k4jpt.mongodb.net:27017,passsaver-shard-00-01-k4jpt.mongodb.net:27017,passsaver-shard-00-02-k4jpt.mongodb.net:27017/test?ssl=true&replicaSet=passSaver-shard-0&authSource=admin&retryWrites=true'



def create_database(expire_time):
    """
    :param int expire_time: after how match time to expire documents (minites)
    :return: None
    """
    client = pymongo.MongoClient(CONN_STR)
    db = client.Autentication
    collection = db.jwt_time
    collection.ensure_index('register_time', expireAfterSeconds=60*expire_time)

def connect():
    client = pymongo.MongoClient(CONN_STR)
    db = client.Autentication
    return db.jwt_time

def add(clientID):
    collection = connect()
    collection.insert_one({'_id': ObjectId(clientID), 'register_time' : datetime.utcnow()})

def validate(clientID, time):
    """
    check if the token was issoed befor or after the last user password change
    :param clientID: the client that owns the token ID
    :param time: the time the token was iisoed
    :return: True if the token is valid, False otherwise
    """
    collection = connect()
    reg_time = collection.find_one({'_id': ObjectId(clientID)})
    if reg_time is None:
        return True
    utc_dt = datetime.utcfromtimestamp(time)
    return reg_time['register_time'] < utc_dt


def delete(clientID):
    collection = connect()
    collection.delete_one({'_id': ObjectId(clientID)})



