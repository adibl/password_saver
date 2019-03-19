"""
name:
date:
description
"""
import logging
import re

import database
from server.HTTPtolls import *

class password():

    @staticmethod
    def create(username, password):
        return database.add(username, password)

    @staticmethod
    def validate(username, password):
        return database.validate(username, password)

    @staticmethod
    def delete(userID):
        return database.delete_user(userID)



