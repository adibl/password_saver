"""
name:
date:
description
"""
import FA
from server.Autentication.JWT.request import AuthenticatedRequestJWT
from server.Autentication.Password.request import AuthenticatedRequestPassword
from server.HTTPtolls import *
from server.request import AuthenticatedRequestScema


class AuthenticatedRequest(AuthenticatedRequestScema):
    SEC_LEVEL = {AuthenticatedRequestJWT: 0, AuthenticatedRequestPassword: 1}

    @classmethod
    def is_fit(cls, request):
        if AuthenticatedRequestPassword.is_fit(request):
            backend = AuthenticatedRequestPassword(request)
        elif AuthenticatedRequestJWT.is_fit(request):
            backend = AuthenticatedRequestJWT(request)
        else:
            logging.debug('dont fit to any of the Autentication metodes')
            return UNAUTHORIZED
        return backend

    @classmethod
    def validate(cls, request):
        return cls.is_fit(request).validate(request)

    def __init__(self, request):
        """
        create Autenticated request that provide all nececery interface.

        :param request: the request string
        """
        super(AuthenticatedRequest, self).__init__(request)
        if AuthenticatedRequestPassword.is_fit(request):
            self.backend = AuthenticatedRequestPassword(request)
        elif AuthenticatedRequestJWT.is_fit(request):
            self.backend = AuthenticatedRequestJWT(request)
        else:
            raise ValueError
            pass  # FIXME: waht to do here????

    def get_user_id(self):
        """
        get the user id from JWT
        :return:
        """
        return self.backend.get_user_id()

    def get_sec_level(self):
        """
        get the autentication methode sec level

        :return: the user sec level
        :rtype: int
        """
        return self.SEC_LEVEL[type(self.backend)]

    def verify_2FA(self):
        return FA.verify()
