"""
name:
date:
description
"""
import re

from server import database_errors
from server.Autentication.JWT import create
from server.Autentication.Password.API import database as errors
from server.Autentication.Password.API import passwordAutentication as database
from server.HTTPtolls import *
from server.database_errors import *


class Register(Uri):
    URI = re.compile('^/register$')
    METODES = ['POST']

    MIN_LEN = 8
    RE_CHRACTERS = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])')
    PASS_POLICY = 'must contain 6-20 characters\r\n1 capital letter\r\n1 letter\r\n1 difit'

    def POST(self):
        """
        register to the service
        :return str: the responce
        """
        ret = self.__get_username_password()
        if ret is None:
            logging.debug('username password is formated wrong')
            return Responce.bad_request()  # FIXME: what this is realy
        username, password = ret
        question, ansear = self.request.get_question_ans()
        ret = self.__test_password(password)
        if ret is True:
            ret = database.add(username, password, question, ansear)
            if ret == database_errors.DUPLIKATE_KEY_ERROR:
                return Responce.unexpected_entity({USERNAME: 'username already exzist'})
            elif ret is None:
                return Responce.internal_eror()
            else:
                return Responce.ok()
        else:
            return Responce.unexpected_entity({PASS: ret})

    def __get_username_password(self):
        return self.request.get_username_password()

    def __test_password(self, password):
        """
        test password aginst the policy
        
        :param password: the password 
        :ret+=: True if the password is correct and string that represent the error otherwise
        """
        ret = []
        if not 6 <= len(password) <= 20:
            ret.append('must contain 6-20 characters')
        if not re.search("[a-z]", password):
            ret.append('must contain one small letter')
        if not re.search("[A-Z]", password):
            ret.append('must contain one big letter')
        if not re.search("[0-9]", password):
            ret.append('must contain one number')
        if not re.search("[!@#$%^&*]", password):
            ret.append('must contain one special character (!@#$%^&*)')
        if ret == []:
            return True
        else:
            print ret
            return '\r\n'.join(ret)


class Login(Uri):
    URI = re.compile('^/login')
    METODES = ['GET']

    def GET(self):
        """
        login to the service and get JWT
        :return str: the responce
        """
        identifier = self.request.get_user_id()
        if identifier is None:
            return Responce.unexpected_entity({
                                                  AUTENTICATION: 'invalid username password structure'})  # FIXME: eror if autentication cradentials are wrong
        jwt = create(identifier)
        return Responce.ok({AUTENTICATION: jwt})


class Reset(Uri):
    URI = re.compile('^/reset$')
    METODES = ['GET', 'POST']

    def GET(self):
        data = self.request.get_data_as_dictionery()
        if data is None:
            return Responce.unexpected_entity({'username': 'username must be in data'})  # FIXME: USER data is wrong
        elif 'username' not in data:
            return Responce.unexpected_entity({'username': 'username must be in data'})  # FIXME: USER data is wrong
        q = database.get_question(data['username'])
        if q == errors.USERNAME_OR_PASSWORD_INCORRECT:
            return Responce.unexpected_entity({USERNAME: 'username is wrong'})
        if q in ERRORS:
            return Responce.validate_erors(q)
        return Responce.ok({'question': q})

class Delete(Uri):
    URI = re.compile('^/delete$')
    METODES = ['DELETE']

    def DELETE(self):
        id = self.request.get_user_id()
        if id == 2:
            return Responce.unexpected_entity({'general': 'username or passwords is wrong'})
        elif database.delete(id):
            return Responce.ok()
        else:
            return Responce.internal_eror()
