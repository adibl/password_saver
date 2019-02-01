"""
name:
date:
description
"""
import re
import logging
from server.Autentication.JWT import validate
from server.validate import Validate

RE_JWT = re.compile(r"^Authorization: Bearer (.*)$", re.M)

OK = 200
METHOD_NOT_ALLOWED = 405
BAD_REQUEST = 400
NOT_FOUND = 404
UNAUTHORIZED = 401





class ValidateAuthentication(Validate):
    def validate(self):
        status = super(ValidateAuthentication, self).validate()
        if status is OK:
            if self.__validate_Authentication():
                jwt = self.get_JWT()
                if validate(jwt):
                    return OK
                else:
                    logging.debug('JWT is wrong')
                    return UNAUTHORIZED
            else:
                logging.debug('Authentication header missing or wrong')
                return BAD_REQUEST
        else:
            return status



    def __validate_Authentication(self):
        """
        validate Autentication header structure
        :param str request: the client request
        :return: True if structure is valid, false otherwise
        """
        return bool(RE_JWT.search(self.request))

    def get_JWT(self):
        """
        :param request: the client full request
        :return: JWT if fount False otherwise
        :rtype: str
        """
        if RE_JWT.search(self.request):
            return RE_JWT.search(self.request).group(1)[:-1] #QUESTION: whay [:-1]