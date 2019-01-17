"""
name:
date:
description
"""
import create
import ast
from jwcrypto import jwt, jwk
import database
import time

def decrypte(Token, key):
    key = jwk.JWK(**ast.literal_eval(key))
    ET = jwt.JWT(key=key, jwt=Token, check_claims={'exp': None, 'iss': None, 'iat': None})
    return ET.claims


def validate(Token, key):
    Token = decrypte(Token, key)
    Token = ast.literal_eval(Token)
    if Token['iat'] > database.read_iss(Token['iss']):
        return True
    return False