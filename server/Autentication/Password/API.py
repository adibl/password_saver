"""
name:
date:
description
"""

import database


class passwordAutentication:

    @staticmethod
    def create(username, password):
        return database.add(username, password)

    @staticmethod
    def validate(username, password):
        return database.validate(username, password)

    @staticmethod
    def delete(userID):
        return database.delete_user(userID)



