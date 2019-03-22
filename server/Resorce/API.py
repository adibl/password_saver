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

        clientID = self.request.get_user_id()
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
        clientID = self.request.get_user_id()
        data = self.request.get_data_as_dictionery()
        sec_level = self.request.get_sec_level()
        if any(x in data.keys() for x in [USERNAME, PASS, PROGRAM]):
            if database.add_record(clientID, data[PROGRAM], data[USERNAME], data[PASS], sec_level):
                return Responce.ok()
        return Responce.bad_request()




class ProgramUri(Uri):
    URI = re.compile('^/passwords/(.*)$')
    METODES = ['GET', 'PATCH', 'DELETE']

    def GET(self):
        """
        get the program username and password
        :return str: http responce 200 or 404 or 401
        """
        uri = self.request.get_URI()
        clientID = self.request.get_user_id()
        programID = self.URI.match(uri).group(1)
        sec_level = self.request.get_sec_level()
        data = database.get_record(clientID, programID)
        if data is None:
            logging.critical('user id {0} send valid JWT but the user not exzisting'.format(clientID))
            return Responce.unauthorized()
        elif len(data) == 0:
            return Responce.not_found()
        elif data['sec_level'] > sec_level:
            logging.debug('valid request with {0} sec level when {1} in neded'.format(sec_level, data['sec_level']))
            return Responce.unauthorized('SecLevel: ' + str(data['sec_level']))
        else:
            return Responce.ok(data)

    def PATCH(self):
        """
        cange program username or password
        :return str: http response 200 or 404
        """
        uri = self.request.get_URI()
        clientID = self.request.get_user_id()
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
        clientID = self.request.get_user_id()
        programID = self.URI.match(uri).group(1)
        if database.delete_record(clientID, programID):
            return Responce.ok()
        else:
            #FIXME: dont have user not valid/ program not valid difference
            return Responce.not_found()











