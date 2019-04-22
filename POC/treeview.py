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
            raise ValueError  # FIXME:
        else:
            self.show_records(data['records'])

    def show_records(self, username):
        """
        show all user usrnames and program id allow to delete, change and see all records details.

        :param data: the records list of dictionaries
        :return: None
        """

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 12))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 14))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.table = ttk.Treeview(self.parent, columns=('A', ), style="mystyle.Treeview")
        self.table.place(relx=0, rely=0, relheight=0.9, relwidth=1)

        self.table.heading("#0", text="test")
        self.table.column("#0", width=100)

        self.table.insert('', 'end', text='text', values=(username, ))


if __name__ == '__main__':
    root = tk.Tk()
    v = SeeAllGui(root)
    v.show_records("bleyer23@gmail.com")
    root.mainloop()
