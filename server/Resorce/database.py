"""
name:
date:
description
"""
import json
import logging
from datetime import datetime
from server.database_errors import *

from bson import json_util
import pymongo
from bson.objectid import ObjectId


MAX_TIMEOUT = 24 * 5  # FIXME move to create file
CONN_STR = 'mongodb://admin:LBGpC.hSJ2xvDk_@passsaver-shard-00-00-k4jpt.mongodb.net:27017,passsaver-shard-00-01-k4jpt.mongodb.net:27017,passsaver-shard-00-02-k4jpt.mongodb.net:27017/test?ssl=true&replicaSet=passSaver-shard-0&authSource=admin&retryWrites=true'



@handle_general_eror
def create_database(expire_time=MAX_TIMEOUT):
    """
    create the database with all needed
    :param expire_time: the time (in houers) after a delete user command will be executed
    :return: None
    """
    client = pymongo.MongoClient(CONN_STR)
    db = client.Resorce
    db.users.ensure_index('delete_time', expireAfterSeconds=60 * 60 * expire_time)


@handle_general_eror
def add_user(userID):
    """
    :param userID: the user ID to create the collection for
    :return: True ifg the client was created, False if he is already exzist
    """
    client = pymongo.MongoClient(CONN_STR)
    db = client.Resorce
    col = db['users'].insert_one({'_id': ObjectId(userID), 'records': []})
    return True


@handle_general_eror
def get_col():
    """
    get the collection of the users
    :return: pymongo collection object
    """
    client = pymongo.MongoClient(CONN_STR)
    db = client.Resorce
    record = db['users']
    return record


@handle_general_eror
def add_record(clientID, programID, username, password, sec_level=0):
    """
    :param clientID: the client ID
    :param programID: the program identifier
    :param username: the client username to the program
    :param password: the client password to the program
    :param sec_level: the security level of this record
    :return bool: True if update seceded False otherwise
    """
    collection = get_col()
    res = collection.update_one({'_id': ObjectId(clientID)},
                                {
                                    '$addToSet': {
                                        'records': {'program_id': programID, 'username': username, 'password': password,
                                                    'sec_level': sec_level}
                                    }
                                })
    return res.modified_count == 1


@handle_general_eror
def cange_record(clientID, programID, username=None, password=None):
    d = {}
    if username is not None:
        d['records.$.username'] = username
    if password is not None:
        d['records.$.password'] = password
    collection = get_col()
    res = collection.update_one(
        {
            '_id': ObjectId(clientID),
            'records': {'$elemMatch': {'program_id': programID}}
        },
        {'$set': d}
    )
    return res.modified_count == 1


@handle_general_eror
def get_record(clientID, programID):
    """
    get record from database
    :param clientID: the client to get the record from
    :param programID: the program identifier to get the cradentials to
    :return: username and password for the program or None if user dont exzist. True if record will be deleted, False otherwise
    """
    collection = get_col()
    prog = collection.find_one({'_id': ObjectId(clientID)}, {'records': {'$elemMatch': {'program_id': programID}}})
    if prog is None:
        return None

    elif u'records' in prog:
        return json.loads(json_util.dumps(prog[u'records'][0]))
    else:
        return {}


@handle_general_eror
def delete_record(clientID, programID):
    """
    delete record from database. delete just after x time.
    :param clientID: the client to get the record from
    :param programID: the program identifier to get the cradentials to
    :return: True if succeed, false otherwise
    """
    collection = get_col()
    res = collection.update_one(
        {
            '_id': ObjectId(clientID),
            'records': {'$elemMatch': {'program_id': programID}}
        },
        {'$set': {"records.$.delete_time": datetime.utcnow()}}
    )
    return res.modified_count == 1


@handle_general_eror
def get_all_records(clientID):
    """
    get all username program id pairs (with delete time if exist)
    :param str clientID: the client id
    :return list: list of dictionaries of the records
    """
    collection = get_col()
    prog = collection.find_one({'_id': ObjectId(clientID)},
                               {'records.program_id': 1, 'records.username': 1, 'records.delete_time': 1,
                                'records.sec_level': 1, 'delete_time': 1, "_id": 0})
    if prog is None:
        return None
    return json.loads(json_util.dumps(prog))


@handle_general_eror
def delete_user(clientID):
    """
    delete user after few days from action
    :param clientID: the client id to delete
    :return bool: True if update seceded, False otherwise
    """
    collection = get_col()
    ret = collection.update_one({'_id': ObjectId(clientID)}, {'$set': {'delete_time': datetime.utcnow()}})
    return ret.modified_count == 1


@handle_general_eror
def cancel_delete(clientID):
    """
    cancel user deletion time
    :param clientID: the client id to undelete
    :return bool: True if update seceded, False otherwise
    """
    collection = get_col()
    ret = collection.update_one({'_id': ObjectId(clientID)}, {'$unset': {'delete_time': ""}})
    return ret.modified_count == 1


def _immidiate_delete(clientID):
    """
    immediately delete user FOR TEST ONLY!!
    """
    collection = get_col()
    return collection.delete_one({'_id': ObjectId(clientID)})
