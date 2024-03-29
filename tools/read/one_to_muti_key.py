# -*- coding: utf-8 -*
# !/usr/bin/python
from PyQt5.QtWidgets import *
import keyboard


def press_muti():
    # 执行浏览器刷新快捷键
    print("剪切板改动")
    keyboard.press_and_release("alt+w")


app = QApplication([])
clipboard = app.clipboard()


# 监听剪切板变动 alt_click
# keyboard.add_hotkey('+', press_muti, args=None)
clipboard.dataChanged.connect(press_muti)
app.exec_()
