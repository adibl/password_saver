"""
name:
date:
description
"""
import ast
import logging
from jwcrypto import jwt, jwe, jwk
from jwcrypto.common import json_decode
import os
from database import validate as validate_JWT_time

with open(os.path.join(os.path.dirname(__file__), 'public_signing.pem'), 'rb') as f: #FIXME: take files from other directory
    KEY = json_decode(f.read())
with open(os.path.join(os.path.dirname(__file__), 'public_encrypte_private.pem'), 'rb') as f:
    ENC_KEY = json_decode(f.read())

def decrypte(Token):
    """
    :param string Token: raw string of JWE token
    :return: False if the token is not valid, and JWS token string otherwise
    """
    E = jwe.JWE(algs=["RSA-OAEP", "A128CBC-HS256"])
    v= jwk.JWK()
    v.import_key(**ENC_KEY)
    try:
        E.deserialize(Token, key=v)
    except jwe.JWException as err:
        logging.warning('sent invalid JWE:' + str(err))
        return False
    raw_payload = E.payload
    S = jwt.JWT(check_claims={'exp': None, 'iat': None, 'iss': None}, algs=['HS256'])
    try:
        S.deserialize(raw_payload, key=jwk.JWK(**KEY))
    except jwt.JWTClaimsRegistry as eror:
        logging.warning('send invalid JWS:' + str(eror))
        return False
    final_payload = S.claims
    return final_payload


def validate(Token):
    """
    :param string Token: raw string of JWE token
    :return: True if the token is valid, false otherwise
    """
    Token = decrypte(Token)
    if Token is False:
        return False
    Token = ast.literal_eval(Token)
    if not validate_JWT_time(Token['iss'], Token['iat']):
        return False
    return True