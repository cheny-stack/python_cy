# -*- coding: utf-8 -*
import time
import win32gui
import pyperclip as pyperclip
import re
import keyboard


def save_paste():
    data = pyperclip.paste()
    filename = "temp.txt"
    with open(filename, 'a') as out:
        out.truncate(0)
        out.write(data + '\n')


# 保存剪切板内容到文件
save_paste()

# 将edge浏览器置顶，执行自动化操作
para_hld = win32gui.FindWindow(None, "temp.txt 和另外 1 个页面 - 个人 - Microsoft​ Edge")
print("窗口句柄：" + str(para_hld))
title = win32gui.GetWindowText(para_hld)
classname = win32gui.GetClassName(para_hld)
print("标题：" + title)
print("classname：" + classname)
win32gui.SetForegroundWindow(para_hld)

# 执行浏览器刷新快捷键
keyboard.press_and_release("ctrl+R")
time.sleep(1)
# 执行浏览器朗读快捷键
keyboard.press_and_release("ctrl+shift+u")
