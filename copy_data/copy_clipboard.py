# from tkinter import Tk
# r = Tk()
# r.withdraw()
# data = r.clipboard_get()
# data = str(data).replace("\r\n", "").replace("\n", "")
# r.clipboard_clear()
# r.clipboard_append(data)
# r.update() # now it stays on the clipboard after the window is closed
# r.destroy()


# import win32clipboard
# import re
# win32clipboard.OpenClipboard()
# data = win32clipboard.GetClipboardData()
# # data = str(data).replace("\r\n", "").replace("\n", "")
# data = re.sub(r"[\r\n]", "", str(data))
# win32clipboard.EmptyClipboard()
# win32clipboard.SetClipboardText(data)
# win32clipboard.CloseClipboard()


import pyperclip as pyperclip
import re
import subprocess

data = pyperclip.paste()
data = re.sub(r"[\r\n*]", "", str(data)).split("作者：", 1)[0].split("版权声明：", 1)[0]
pyperclip.copy(data)
