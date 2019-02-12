"""
name: adi bleyer
date: =30.12.18
validate the request with re.
have defs to extract the data from the request.

"""
import re
import logging
from server.Autentication.request import AuthenticatedRequest
from server.HTTPtolls import *
from API import PasswordsUri, ProgramUri
# regex


class ResorceRequest(AuthenticatedRequest):
    ResorceURI = [PasswordsUri.URI, ProgramUri.URI]

    @classmethod
    def IsResorceURL(clt, request):
        request = AuthenticatedRequest(request)
        return any([True for uri in clt.ResorceURI if uri.match(request.get_URI())])

    @classmethod
    def validate(clt, request):
        status = super(AuthenticatedRequest, clt).validate(request)
        if status is OK:
            return clt.IsResorceURL(request)
        else:
            return status

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












