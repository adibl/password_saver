from client.API.Register import Register
import Tkinter as tk
from client.PAGE_GUI import register_support
from client.PAGE_GUI.register import Toplevel1

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    register_support.set_Tk_var()
    top = RegisterGui(root)
    register_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    register_support.set_Tk_var()
    top = RegisterGui(w)
    register_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class RegisterGui(Toplevel1):
    def run(self, *args):
        self.clean_errors()
        print 'runnn'
        ret = Register.handle(self.entry_username.get(), self.entry_password.get(), self.Spinbox_question.get(), self.entry_aswer.get())
        print ret
        if ret is True:
            return
        elif type(ret) is dict:
            for error in ret.keys():
                if error == 'username':
                    self.username_error(ret[error])
                elif error == 'password':
                    self.password_error(ret[error])
                elif error == 'question':
                    print ret[error]
                    self.question_error(ret[error])

    def username_error(self, error):
        self.lable_username_error.config(text=error)

    def password_error(self, error):
        self.lable_password_error.config(text=error)

    def question_error(self, error):
        self.lable_question_error.config(text=error)

    def clean_errors(self):
        self.lable_username_error.config(text=' ')
        self.lable_password_error.config(text=' ')
        self.lable_answer_error.config(text=' ')
        self.lable_question_error.config(text=' ')


if __name__ == '__main__':
    vp_start_gui()