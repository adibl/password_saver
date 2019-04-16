"""
name:
date:
description
"""
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from client.API.AddRecord import Passwords
import base64
import re
import numpy
from .Gui import Gui

class SeeAllGui(Gui):
    URL_RE = re.compile('^https?://(?:\w+\.)?(\w+)\.(\w+).*')
    _RELX_ENTITY = 0.25
    _WITH_BUTTON = 0.2
    _HIGH_ALL = 0.07
    _WITH_LABLE_SITE = 0.2
    _RELX_LABLE_SITE = 0.05
    _RELX_LABLE_USERNAME = _RELX_LABLE_SITE + _WITH_LABLE_SITE
    _WITH_LABLE_USERNAME = 0.3
    _REL_X_BUTTON_1 = _RELX_LABLE_USERNAME + _WITH_LABLE_USERNAME
    _REL_X_BUTTON_2 = _REL_X_BUTTON_1 + _WITH_BUTTON


    def __init__(self, parent):
        super(SeeAllGui, self).__init__(parent)
        self.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.configure(width=455)
        self.lables = []

        button = tk.Button(self)
        button.place(relx=0.4, rely=0.9, relheight=0.1, relwidth=0.2)
        button.configure(command=self.run_before)
        button.configure(text='''reset''')



    def run_before(self):
        data = Passwords.GET()
        if any(x in data for x in ['general', 'error']):
            raise ValueError #FIXME:
        else:
            self.show_records(data['records'])

    def show_records(self, data):
        """
        show all user usrnames and program id allow to delete, change and see all records details.

        :param data: the records list of dictionaries
        :return: None
        """
        if len(data) == 0:
            return
        print data

        lable = tk.Label(self)
        lable.place(relx=self._RELX_LABLE_SITE, rely=0, relheight=self._HIGH_ALL, relwidth=self._WITH_LABLE_SITE)
        lable.configure(anchor='w')
        lable.configure(font="-family {Segoe UI} -size 12")
        lable.configure(text='program name')

        lable = tk.Label(self)
        lable.place(relx=self._RELX_LABLE_USERNAME, rely=0, relheight=self._HIGH_ALL, relwidth=self._WITH_LABLE_SITE)
        lable.configure(anchor='w')
        lable.configure(font="-family {Segoe UI} -size 12")
        lable.configure(text='username')

        button_high = 0.8 / len(data)
        for record, rely in zip(data, numpy.arange(0.1, 0.9, button_high)):
            username = record['username']
            program_name = self.url_to_name(record['program_id'])
            lable = tk.Label(self)
            lable.place(relx=self._RELX_LABLE_SITE, rely=rely, relheight=self._HIGH_ALL, relwidth=self._WITH_LABLE_SITE)
            lable.configure(anchor='w')
            lable.configure(font="-family {Segoe UI} -size 12")
            lable.configure(text=str(program_name))

            lable = tk.Label(self)
            lable.place(relx=self._RELX_LABLE_USERNAME, rely=rely, relheight=self._HIGH_ALL, relwidth=self._WITH_LABLE_USERNAME)
            lable.configure(anchor='w')
            lable.configure(font="-family {Segoe UI} -size 12")
            lable.configure(text=str(username))

            button = tk.Button(self)
            button.place(relx=self._REL_X_BUTTON_1, rely=rely, relheight=self._HIGH_ALL, relwidth=self._WITH_BUTTON)
            #button.configure(command=lambda : self.delete(program_name)) TODO: add delete user interface
            button.configure(text='''Edit''')
            button = tk.Button(self)
            button.place(relx=self._REL_X_BUTTON_2, rely=rely, relheight=self._HIGH_ALL, relwidth=self._WITH_BUTTON)
            # button.configure(command=lambda : self.delete(program_name)) TODO: add delete user interface
            button.configure(text='''Delete''')

    @classmethod
    def url_to_name(cls, url):
        url = base64.urlsafe_b64decode(str(url))
        if re.search(cls.URL_RE, url):
            grops = re.search(cls.URL_RE, url).groups()
            return grops[0]


if __name__ == '__main__':
    v = SeeAllGui(None)
    v.run_before()
    v.mainloop()

