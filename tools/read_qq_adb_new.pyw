# -*- coding: utf-8 -*
#!/usr/bin/python
import time
import win32gui,win32com.client
import re
import keyboard
import argparse
import pythoncom
import subprocess

# adb shell
# getevent
# 其中以003 0035和003 0036 开头的两条数据就是我们要的了
# 把170和38e由16进制转换成10进制就是我们要的x，y轴坐标了

# 点击网址
# /dev/input/event1: 0003 0035 000001c4  452
# /dev/input/event1: 0003 0036 000000ae  174
# 粘贴网址
# adb shell input text 'http://192.169.5.16:5500/temp.html'
# 点击进入
# /dev/input/event1: 0003 0035 000003b8  952
# /dev/input/event1: 0003 0036 000000bf  191
# 工具箱
# /dev/input/event1: 0003 0035 000003ee  1006
# /dev/input/event1: 0003 0036 00000095  149
# 朗读
# /dev/input/event1: 0003 0035 000003ae  942
# /dev/input/event1: 0003 0036 0000015c  348

old_file = "old.txt"
file_name = "temp.html"
bad_words = ['作者：', '链接：', '来源：', '著作权归']
file_size = 0

def clear():
    with open(old_file,  encoding='utf-8') as oldfile, open(file_name, 'w',  encoding='utf-8') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                # line = re.sub(r"[\r\n\s]", "", str(line))
                newfile.write(line)


def save_paste(data):
    # if not any(x in data for x in bad_words):
    #     data = re.sub(r"[\r\n\s]", "", str(data))
    data = re.sub(r"\\textit", "", str(data))
    data = re.sub(r"{.*?\}", "", str(data))
    filename = old_file
    with open(filename, 'a', encoding='utf-8') as out:
        out.truncate(0)
        out.write(data + '\n')
    clear()
    
def run_qq_adb():
    print('手机qq朗读')
    current_milli_time = lambda: int(round(time.time() * 1000))
    print(subprocess.call("adb shell input tap 452 174", shell=True))
    text_url= "adb shell input text 'http://192.169.5.16:5500/temp.html?" + str(current_milli_time()) +"'"
    print(subprocess.call(text_url, shell=True))
    print(subprocess.call("adb shell input tap 952 191", shell=True))
    print(subprocess.call("adb shell input tap 864 179", shell=True))
    print(subprocess.call("adb shell input tap 1006 149", shell=True))
    print(subprocess.call("adb shell input tap 942 348", shell=True))
    

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
        run_qq_adb()


# 监听剪切板变动 alt_click
# clipboard.dataChanged.connect(CHANGE_DEAL)
keyboard.add_hotkey('0', change_deal, args=None)
app.exec_()