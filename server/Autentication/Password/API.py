"""
name:
date:
description
"""

import base64

import database
from server.HTTPtolls import *
from server.database_errors import *
class passwordAutentication:

    @staticmethod
    def add(username, password, question, ans):
        return database.add(username, password, question, ans)

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
    def validate_question(username, ans):
        ret = database.validate_question(username, ans)
        if ret in [database.USERNAME_OR_PASSWORD_INCORRECT, database.WRONG_ANSWER]:
            return ret
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
    def get_id_without_password(username):
        return database.get_id(username)

    @staticmethod
    def get_question(username):
        return database.get_question(username)

    @staticmethod
    def delete(userID):
        return database.delete_user(userID)

    @staticmethod
    def change_user_cradencials(clientID, username=None, password=None):
        return database.change_user_cradencials(clientID, username, password)
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
