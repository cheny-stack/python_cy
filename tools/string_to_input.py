from pynput.keyboard import Key, Controller
import time
from PyQt5.QtWidgets import *

app = QApplication([])
clipboard = app.clipboard()

data = clipboard.mimeData()

if('text/plain' in data.formats()):
    data = data.text()
    print(data)
    print("睡眠3秒")
    time.sleep(3)
    keyboard = Controller()
    keyboard.type(data)
    # for c in data:
    #     #do something with c
    #     time.sleep(0.1)
    #     keyboard.press_and_release(c)