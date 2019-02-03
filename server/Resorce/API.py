"""
name:
date:
description
"""
import request
from server.HTTPtolls import *
from request import ResorceRequest
import re
import database
import logging

URI_GENERAL = re.compile('^/passwords$')
URI_PROGRAM = re.compile('^/passwords/(.*)$')

def process_request(request):
    if programUri.is_uri(request.get_URI()):
        responce = programUri(request).handle_request()
    elif PasswordsUri.is_uri(request.get_URI()):
        responce = PasswordsUri(request).handle_request()
    else:
        return Responce.not_found()
    return responce


class PasswordsUri(Uri):
    URI = re.compile('^/passwords$')

    def handle_request(self):
        metode = self.request.get_verb()
        if metode == 'GET':
            return self.GET()
        else:
            return Responce.not_found()

    def GET(self):
        clientID = self.request.get_JWT_data()['iss']
        data = database.get_all_records(clientID)
        if data is None:
            logging.critical('user id {0} send valid JWT but the user not exzisting'.format(clientID))
            return Responce.not_found() #FIXME: user dont exzist is not found ????
        else:
            s = ''
            s += "HTTP/1.1 200 OK\r\n"
            s += str(data)
            s += "\r\n"
            return s

class programUri(Uri):
    URI = re.compile('^/passwords/(.*)$')




    def handle_request(self):
        metode = self.request.get_verb()
        if metode == 'GET':
            return self.GET()
        else:
            return Responce.not_found()

    def GET(self):
        uri = self.request.get_URI()
        clientID = self.request.get_JWT_data()['iss']
        programID = self.URI.match(uri).group(1)
        data = database.get_record(clientID, programID)
        if data is None:
            logging.critical('user id {0} send valid JWT but the user not exzisting'.format(clientID))
            return Responce.not_found() #FIXME: user dont exzist is not found ????
        if len(data) == 0:
            return Responce.not_found()
        else:
            s = ''
            s += "HTTP/1.1 200 OK\r\n"
            s += str(data)
            s += "\r\n"
            return s










