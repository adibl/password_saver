"""
name:
date:
description
"""
from datetime import datetime

import pymongo
from bson.objectid import ObjectId

from server.database_errors import *

MAX_TIMEOUT = 25  # TODO: move to create file
PORT = 27017


def connect(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        client = pymongo.MongoClient(port=PORT)
        db = client.Autentication
        ret = f(db.jwt_time, *args, **kwds)
        client.close()
        return ret

    return wrapper


def create_database(expire_time=MAX_TIMEOUT):
    """
    :param int expire_time: after how match time to expire documents (minites)
    :return: None
    """
    client = pymongo.MongoClient(port=PORT)
    db = client.Autentication
    collection = db.jwt_time
    collection.ensure_index('register_time', expireAfterSeconds=60 * expire_time)


@handle_general_eror
@connect
def add(collection, clientID):
    """
    add user record to database
    :param clientID: the client identifier
    :return:
    """
    collection.insert_one({'_id': ObjectId(clientID), 'register_time': datetime.utcnow()})


@handle_general_eror
@connect
def validate_JWT_time(collection, clientID, time):
    """
    check if the token was issoed befor or after the last user password change
    :param clientID: the client that owns the token ID
    :param time: the time the token was iisoed
    :return: True if the token is valid, False otherwise
    """
    reg_time = collection.find_one({'_id': ObjectId(clientID)})
    if reg_time is None:
        return True
    utc_dt = datetime.utcfromtimestamp(time)
    return reg_time['register_time'] < utc_dt


@handle_general_eror
@connect
def delete(collection, clientID):
    """
    delete user credentials reset, FOR TESTS ONLY!!!
    :param clientID: the client ID
    :return: None
    """
    collection.delete_one({'_id': ObjectId(clientID)})
