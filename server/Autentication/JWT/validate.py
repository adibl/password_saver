"""
name:
date:
description
"""
import ast
import logging
from jwcrypto import jwt, jwe, jwk
import json
from jwcrypto.common import json_decode

with open('public_signing.pem', 'rb') as f: #FIXME: take files from other directory
    KEY = json_decode(f.read())
with open('public_encrypte_private.pem', 'rb') as f:
    ENC_KEY = json_decode(f.read())

def decrypte(Token):
    E = jwe.JWE(algs=["RSA-OAEP", "A128CBC-HS256"])
    v= jwk.JWK()
    v.import_key(**ENC_KEY)
    print v.has_public
    print v.export_public()
    E.deserialize(Token, key=v)
    raw_payload = E.payload
    S = jwt.JWT(check_claims={'exp': None, 'iat': None, 'iss': None}, algs=['HS256'])
    try:
        S.deserialize(raw_payload, key=jwk.JWK(**KEY))
    except jwt.JWTMissingClaim as eror:
        logging.warning('send invalid token:' + str(eror))
        print(eror)
        return False
    final_payload = S.claims
    return final_payload


def validate(Token):
    Token = decrypte(Token)
    if Token is False:
        return False
    Token = ast.literal_eval(Token)
    return True