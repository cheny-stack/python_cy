# -*- coding: utf-8 -*
import sys

import win32api
import win32gui, win32com.client
import win32con
import pyperclip as pyperclip


def zhanTie():
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(86, 0, 0, 0)  # v键位码是86
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


def clear():
    # 获取电脑剪切板内容
    data = pyperclip.paste()
    pyperclip.copy(' ')
    print(data)
    # data = re.sub(r"[\r\n\s]", "", str(data))
    # print(data)
    pyperclip.copy(data + " ")


# para_hld = win32gui.FindWindow(None, "GDI+ Window (TencentDocs.exe)")# 1836416
para_hld = win32gui.FindWindow(None, "同步窗口")
print("窗口句柄：" + str(para_hld))

title = win32gui.GetWindowText(para_hld)

classname = win32gui.GetClassName(para_hld)

print("标题：" + title)
print("classname：" + classname)

win32gui.SetForegroundWindow(para_hld)
shell = win32com.client.Dispatch("WScript.Shell")

shell.SendKeys('^a')
clear()
zhanTie()
