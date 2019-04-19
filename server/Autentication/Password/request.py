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

    @classmethod
    def is_fit(cls, request):
        return cls.validate_Authentication(request)

    @classmethod
    def validate(cls, request):
        status = super(AuthenticatedRequestPassword, cls).validate(request)
        if status is OK:
            if cls.validate_Authentication(request):
                auto = cls.RE_VALIDATE.search(request).group(1)
                username_password = passwordAutentication.get_username_password(auto)
                if username_password is None:
                    logging.debug('username and password are wrong formated')
                    return BAD_REQUEST
                username, password = username_password
                return passwordAutentication.validate(username, password)
            else:
                logging.debug('Authentication header missing or wrong')
                return BAD_REQUEST
        else:
            return status

    def get_user_id(self):
        """
        get the user id from database
        :return: the user ID
        :rtype: str
        """
        username_password = self.get_username_password()
        if username_password is None:
            return None
        username, password = username_password
        return passwordAutentication.get_id(username, password)

    def get_username_password(self):
        auto = self.RE_VALIDATE.search(self.request).group(1)
        return passwordAutentication.get_username_password(auto)



