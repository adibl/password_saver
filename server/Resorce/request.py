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
# regex


class ResorceRequest(AuthenticatedRequest):
    ResorceURI = ['/passwords', "/client/try"] #FIXME: take form the URI classes

    @classmethod
    def IsResorceURL(clt, request):
        request = AuthenticatedRequest(request)
        return any([True for uri in clt.ResorceURI if uri in request.get_URI()])

    @classmethod
    def validate(clt, request):
        status = super(AuthenticatedRequest, clt).validate(request)
        if status is OK:
            return clt.__validate_URI(request)
        else:
            return status

    @classmethod
    def __validate_URI(clt, request):
        request = AuthenticatedRequest(request)
        verb = request.get_verb()
        uri = [uri for uri in clt.ResorceURI if uri in request.get_URI()]
        if len(uri) == 1:
            if verb in URI_PREMITED_LIST[uri[0]]:
                return OK

            else:
                logging.debug('resource validation fail, invalid verb')
                return METHOD_NOT_ALLOWED
        else:
            logging.debug('resource validation fail, invalid uri')
            return NOT_FOUND












