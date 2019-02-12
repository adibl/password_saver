"""
name:
date:
description
"""
import re
import logging
from server.Autentication import JWT
from server.request import Request

OK = 200
METHOD_NOT_ALLOWED = 405
BAD_REQUEST = 400
NOT_FOUND = 404
UNAUTHORIZED = 401


class AuthenticatedRequest(Request):
    RE_JWT = re.compile(r"^Authorization: Bearer (.*)$", re.M)

    @classmethod
    def validate(clt, request):
        status = super(AuthenticatedRequest, clt).validate(request)
        if status is OK:
            if clt.__validate_Authentication(request):
                request = AuthenticatedRequest(request)
                jwt = request.get_JWT()
                if JWT.validate(jwt):
                    return OK
                else:
                    logging.debug('JWT is wrong')
                    return UNAUTHORIZED
            else:
                logging.debug('Authentication header missing or wrong')
                return BAD_REQUEST
        else:
            return status

    @classmethod
    def __validate_Authentication(clt, request):
        """
        validate Autentication header structure
        :param str request: the client request
        :return: True if structure is valid, false otherwise
        """
        return bool(clt.RE_JWT.search(request))

    def get_JWT(self):
        """
        :param request: the client full request
        :return: JWT if fount False otherwise
        :rtype: str
        """
        if self.RE_JWT.search(self.request):
            return self.RE_JWT.search(self.request).group(1)

    def get_JWT_data(self):
        """
        return the JWT payload data
        :return dict: dictionery of JWT payload
        """
        return JWT.get_data(self.get_JWT())

    def is_user_exzist(self):
        """
        check if the user in the JWT is exzist
        :return: True if the user exzist, False otherwise
        """
        pass #FIXME: add check if user exzist in username password database

