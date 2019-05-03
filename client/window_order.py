"""
name:
date:
description
"""
from fysom import Fysom

# from client.API.Register import Register
# from client.GUI.Register import RegisterGui
# from client.GUI.main_page import SeaofBTCapp


fsm = Fysom({'initial': 'login', 'final': 'end',
             'events': [
                 {'name': 'registered', 'src': 'register', 'dst': 'login'},

                 {'name': 'to_register', 'src': 'login', 'dst': 'register'},
{'name': 'to_forgot_password', 'src': 'login', 'dst': 'get_security_question'},
{'name': 'got_question', 'src': 'get_security_question', 'dst': 'get_answer'},
{'name': 'finish', 'src': 'get_answer', 'dst': 'login'},
                 {'name': 'logedin', 'src': 'login', 'dst': 'see_all'},
                 {'name': 'edit', 'src': 'see_all', 'dst': 'edit'},
                 {'name': 'return', 'src': 'edit', 'dst': 'see_all'},
                {'name': 'to_delete', 'src': 'see_all', 'dst': 'delete_user'},
                 {'name': 'sucsees', 'src': 'delete_user', 'dst': 'end'},
             ]})

shadow_fsm = Fysom({'initial': 'key_logger', 'final': 'end',
                    'events': [
                        {'name': 'insert', 'src': 'key_logger', 'dst': 'insert_username'},
                        {'name': 'no_url', 'src': 'insert_username', 'dst': 'key_logger'},

                        {'name': 'username_inserted', 'src': 'insert_username', 'dst': 'insert_password'},
                        {'name': 'close', 'src': '.', 'dst': 'end'},
                        {'name': 'home', 'src': 'key_logger', 'dst': 'add_record'},
                        {'name': 'no_url', 'src': 'add_record', 'dst': 'key_logger'},
                        {'name': 'to_key_logger', 'src': 'add_record', 'dst': 'key_logger'},
                        {'name': 'already_exzist', 'src': 'add_record', 'dst': 'key_logger'},
                        {'name': 'to_key_logger', 'src': 'insert_password', 'dst': 'key_logger'},
                        {'name': 'close', 'src': '.', 'dst': 'end'},
                    ]})
