"""
name:
date:
description
"""
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
    db = client.Resorce


def add_user(userID):
    client = pymongo.MongoClient(CONN_STR)
    db = client.Resorce
    try:
        col = db.create_collection(userID)
        col.create_index('program_id')
    except pymongo.errors.CollectionInvalid as err:
        return False
    return True




def get_col(userID):
    client = pymongo.MongoClient(CONN_STR)
    db = client.Resorce
    return db[userID]


def add_record(clientID, programID, username, password):
    collection = get_col(clientID)
    collection.insert_one({'program_id': programID, 'username': username, 'password': password})


def get_record(clientID, programID):
    collection = get_col(clientID)
    reg_time = collection.find_one({'program_id': programID})
    return reg_time


def delete_user(clientID):
    collection = get_col(clientID)
    return collection.drop()




