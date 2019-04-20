from authy.api import AuthyApiClient

global authy_api
authy_api = AuthyApiClient('hAXCd8GH1hrNNbVs6dkm8gEHK49WxPKu')


def create(email, cell, country_code=972):
    user = authy_api.users.create(email, cell, country_code=972)

    if user.ok():
        print user.id
    else:
        print user.errors()


def verify():
    user_id = 137156574
    token = raw_input()
    verification = authy_api.tokens.verify(user_id, token)
    return verification.ok()


def delete(authy_id):
    user = authy_api.users.delete(authy_id)
