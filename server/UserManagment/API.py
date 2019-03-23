"""
name:
date:
description
"""
import logging
import re
import base64

from server.Autentication.Password import database
from server.HTTPtolls import *
from server.Autentication.Password.API import passwordAutentication


class Register(Uri):
    URI = re.compile('^/register$')
    METODES = ['GET']

    MIN_LEN = 8
    RE_CHRACTERS = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])')
    PASS_POLICY ='must contain 6-20 characters\r\n1 capital letter\r\n1 letter\r\n1 difit'

    def GET(self):
        """
        register to the service
        :return str: the responce
        """
        ret = self.__get_username_password()
        if ret is None:
            logging.debug('username password is formated wrong')
            return Responce.bad_request() #FIXME: what this is realy
        username, password = ret
        if re.match(self.RE_CHRACTERS, password):
            ret = database.add(username, password)
            if ret == database.USERNAME_ALREADY_EXZIST:
                return Responce.unexpected_entity({USERNAME: 'username already exzist'})
            elif ret is None:
                return Responce.internal_eror()
            else:
                return Responce.ok()
        else:
            return Responce.unexpected_entity({PASS: self.PASS_POLICY})

    def __get_username_password(self):
        return self.request.get_username_password()