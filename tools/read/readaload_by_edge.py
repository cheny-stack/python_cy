# -*- coding: utf-8 -*
#!/usr/bin/python
import time
import win32gui,win32com.client
import re
import keyboard
import argparse
import pythoncom


old_file = "old.txt"
file_name = "temp.html"
bad_words = ['作者：', '链接：', '来源：', '0']
file_size = 0

# def clear():
#     with open(old_file,  encoding='utf-8') as oldfile, open(file_name, 'w',  encoding='utf-8') as newfile:
#         for line in oldfile:
#             if not any(bad_word in line for bad_word in bad_words):
#                 # line = re.sub(r"[\r\n\s]", "", str(line))
#                 newfile.write(line)


def save_paste(data):
    # if not any(x in data for x in bad_words):
    #     data = re.sub(r"[\r\n\s]", "", str(data))
    data = re.sub(r"\\textit", "", str(data))
    data = re.sub(r"{.*?\}", "", str(data))
    filename = file_name
    with open(filename, 'a', encoding='utf-8') as out:
        out.truncate(0)
        out.write(data + '\n')
    
def run_edge():
    # 将edge浏览器置顶，执行自动化操作
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--window-title', type=str,
                        default="temp.html - 个人 - Microsoft​ Edge")
    args = parser.parse_args()

    print("窗口名：" + args.window_title)

    para_hld = win32gui.FindWindow(None, args.window_title)
    print("窗口句柄：" + str(para_hld))
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(para_hld)

    # 执行浏览器刷新快捷键
    keyboard.press_and_release("ctrl+R")
    time.sleep(0.5)
    keyboard.press_and_release("ctrl+R")
    time.sleep(0.5)
    # 执行浏览器朗读快捷键
    # keyboard.press_and_release("alt+R")
    keyboard.press_and_release("ctrl+shift+u")
    

from PyQt5.QtWidgets import *

app = QApplication([])
clipboard = app.clipboard()

# 当剪切板变动会执行该方法
def change_deal():
    pythoncom.CoInitialize()
    global file_size
    data = clipboard.mimeData()
	
	# 获取剪切板内容格式
    print(data.formats())
    # 如果是文本格式，把内容打印出来
    if('text/plain' in data.formats()):
        file_size = len(data.text())
        # 保存剪切板内容到文件
        data = data.text()
        save_paste(data)
        run_edge()


# 监听剪切板变动 alt_click
keyboard.add_hotkey('0', change_deal, args=None)
app.exec_()