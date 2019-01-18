"""
name:
date:
description
"""
import pymongo
URL= 'mongodb://admin:cbOyyIRfWXOJSrNF@passsaver-shard-00-00-k4jpt.mongodb.net:27017,passsaver-shard-00-01-k4jpt.mongodb.net:27017,passsaver-shard-00-02-k4jpt.mongodb.net:27017/test?ssl=true&replicaSet=passSaver-shard-0&authSource=admin&retryWrites=true'
def connect():
    global client
    client = pymongo.MongoClient(URL)


def add_customer(user_name):
    pass_database = client["pass"]
    costumer_col = pass_database["customers"]
    mydict = {"user_name": user_name}
    x = costumer_col.insert_one(mydict)
    print(client.list_database_names())
    return True


