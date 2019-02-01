"""
name:
date:
description
"""
import validate
from server.HTTPtolls import *

def handle_client(data):
    """
    :param data: the client request
    :return: the needed responce
    """
    data = data.replace('\r\n', '\n')
    val = validate.ValidateResorce(data)
    code = val.validate()
    return code_to_responce(code, data)



