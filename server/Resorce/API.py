"""
name:
date:
description
"""
import logging
import re

import database
from server.HTTPtolls import *




class PasswordsUri(Uri):
    URI = re.compile('^/passwords$')
    METODES = ['GET', 'POST']

    def GET(self):
        """
        get all the program ID and the usernames
        :return str: the responce
        """

        clientID = self.request.get_JWT_data()['iss']
        data = database.get_all_records(clientID)
        if data is None:
            logging.critical('user id {0} send valid JWT but the user not exzisting'.format(clientID))
            return Responce.unauthorized()
        else:
            return Responce.ok(data)


    def POST(self):
        """
        post new password, username, program id record to database
        :return str: the response 200 ok or 400 bad request
        """
        clientID = self.request.get_JWT_data()['iss']
        data = self.request.get_data_as_dictionery()
        if any(x in data.keys() for x in [USERNAME, PASS, PROGRAM]):
            if database.add_record(clientID, data[PROGRAM], data[USERNAME], data[PASS]):
                return Responce.ok()
        return Responce.bad_request()

    @staticmethod
    def delte_user(clientID): #FIXME: is needed???
        """
        delete the user from the databse
        :return bool: true if delete seceded, false otherwise
        """
        return database.delete_user(clientID)




class ProgramUri(Uri):
    URI = re.compile('^/passwords/(.*)$')
    METODES = ['GET', 'PATCH', 'DELETE']

    def GET(self):
        """
        get the program username and password
        :return str: http responce 200 or 404 or 401
        """
        uri = self.request.get_URI()
        clientID = self.request.get_JWT_data()['iss']
        programID = self.URI.match(uri).group(1)
        data = database.get_record(clientID, programID)
        if data is None:
            logging.critical('user id {0} send valid JWT but the user not exzisting'.format(clientID))
            return Responce.unauthorized()
        if len(data) == 0:
            return Responce.not_found()
        else:
            return Responce.ok(data)

    def PATCH(self):
        """
        cange program username or password
        :return str: http response 200 or 404
        """
        uri = self.request.get_URI()
        clientID = self.request.get_JWT_data()['iss']
        programID = self.URI.match(uri).group(1)
        data = self.request.get_data_as_dictionery()
        username, password = data.get(USERNAME), data.get(PASS)
        if database.cange_record(clientID, programID, username, password):
            return Responce.ok()
        else:
            # FIXME: dont have user not valid/ program not valid difference
            return Responce.not_found()

    def DELETE(self):
        """
        delete the program from user account
        :return str: http response 200 or 404
        """
        uri = self.request.get_URI()
        clientID = self.request.get_JWT_data()['iss']
        programID = self.URI.match(uri).group(1)
        if database.delete_record(clientID, programID):
            return Responce.ok()
        else:
            #FIXME: dont have user not valid/ program not valid difference
            return Responce.not_found()











