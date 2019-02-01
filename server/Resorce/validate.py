"""
name: adi bleyer
date: =30.12.18
validate the request with re.
have defs to extract the data from the request.

"""
import re
import logging
from server.Autentication.validate import ValidateAuthentication
from server.HTTPtolls import *
# regex


class ValidateResorce(ValidateAuthentication):
    ResorceURI = ['/password', "/client/try"]
    @classmethod
    def IsResorceURL(clt, request):
        return any([True for uri in clt.ResorceURI if uri in request.get_URI()])


    def validate(self):
        status = super(ValidateAuthentication, self).validate()
        if status is OK:
            return self.__validate_URI()
        else:
            return status

    def __validate_URI(self):
        verb = self.get_verb()
        uri = [uri for uri in self.ResorceURI if uri in self.get_URI()]
        print uri
        if len(uri) == 1:
            if verb in URI_PREMITED_LIST[uri[0]]:
                return OK

            else:
                logging.debug('resource validation fail, invalid verb')
                return METHOD_NOT_ALLOWED
        else:
            logging.debug('resource validation fail, invalid uri')
            return NOT_FOUND












