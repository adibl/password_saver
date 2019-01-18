"""
name:
date:
description
"""
import ast
import logging
from jwcrypto import jwt, jwk, jwe, jws
import database


def decrypte(Token, key, enc_key):
    E = jwe.JWE(algs=["RSA-OAEP", "A128CBC-HS256"])
    E.deserialize(Token, key=enc_key)
    raw_payload = E.payload
    S = jwt.JWT(check_claims={'exp': None, 'iat': None, 'iss': None}, algs=['HS256'])
    try:
        S.deserialize(raw_payload, key=key)
    except jwt.JWTMissingClaim as eror:
        logging.warning('send invalid token:' + str(eror))
        print eror
        return False
    final_payload = S.claims
    print final_payload
    return final_payload


def validate(Token, key, enc_key):
    Token = decrypte(Token, key, enc_key)
    if Token is False:
        return False
    Token = ast.literal_eval(Token)
    return Token