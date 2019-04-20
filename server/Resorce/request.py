"""
name: adi bleyer
date: =30.12.18
validate the request with re.
have defs to extract the data from the request.

"""
from API import PasswordsUri, ProgramUri
from server.Autentication.request import AuthenticatedRequest
from server.HTTPtolls import *
from server.request import Request


class ResorceRequest(AuthenticatedRequest):
    ResorceURI = [PasswordsUri.URI, ProgramUri.URI]

    @classmethod
    def IsResorceURL(cls, request):
        request = Request(request)
        return any([True for uri in cls.ResorceURI if uri.match(request.get_URI())])

    def process_request(self):
        """
        proses resource request
        :return str: the response
        """
        if ProgramUri.is_uri(self.get_URI()):
            responce = ProgramUri(self).handle_request()
        elif PasswordsUri.is_uri(self.get_URI()):
            responce = PasswordsUri(self).handle_request()
        else:
            return Responce.not_found()
        return responce
