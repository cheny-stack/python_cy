# -*- coding: utf-8 -*
import sys,time

import win32api
import win32gui
import win32con
import pyperclip as pyperclip
import re
import keyboard


def save_paste():
    data = pyperclip.paste()

    filename = "temp.txt"
    with open(filename, 'a') as out:
        out.truncate(0)
        out.write(data + '\n')


def clear():
    # 获取电脑剪切板内容
    data = pyperclip.paste()
    pyperclip.copy(' ')
    print(data)
    # data = re.sub(r"\n作者.*\n", "\n", str(data))
    sub_str = "\n作者"
    if sub_str in data:
        data = data[:data.index(sub_str)]
    data = re.sub(r"[\r\n\s]", "", str(data))
    # print(data)
    pyperclip.copy(data + " ")


# para_hld = win32gui.FindWindow(None, "GDI+ Window (TencentDocs.exe)")# 1836416
para_hld = win32gui.FindWindow(None, "temp.txt 和另外 1 个页面 - 个人 - Microsoft​ Edge")
print("窗口句柄：" + str(para_hld))

title = win32gui.GetWindowText(para_hld)

classname = win32gui.GetClassName(para_hld)

print("标题：" + title)
print("classname：" + classname)

save_paste()
win32gui.SetForegroundWindow(para_hld)
keyboard.press_and_release("ctrl+R")
time.sleep(1)
keyboard.press_and_release("ctrl+shift+u")
