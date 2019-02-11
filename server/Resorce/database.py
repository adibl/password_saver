"""
name:
date:
description
"""
import pymongo
from bson.objectid import ObjectId
from datetime import datetime

MAX_TIMEOUT = 24*5 #FIXME move to create file
CONN_STR = 'mongodb://admin:LBGpC.hSJ2xvDk_@passsaver-shard-00-00-k4jpt.mongodb.net:27017,passsaver-shard-00-01-k4jpt.mongodb.net:27017,passsaver-shard-00-02-k4jpt.mongodb.net:27017/test?ssl=true&replicaSet=passSaver-shard-0&authSource=admin&retryWrites=true'



def create_database(expire_time =MAX_TIMEOUT):
    """
    create the database with all needed
    :param expire_time: the time (in houers) after a delete user command will be executed
    :return: None
    """
    client = pymongo.MongoClient(CONN_STR)
    db = client.Resorce
    db.users.ensure_index('delete_time', expireAfterSeconds=60 * 60 * expire_time)


def add_user(userID):
    """
    :param userID: the user ID to create the collection for
    :return: True ifg the client was created, False if he is already exzist
    """
    client = pymongo.MongoClient(CONN_STR)
    db = client.Resorce
    try:
        col = db['users'].insert_one({'_id': ObjectId(userID), 'records': []})
    except pymongo.errors.DuplicateKeyError as err:
        return False
    return True


def get_col():
    """
    get the collection of the users
    :return: pymongo collection object
    """
    client = pymongo.MongoClient(CONN_STR)
    db = client.Resorce
    record = db['users']
    return record


def add_record(clientID, programID, username, password):
    """
    :param clientID: the client ID
    :param programID: the program identifier
    :param username: the client username to the program
    :param password: the client password to the program
    :return: #QUESTION: ??
    """
    collection = get_col()
    res = collection.update({'_id': ObjectId(clientID) },
    {
     '$addToSet': {
        'records': {'program_id': programID, 'username': username, 'password': password}
        }
    })
    return res


def get_record(clientID, programID):
    """
    get record from database
    :param clientID: the client to get the record from
    :param programID: the program identifier to get the cradentials to
    :return: username and password for the program
    """
    collection = get_col()
    prog = collection.find_one({'_id': ObjectId(clientID)}, {'records': {'$elemMatch': {'program_id': programID}}})
    print prog
    if prog is None:
        return None
    return prog[u'records']


def get_all_records(clientID):
    collection = get_col()
    prog = collection.find_one({'_id': ObjectId(clientID)}, {'records.program_id': 1, 'records.username': 1})
    if prog is None:
        return None
    return prog[u'records']


def delete_user(clientID):
    """
    delete user after few days from action
    :param clientID: the client id to delete
    :return: #QUESTION: ??
    """
    collection = get_col()
    return collection.update({'_id': ObjectId(clientID)}, {'delete_time': datetime.utcnow()})


def _immidiate_delete(clientID):
    """
    immediately delete user FOR TEST ONLY!!
    """
    collection = get_col()
    return collection.delete_one({'_id': ObjectId(clientID)})




