"""
name:
date:
description
"""
from server.request import AuthenticatedRequestScema
from server.Autentication.JWT.request import AuthenticatedRequestJWT
from server.Autentication.Password.request import AuthenticatedRequestPassword


class AuthenticatedRequest(AuthenticatedRequestScema):
    SEC_LEVEL = {AuthenticatedRequestJWT: 0, AuthenticatedRequestPassword: 1}

    @classmethod
    def validate(cls, request):
        if AuthenticatedRequestPassword.is_fit(request):
            backend = AuthenticatedRequestPassword(request)
        elif AuthenticatedRequestJWT.is_fit(request):
            backend = AuthenticatedRequestJWT(request)
        else:
            return None
        return backend.validate(request)

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
            pass #FIXME: waht to do here????

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











