"""
name:
date:
description
"""
from datetime import datetime

import pymongo
from bson.objectid import ObjectId
from passlib.hash import bcrypt

import server.Resorce.database as resorce_database
from HTTPtolls import *
from server.database_errors import *

EXPIRE_TIME_HOUERS = 48  # FIXME: should be the same as resorce database
ROUNDS = 13
CONN_STR = 'mongodb://admin:LBGpC.hSJ2xvDk_@passsaver-shard-00-00-k4jpt.mongodb.net:27017,passsaver-shard-00-01-k4jpt.mongodb.net:27017,passsaver-shard-00-02-k4jpt.mongodb.net:27017/test?ssl=true&replicaSet=passSaver-shard-0&authSource=admin&retryWrites=true'
USERNAME_OR_PASSWORD_INCORRECT = 2
WRONG_ANSWER = 3


# FIXME: hash the answer to the question

def connect(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        client = pymongo.MongoClient(CONN_STR)
        db = client.Autentication
        ret = f(db.passwords, *args, **kwds)
        client.close()
        return ret

    return wrapper


def create_database():
    """
    create the database with his indexes
    """
    client = pymongo.MongoClient(CONN_STR)
    db = client.Autentication
    collection = db.passwords
    collection.create_index('delete_time', expireAfterSeconds=60 * 60 * EXPIRE_TIME_HOUERS)
    collection.create_index('username', unique=True)


@handle_general_eror
@connect
def add(collection, username, password, question, anser):
    """
    add user to database
    :param username: the client username
    :param password: the client password
    :return: the client id if created None otherwise.
    :rtype: ObjectId
    """
    d = {'username': username, 'password': bcrypt.using(rounds=ROUNDS).hash(password), 'question': question, 'ans': bcrypt.using(rounds=ROUNDS).hash(anser)}
    ret = collection.insert_one(d)  # QUESTION: how match rounds to do??
    if resorce_database.add_user(ret.inserted_id):
        print ret.inserted_id
        print type(ret.inserted_id)
        return str(ret.inserted_id)
    else:
        return None


@handle_general_eror
@connect
def change_user_cradencials(collection, clientID, username=None, password=None):
    """
    change username and password to user.
    :param collection:
    :param clientID: the client id to change
    :param username: the new username or None (if you don't want to change)
    :param password: the new password or None (if you don't want to change)
    :return: True if operatoin sucseed, False otherwise
    """
    d = {}
    if username is not None:
        d['username'] = username
    if password is not None:
        d['password'] = bcrypt.using(rounds=ROUNDS).hash(password)
    print d
    res = collection.update_one(
        {
            '_id': ObjectId(clientID),
        },
        {'$set': d}
    )
    return res.modified_count == 1


@handle_general_eror
@connect
def get_question(collection, username):
    prog = collection.find_one({'username': username})
    if prog is None:
        logging.debug('username incorrect')
        return USERNAME_OR_PASSWORD_INCORRECT
    elif 'ans' in prog:
        return str(prog['ans'])
    else:
        logging.debug('no question in database')
        return INTERNAL_ERROR


@handle_general_eror
@connect
def validate(collection, username, password):
    """
    validate user cradentials
    :param username:
    :param password: the hashed password
    :return: the id if the password is correct and None otherwise
    :rtype: str
    """

    prog = collection.find_one({'username': username})
    if prog is None:
        logging.debug('username incorrect')
        return USERNAME_OR_PASSWORD_INCORRECT
    elif bcrypt.verify(password, prog['password']):
        return str(prog['_id'])
    else:
        logging.debug('password incorrect')
        return USERNAME_OR_PASSWORD_INCORRECT


@handle_general_eror
@connect
def get_id(collection, username):
    """
    get user id from username
    :param username:
    :return: the id if the username is correct and None otherwise
    :rtype: str
    """

    prog = collection.find_one({'username': username})
    if prog is None:
        logging.debug('username incorrect')
        return USERNAME_OR_PASSWORD_INCORRECT
    else:
        return prog['_id']


@handle_general_eror
@connect
def validate_question(collection, username, anser):
    prog = collection.find_one({'username': username})
    if prog is None:
        logging.debug('username incorrect')
        return USERNAME_OR_PASSWORD_INCORRECT
    elif bcrypt.verify(anser, prog['ans']):
        return str(prog['_id'])
    else:
        logging.debug('answer incorrect')
        return WRONG_ANSWER


@handle_general_eror
@connect
def delete_user(collection, clientID):
    """
    delete user after few days from action
    :param clientID: the client id to delete
    :return bool: True if update seceded, False otherwise
    """

    resorce_database._immidiate_delete(clientID)
    return collection.delete_one({'_id': ObjectId(clientID)}).deleted_count == 1


@connect
def _immidiate_delete(collection, clientID):
    """
    immediately delete user FOR TEST ONLY!!
    """
    resorce_database._immidiate_delete(clientID)
    return collection.delete_one({'_id': ObjectId(clientID)}).deleted_count == 1


@connect
def __add_id(collection, ID, username, password):
    """
    add user with predefined ID , FOR TESTS ONLY!!!!
    :return:
    """
    d = {'_id': ObjectId(ID), 'username': username, 'password': bcrypt.using(rounds=ROUNDS).hash(password)}
    ret = collection.insert_one(d)  # QUESTION: how match rounds to do??
    resorce_database.add_user(ID)
    return ret.inserted_id
