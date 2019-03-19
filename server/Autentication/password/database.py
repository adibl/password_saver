"""
name:
date:
description
"""
import pymongo
from bson.objectid import ObjectId
from datetime import datetime
import logging
from passlib.hash import bcrypt
import server.Resorce.database as resorce_database

EXPIRE_TIME_HOUERS = 48 #FIXME: should be the same as resorce database
CONN_STR = 'mongodb://admin:LBGpC.hSJ2xvDk_@passsaver-shard-00-00-k4jpt.mongodb.net:27017,passsaver-shard-00-01-k4jpt.mongodb.net:27017,passsaver-shard-00-02-k4jpt.mongodb.net:27017/test?ssl=true&replicaSet=passSaver-shard-0&authSource=admin&retryWrites=true'

USERNAME_ALREADY_EXZIST = 1


def create_database():
    """
    :param int expire_time: after how match time to expire documents (minites)
    :return: None
    """
    client = pymongo.MongoClient(CONN_STR)
    db = client.Autentication
    collection = db.passwords
    collection.create_index('delete_time', expireAfterSeconds=60*60*EXPIRE_TIME_HOUERS)
    collection.create_index('username', unique=True)

def connect():
    """
    connect to the database.
    :return:
    """
    client = pymongo.MongoClient(CONN_STR)
    db = client.Autentication
    return db.passwords


def add(username, password):
    """
    add user to database
    :param username: the client username
    :param password: the client password
    :return: the client id if created None otherwise.
    """
    collection = connect()
    try:
        d = {'username': username, 'password':  bcrypt.using(rounds=13).hash(password)}
        ret = collection.insert_one(d) #QUESTION: how match rounds to do??
    except pymongo.errors.DuplicateKeyError as err:
        return USERNAME_ALREADY_EXZIST
    except pymongo.errors as err:
        logging.critical('add user didint sucsess' + str(err))
        return None
    if resorce_database.add_user(ret.inserted_id):
        return ret.inserted_id
    else:
        return None


def validate(username, password):
    """
    validate user cradentials
    :param username:
    :param password:
    :return: the id if the password is correct and None otherwise
    """

    collection = connect()
    try:
        prog = collection.find_one({'username': username})
        print prog
    except pymongo.errors as err:
        logging.info('add user didint sucsess' + str(err))
        return None
    if prog is None:
        return None
    elif bcrypt.verify(password, prog['password']):
        return prog['_id']
    else:
        return None


#unchecked
def delete_user(clientID):
    """
    delete user after few days from action
    :param clientID: the client id to delete
    :return bool: True if update seceded, False otherwise
    """
    collection = connect()
    # TODO: add delete user data in resorce database
    if resorce_database.delete_user(clientID) is True:
        ret = collection.update_one({'_id': ObjectId(clientID)}, {'$set': {'delete_time': datetime.utcnow()}})
        return ret.modified_count == 1
    else:
        return False


def _immidiate_delete(clientID):
    """
    immediately delete user FOR TEST ONLY!!
    """
    collection = connect()
    resorce_database._immidiate_delete(clientID)
    return collection.delete_one({'_id': ObjectId(clientID)})

create_database()


