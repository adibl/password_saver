import authy

from authy.api import AuthyApiClient
authy_api = AuthyApiClient('LP6EuXNWArzMiCFBPkZi4kTr42UT77mt')

#create
user = authy_api.users.create('bleyer23@gmail.com', '547-893-215', 972) #email, cellphone, country_code
print user.id

user_id = user.id
message = "Require for login"
seconds_to_expire = 120

#validate user
response = authy_api.one_touch.send_request(user_id,
	                                        message,
	                                        seconds_to_expire=seconds_to_expire)

if response.ok():
    uuid = response.get_uuid()
    # do your stuff.
else:
    print response.errors()

#check token
token = raw_input()
verification = authy_api.tokens.verify(user.id, token)
print verification