"""
name:
date:
description
"""
from fysom import FysomGlobalMixin, FysomGlobal, Fysom
#from client.API.Register import Register
#from client.GUI.Register import RegisterGui
#from client.GUI.main_page import SeaofBTCapp


fsm = Fysom({ 'initial': 'login', 'final': 'end',
              'events': [
                    {'name': 'registered', 'src': 'register', 'dst': 'login'},

                    {'name': 'to_register', 'src': 'login', 'dst': 'register'},
                    {'name': 'logedin', 'src': 'login', 'dst': 'see_all'},
                    {'name': 'insert_pass', 'src': 'see_all', 'dst': 'end'},
              ] })


shadow_fsm = Fysom({ 'initial': 'key_logger', 'final': 'end',
              'events': [
                    {'name': 'insert', 'src': 'key_logger', 'dst': 'insert_username'},
                    {'name': 'no_url', 'src': 'insert_username', 'dst': 'key_logger'},
                    {'name': 'username_inserted', 'src': 'insert_username', 'dst': 'insert_password'},
                    {'name': 'password_inserted', 'src': 'insert_password', 'dst': 'key_logger'},
                    {'name': 'close', 'src': '.', 'dst': 'end'},
                    {'name': 'home', 'src': 'key_logger', 'dst': 'add_record'},
              ] })





