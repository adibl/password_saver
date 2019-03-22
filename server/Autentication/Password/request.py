"""
name:
date:
description
"""
import logging
import re
import base64

from server.Autentication.Password.API import passwordAutentication
from HTTPtolls import *
from server.request import AuthenticatedRequestScema


class AuthenticatedRequestPassword(AuthenticatedRequestScema):
    RE_VALIDATE = re.compile(r"^Authorization: Basic (.*)$", re.M)
    SEC_LEVEL = 1

    @classmethod
    def is_fit(cls, request):
        return cls.validate_Authentication(request)

    @classmethod
    def validate(cls, request):
        status = super(AuthenticatedRequestPassword, cls).validate(request)
        if status is OK:
            if cls.validate_Authentication(request):
                request = AuthenticatedRequestPassword(request)
                username_password = cls.__get_username_password(request)
                if username_password is None:
                    return BAD_REQUEST #QUESTION: eror type if Autentication filed is wrong??
                username, password = username_password.split(':')
                ret = passwordAutentication.validate(username, password)
                if ret is None:
                    return NOT_FOUND #QUESTION: eror type if pass or username filed is wrong??
                else:
                    return OK
            else:
                logging.debug('Authentication header missing or wrong')
                return BAD_REQUEST #QUESTION: eror type if Autentication filed is wrong??
        else:
            return status

    def get_user_id(self):
        """
        get the user id from JWT
        :return:
        """
        username_password = self.__get_username_password(self.request)
        print username_password
        print type(username_password)
        if username_password is None:
            return None
        username, password = username_password
        return passwordAutentication.validate(username, password)


    @classmethod
    def __get_username_password(cls, request):
        auto = cls.RE_VALIDATE.search(request).group(1)
        auto += '='*(len(auto)%4)
        username_password = base64.b64decode(auto)
        print username_password
        print type(username_password)
        if ':' in username_password:
            return ':'.split(username_password)
        else:
            return None
