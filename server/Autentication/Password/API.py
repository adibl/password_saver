"""
name:
date:
description
"""

import database
import base64
from server.HTTPtolls import *
from server.database_errors import *


class passwordAutentication:

    @staticmethod
    def add(username, password):
        return database.add(username, password)

    @staticmethod
    def validate(username, password):
        ret = database.validate(username, password)
        if ret == database.USERNAME_OR_PASSWORD_INCORRECT:
            return UNEXPECTED_ENTITY
        elif ret == None:
            return INTERNAL_ERROR
        elif ret in ERRORS:
            return ret
        else:
            return OK

    @staticmethod
    def get_id(username, password):
        return database.validate(username, password)

    @staticmethod
    def delete(userID):
        return database.delete_user(userID)

    @classmethod
    def get_username_password(cls, auto):
        """
        get user username and password from request
        :param str request: the request string
        :return: username, password tuple
        """
        auto += '=' * (len(auto) % 4)
        username_password = base64.b64decode(auto)
        if ':' in username_password:
            return username_password.split(':')
        else:
            return None



