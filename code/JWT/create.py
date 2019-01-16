"""
name:
date:
description
"""
from jwcrypto import jwk, jwt
import time
EXP_TIME_MIN = 25

def create(userID):
    """
    bild JWT token from user cradentials
    :param str userID:
    :return:
    """
    header = {}
    header['alg'] = 'HS256'
    header['typ'] = "JWT"
    body ={}
    body['iss'] = userID
    body['iat'] = int(time.time())
    body['exp'] = body['iat'] + EXP_TIME_MIN * 60
    key = jwk.JWK(generate='oct', size=256)
    Token = jwt.JWT(header=header,
                    claims=body)
    Token.make_signed_token(key)
    return Token.serialize(), key.export()