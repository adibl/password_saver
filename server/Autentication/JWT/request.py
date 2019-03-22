"""
name:
date:
description
"""
import logging
import re

from server.Autentication import JWT
from HTTPtolls import *
from server.request import AuthenticatedRequestScema


class AuthenticatedRequestJWT(AuthenticatedRequestScema):
    RE_VALIDATE = re.compile(r"^Authorization: Bearer (.*)$", re.M)
    SEC_LEVEL = 1

    @classmethod
    def is_fit(cls, request):
        return cls.validate_Authentication(request)

    @classmethod
    def validate(cls, request):
        status = super(AuthenticatedRequestJWT, cls).validate(request)
        if status is OK:
            if cls.validate_Authentication(request):
                request = AuthenticatedRequestJWT(request)
                jwt = request.__get_JWT()
                if JWT.validate(jwt):
                    return OK
                else:
                    logging.debug('JWT is wrong')
                    return UNAUTHORIZED
            else:
                logging.debug('Authentication header missing or wrong')
                return BAD_REQUEST #QUESTION: eror type if Autentication filed is wrong??
        else:
            return status

    def __get_JWT(self):
        """
        :param request: the client full request
        :return: JWT if fount False otherwise
        :rtype: str
        """
        if self.RE_VALIDATE.search(self.request):
            return self.RE_VALIDATE.search(self.request).group(1)

    def __get_JWT_data(self):
        """
        return the JWT payload data
        :return dict: dictionery of JWT payload
        """
        return JWT.get_data(self.__get_JWT())

    def get_user_id(self):
        """
        get the user id from JWT
        :return:
        """
        return JWT.get_data(self.__get_JWT())['iss']
