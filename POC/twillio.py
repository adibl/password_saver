from authy.api import AuthyApiClient

authy_api = AuthyApiClient('hAXCd8GH1hrNNbVs6dkm8gEHK49WxPKu')


def create():
    user = authy_api.users.create('bleyer23@gmail.com', '547-893-215', 972)  # email, cellphone, country_code

    if user.ok():
        print user.id
    else:
        print user.errors()


def verify():
    user_id = 137156574
    token = raw_input()
    verification = authy_api.tokens.verify(user_id, token)
    print verification.ok()


verify()
