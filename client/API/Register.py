"""

"""
import base64

import requests
import json

URI = 'http://127.0.0.1:50007'

class Register(object):

    @classmethod
    def handle(cls, username, password, question, answer):
        return cls.POST(username, password, question, answer)


    @classmethod
    def POST(cls, username, password, question, answer):
        auto = base64.b64encode(username + ':' + password)
        responce = requests.post(URI + '/register', headers={'Authorization': 'Basic {0}'.format(auto)},
                                 json={'question': question, 'answer': answer})
        if responce.status_code == 200:
            return True
        elif responce.status_code == 442:
            return json.loads(responce.text)
        else:
            return {'general': 'general error'}