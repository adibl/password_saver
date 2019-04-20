"""
name:
date:
description
"""
import json
from datetime import datetime

import pymongo
from bson import json_util
from bson.objectid import ObjectId

from server.database_errors import *

MAX_TIMEOUT = 24 * 5  # FIXME move to create file
CONN_STR = 'mongodb://admin:LBGpC.hSJ2xvDk_@passsaver-shard-00-00-k4jpt.mongodb.net:27017,passsaver-shard-00-01-k4jpt.mongodb.net:27017,passsaver-shard-00-02-k4jpt.mongodb.net:27017/test?ssl=true&replicaSet=passSaver-shard-0&authSource=admin&retryWrites=true'


def connect(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        client = pymongo.MongoClient(CONN_STR)
        db = client.Resorce
        record = db['users']
        ret = f(record, *args, **kwds)
        client.close()
        return ret

    return wrapper


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
@connect
def add_user(collection, userID):
    """
    :param userID: the user ID to create the collection for
    :return: True ifg the client was created, False if he is already exzist
    """
    col = collection.insert_one({'_id': ObjectId(userID), 'records': []})
    return True


@handle_general_eror
@connect
def add_record(collection, clientID, programID, username, password, sec_level=0):
    """
    :param clientID: the client ID
    :param programID: the program identifier
    :param username: the client username to the program
    :param password: the client password to the program
    :param sec_level: the security level of this record
    :return bool: True if update seceded False otherwise
    """
    res = collection.update_one({'_id': ObjectId(clientID)},
                                {
                                    '$addToSet': {
                                        'records': {'program_id': programID, 'username': username, 'password': password,
                                                    'sec_level': sec_level}
                                    }
                                })
    return res.modified_count == 1


@handle_general_eror
@connect
def cange_record(collection, clientID, programID, username=None, password=None):
    d = {}
    if username is not None:
        d['records.$.username'] = username
    if password is not None:
        d['records.$.password'] = password
    res = collection.update_one(
        {
            '_id': ObjectId(clientID),
            'records': {'$elemMatch': {'program_id': programID}}
        },
        {'$set': d}
    )
    return res.modified_count == 1


@handle_general_eror
@connect
def get_record(collection, clientID, programID):
    """
    get record from database
    :param clientID: the client to get the record from
    :param programID: the program identifier to get the cradentials to
    :return: username and password for the program or None if user dont exzist. True if record will be deleted, False otherwise
    """
    prog = collection.find_one({'_id': ObjectId(clientID)}, {'records': {'$elemMatch': {'program_id': programID}}})
    if prog is None:
        return None

    elif u'records' in prog:
        return json.loads(json_util.dumps(prog[u'records'][0]))
    else:
        return {}


@handle_general_eror
@connect
def delete_record(collection, clientID, programID):
    """
    delete record from database. delete just after x time.
    :param clientID: the client to get the record from
    :param programID: the program identifier to get the cradentials to
    :return: True if succeed, false otherwise
    """
    res = collection.update_one(
        {
            '_id': ObjectId(clientID),
            'records': {'$elemMatch': {'program_id': programID}}
        },
        {'$set': {"records.$.delete_time": datetime.utcnow()}}
    )
    return res.modified_count == 1


@handle_general_eror
@connect
def get_all_records(collection, clientID):
    """
    get all username program id pairs (with delete time if exist)
    :param str clientID: the client id
    :return list: list of dictionaries of the records
    """
    prog = collection.find_one({'_id': ObjectId(clientID)},
                               {'records.program_id': 1, 'records.username': 1, 'records.delete_time': 1,
                                'records.sec_level': 1, 'delete_time': 1, "_id": 0})
    if prog is None:
        return None
    return json.loads(json_util.dumps(prog))


@handle_general_eror
@connect
def delete_user(collection, clientID):
    """
    delete user after few days from action
    :param clientID: the client id to delete
    :return bool: True if update seceded, False otherwise
    """
    ret = collection.update_one({'_id': ObjectId(clientID)}, {'$set': {'delete_time': datetime.utcnow()}})

    return ret.modified_count == 1


@handle_general_eror
@connect
def cancel_delete(collection, clientID):
    """
    cancel user deletion time
    :param clientID: the client id to undelete
    :return bool: True if update seceded, False otherwise
    """
    ret = collection.update_one({'_id': ObjectId(clientID)}, {'$unset': {'delete_time': ""}})
    return ret.modified_count == 1


@connect
def _immidiate_delete(collection, clientID):
    """
    immediately delete user FOR TEST ONLY!!
    """
    return collection.delete_one({'_id': ObjectId(clientID)})
