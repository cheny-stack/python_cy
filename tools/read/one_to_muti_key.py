# -*- coding: utf-8 -*
#!/usr/bin/python
from PyQt5.QtWidgets import *
import time
import win32gui
import win32com.client
import re
import keyboard
import argparse
import pythoncom


def press_muti():
    # 执行浏览器刷新快捷键
    keyboard.press_and_release("alt+w")


app = QApplication([])
# clipboard = app.clipboard()

# 当剪切板变动会执行该方法
# def change_deal():
#     press_muti()


# 监听剪切板变动 alt_click
keyboard.add_hotkey('0', press_muti, args=None)
app.exec_()
