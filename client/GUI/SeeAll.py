"""
name:
date:
description
"""
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import base64
import re
import ttk

from client.API.AddRecord import Passwords
from client.GUI.Gui import Gui
import tkMessageBox


class SeeAllGui(Gui):
    URL_RE = re.compile('^(?:\w+\.)?(\w+)\.(\w+).*')
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
        button.configure(text='''reload''')

        button = tk.Button(self)
        button.place(relx=0.7, rely=0.9, relheight=0.1, relwidth=0.2)
        button.configure(command=self.delete_user)
        button.configure(text='''delete user''')

    def run_before(self):
        data = Passwords.GET()
        if any(x in data for x in ['general', 'error']):
            raise ValueError  # FIXME:
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

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 12))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 14))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.table = ttk.Treeview(self.parent, columns=('A', ), style="mystyle.Treeview")
        self.table.place(relx=0, rely=0, relheight=0.9, relwidth=1)

        self.table.heading("#0", text="program name")
        self.table.column("#0", width=100)

        self.table.heading("A", text="username")
        self.table.column("A", width=100)

        self.records = {}

        for record in data:
            username = record['username']
            program_name = self.url_to_name(record['program_id'])
            program_id = base64.urlsafe_b64decode(str(record['program_id']))
            print program_name
            print program_id
            print username
            id = self.table.insert('', 'end', text=program_name, values=(username, ))
            self.records[id] = program_id
            self.table.bind(sequence="<Double-1>", func=self.edit_record)
        print self.records

    @classmethod
    def url_to_name(cls, url):
        url = base64.urlsafe_b64decode(str(url))
        if re.search(cls.URL_RE, url):
            grops = re.search(cls.URL_RE, url).groups()
            return grops[0]


if __name__ == '__main__':
    root = tk.Tk()
    v = SeeAllGui(root)
    v.show_records([{"username": "bleyer23", "sec_level": 0,
                     "program_id": "aHR0cHM6Ly93ZWIubWFzaG92LmluZm8vc3R1ZGVudHMvIyEvbG9naW4v"},
                    {"username": "sgfdfdsg", "sec_level": 0,
                     "program_id": "aHR0cHM6Ly9zdGFja292ZXJmbG93LmNvbS9xdWVzdGlvbnMvMTYzNzM4ODcvaG93LXRvLXNldC10aGUtdGV4dC12YWx1ZS1jb250ZW50LW9mLWFuLWVudHJ5LXdpZGdldC11c2luZy1hLWJ1dHRvbi1pbi10a2ludGVy"},
                    {"username": "qewr", "sec_level": 0,
                     "program_id": "aHR0cHM6Ly9zdGFja292ZXJmbG93LmNvbS9xdWVzdGlvbnMvMjI3NTExMDAvdGtpbnRlci1tYWluLXdpbmRvdy1mb2N1cw=="}])
    root.mainloop()
