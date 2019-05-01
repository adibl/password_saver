"""
name:
date:
description
"""
import re

from server import database_errors
from server.Autentication.JWT import create
from server.Autentication.Password import database as errors
from server.Autentication.Password.API import passwordAutentication as database
from server.HTTPtolls import *
from server.database_errors import *
from server.Autentication.JWT import database as jwt_database


class Register(Uri):
    URI = re.compile('^/register$')
    METODES = ['POST']

    MIN_LEN = 8

    def POST(self):
        """
        register to the service
        :return str: the responce
        """
        ret = self.__get_username_password()
        if ret is None:
            logging.debug('username password is formated wrong')
            return Responce.bad_request()  # FIXME: what this is really
        username, password = ret
        question, ansear = self.request.get_question_ans()
        ret = self.test_password(password)
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

    @staticmethod
    def test_password(password):
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
    METODES = ['GET', 'PATCH']

    def GET(self):
        data = self.request.get_data_as_dictionery()
        if data is None:
            return Responce.unexpected_entity({'username': 'username must be in data'})
        elif 'username' not in data:
            return Responce.unexpected_entity({'username': 'username must be in data'})
        q = database.get_question(data['username'])
        if q == errors.USERNAME_OR_PASSWORD_INCORRECT:
            return Responce.unexpected_entity({USERNAME: 'username is wrong'})
        if q in ERRORS:
            return Responce.validate_erors(q)
        return Responce.ok({'question': q})


    def PATCH(self):
        data = self.request.get_data_as_dictionery()
        if 'answer' in data and 'username' in data:
            ret = database.validate_question(data['username'], data['answer'])
            if ret is OK:
                id = database.get_id_without_password(data['username'])
                changelist = {}
                if 'NewUsername' in data:
                    changelist['username'] = data['NewUsername']
                if 'NewPassword' in data:
                    ret = Register.test_password(data['NewPassword'])
                    if ret is not True:
                        return Responce.unexpected_entity({'password': ret})
                    changelist['password'] = data['NewPassword']
                if len(changelist) > 0:
                    if database.change_user_cradencials(id, **changelist):
                        jwt_database.add(id)
                        return Responce.ok()
                    else:
                        return Responce.internal_eror()
                else:
                    return Responce.unexpected_entity({'general': 'must have new username or new password'})
            elif ret == errors.USERNAME_OR_PASSWORD_INCORRECT:
                return Responce.unexpected_entity({'username': 'username is wrong'})
            elif ret == errors.WRONG_ANSWER:
                return Responce.unexpected_entity({'answer': 'answer is wrong'})
            else:
                return Responce.validate_erors(ret)
        else:
            return Responce.unexpected_entity({'general': 'answer and old username fields must be in request'})


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
