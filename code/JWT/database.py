"""
name:
date:
description
"""
database = {}

def read_iss(iss):
    if iss in database.keys():
        return database[iss]
    else:
        return None

def write_iss(iss, time):
    database[iss] = time