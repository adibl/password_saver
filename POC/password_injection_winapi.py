import subprocess
import time
import win32api
import win32com.client
import sys


if __name__ == "__main__":
    program =" ".join(sys.argv[1:])
    sub = subprocess.Popen(program)
    shell = win32com.client.Dispatch("WScript.Shell")
    time.sleep(9)
    shell.SendKeys("bleyer23@gmail.com")
    shell.SendKeys("{TAB}")
    win32api.Sleep(50)
    shell.SendKeys("qazwsx12")
    shell.SendKeys("{ENTER}")
    sub.wait()

