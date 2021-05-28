# -*- coding: utf-8 -*
import time
import win32gui
import pyperclip as pyperclip
import re
import keyboard
import argparse


old_file = "old.txt"
file_name = "temp.txt"


def clear():
    bad_words = ['作者：', '链接：', '来源：', '著作权归']
    with open(old_file,  encoding='utf-8') as oldfile, open(file_name, 'w',  encoding='utf-8') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)


def save_paste():
    data = pyperclip.paste()
    data = re.sub(r"[\r\n\s]", "", str(data))
    filename = old_file
    with open(filename, 'a', encoding='utf-8') as out:
        out.truncate(0)
        out.write(data + '\n')
    clear()



# 保存剪切板内容到文件
save_paste()

# 将edge浏览器置顶，执行自动化操作
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--window-title', type=str, default= "temp.txt - 个人 - Microsoft​ Edge")
args = parser.parse_args()

print("窗口名：" + args.window_title)

para_hld = win32gui.FindWindow(None, args.window_title)
print("窗口句柄：" + str(para_hld))
title = win32gui.GetWindowText(para_hld)
classname = win32gui.GetClassName(para_hld)
win32gui.SetForegroundWindow(para_hld)

# 执行浏览器刷新快捷键
keyboard.press_and_release("ctrl+R")
time.sleep(1)
# 执行浏览器朗读快捷键
keyboard.press_and_release("ctrl+shift+u")
