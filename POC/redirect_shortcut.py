import glob
import win32com.client
import os

program = 'C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\Uplay.exe'

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
paths = glob.glob(desktop + "\\*.lnk")
print paths
shell = win32com.client.Dispatch("WScript.Shell")
for path in paths:
    if shell.CreateShortCut(path).Targetpath == program:
        shortcut = shell.CreateShortCut(paths[0])
        shortcut.targetpath = "D:\\adi\\Documents\\password_saver\\POC\\activate_uplay.bat"
        shortcut.save()