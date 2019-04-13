"""
name:
date:
description
"""
from fysom import FysomGlobalMixin, FysomGlobal, Fysom
#from client.API.Register import Register
#from client.GUI.Register import RegisterGui
#from client.GUI.main_page import SeaofBTCapp


fsm = Fysom({ 'initial': 'login','final': 'end',
              'events': [
                  {'name': 'registered', 'src': 'register', 'dst': 'login'},
                    {'name': 'logedin', 'src': 'login', 'dst': 'end'},
                    {'name': 'to_register', 'src': 'login', 'dst': 'register'},
              ] })





