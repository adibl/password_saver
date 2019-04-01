"""
name: adi bleyer
date: =30.12.18
user managmet requests handler

"""
from Autentication.Password.request import AuthenticatedRequestPassword
from Autentication.request import AuthenticatedRequest
from UserManagment.API import Register, Login, Reset
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
            request = Request(request)
            data = request.get_data_as_dictionery()
            if type(data) is dict:
                if 'question' in data and 'answer' in data:
                    return OK
            return UNEXPECTED_ENTITY
        return UNAUTHORIZED #FIXME: if auterization is in the wrong level what to do



    def get_question_ans(self):
        request = Request(self.request)
        return request.get_data_as_dictionery()['question'],  request.get_data_as_dictionery()['answer']


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


class ResetRequest(Request):
    ResorceURI = [Reset.URI]

    @classmethod
    def IsResorceURL(cls, request):
        request = Request(request)
        return any([True for uri in cls.ResorceURI if uri.match(request.get_URI())])

    @classmethod
    def validate(cls, request):
        return super(ResetRequest, cls).validate(request) #FIXME: add somthing

    def process_request(self):
        """
        proses resource request
        :return str: the response
        """
        if Reset.is_uri(self.get_URI()):
            return Reset(self).handle_request()
        else:
            return Responce.not_found()
