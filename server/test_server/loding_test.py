"""
name:
date:
description
"""
#  locust -f D:\adi\Documents\password_saver\server\test_server\loding_test.py --host=http://example.com

from locust import HttpLocust, TaskSet
import os


def get_user(l):
    h = {'Authorization': 'Bearer eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkExMjhDQkMtSFMyNTYiLCJ0eXAiOiJKV0UifQ.ubiJs2_ty808XU1j95AouKvSNJ3Ii9MDnI67MMn4P_ROzJ0ITCOoFyOwInXv1ZnClA1egt82mVYDlmt5DKA7Fw8F9FQtwboBxEhs4p8A0hsgtAtsEeqguGtkpbIQNFN4spdC7lfhFhl2R8hYQEyCeecRvrFD0mfNoYHpOEwmgeVnwlvLHQWQ-XQIuJGvTPxG9t3ub81GRf6oqEjQ7HUZ3jShSeXCQ7P-FPEoNwxDErPK_qai8rHc3V9WVSVXm7iwc58tLrJX_rcwnDO8HYb8AasBqvs9PdM7GYrwFVIteltmFJfXf2pp9w0yO7JMMkdQ5TS0p0c4WrhkGBno0vAkhQ.fuEb6fVyJ5Z5GzbFS9vcuQ.7UKmYWBpDz_kq_j0UYafGZHM0m-kkkfuggZaZWf7cF6RH4ODp4ZrPSdogRRG3pvN4on_X-qF6kgDolnr-E22sobsxQ52IkjfYjdxot0a_IMjEY-YLzq59sRXk-ev43lHwtQdwwH9zW5Hwdccf_DYXGOmvp-O4odzjlc69xNgifrPhrKoVQo5Bp-A69KVT1bAkgrhzIwBRuS59H97yNd2ISSXOELV7infIUNrVMacoggWirJlBD591Y_-X7Uouerw.RDY3WkfGsRdKnSIojSbtaQ',
         'Content-Type' : 'application/json'

         }
    l.client.get("http://127.0.0.1:50008/client/try", headers=h)

class UserBehavior(TaskSet):
    tasks = {get_user: 3}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1
    max_wait = 10


if __name__ == '__main__':
    os.system('locust --help')