"""
name: adi bleyer
date: =30.12.18
user managmet requests handler

"""
from Autentication.Password.request import AuthenticatedRequestPassword
from Autentication.request import AuthenticatedRequest
from UserManagment.API import Register, Login
from server.request import Request
from server.HTTPtolls import *


class RegisterRequest(AuthenticatedRequestPassword):
    ResorceURI = [Register.URI]

    @classmethod
    def IsResorceURL(cls, request):
        request = Request(request)
        return any([True for uri in cls.ResorceURI if uri.match(request.get_URI())])

    @classmethod
    def validate(cls, request):
        if super(RegisterRequest, cls).is_fit(request):
            return OK
        return UNAUTHORIZED #FIXME: if auterization is in the wrong level what to do



    def process_request(self):
        """
        proses resource request
        :return str: the response
        """
        if Register.is_uri(self.get_URI()):
            return Register(self).handle_request()
        else:
            return Responce.not_found()


class LoginRequests(AuthenticatedRequestPassword):
    ResorceURI = [Login.URI]

    @classmethod
    def IsResorceURL(cls, request):
        request = Request(request)
        return any([True for uri in cls.ResorceURI if uri.match(request.get_URI())])

    @classmethod
    def validate(cls, request):
        if super(LoginRequests, cls).is_fit(request):
            return OK
        return UNAUTHORIZED  # FIXME: if auterization is in the wrong level what to do

    def process_request(self):
        """
        proses resource request
        :return str: the response
        """
        if Login.is_uri(self.get_URI()):
            return Login(self).handle_request()
        else:
            return Responce.not_found()