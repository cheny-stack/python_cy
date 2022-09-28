# -*- coding: utf-8 -*
#!/usr/bin/python
import time
import win32gui,win32com.client
import re
import keyboard
import argparse
import pythoncom

from PyQt5.QtWidgets import *

app = QApplication([])
clipboard = app.clipboard()

# 当剪切板变动会执行该方法
def change_deal():
    pythoncom.CoInitialize()
        # 将edge浏览器置顶，执行自动化操作
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--window-title', type=str,
                        default="云")
    args = parser.parse_args()

    print("窗口名：" + args.window_title)

    para_hld = win32gui.FindWindow(None, args.window_title)
    print("窗口句柄：" + str(para_hld))
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(para_hld)

    # 执行浏览器刷新快捷键
    keyboard.press_and_release("0")
    


# 监听剪切板变动 alt_click
keyboard.add_hotkey('8', change_deal, args=None)
app.exec_()