# -*- coding: utf-8 -*
#!/usr/bin/python
import os
import time
from PyQt5.QtWidgets import *
import keyboard
import pyautogui



def press_muti():
    # 执行浏览器刷新快捷键
    # cmd = """
    # osascript -e 'tell application "System Events" to keystroke "1" using {option down}' 
    # """
    # # minimize active window
    # os.system(cmd)
    pyautogui.hotkey('option', 'q')
    # time.sleep(0.1)
    print("option+Q")


app = QApplication([])
# clipboard = app.clipboard()

# 当剪切板变动会执行该方法
# def change_deal():
#     press_muti()


# 监听剪切板变动 alt_click
keyboard.add_hotkey('/', press_muti, args=None)
app.exec_()
