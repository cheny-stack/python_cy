# -*- coding: utf-8 -*
import time
import requests
import json
import pyperclip as pyperclip
import re
import keyboard
import subprocess


def clear(old_str):
    bad_words = ['作者：', '链接：', '来源：', '著作权归']
    res = ""
    lines = old_str.splitlines()
    for line in lines:
        if not any(bad_word in line for bad_word in bad_words):
            #            line = re.sub(r"千", "于", str(line))
            #            line = re.sub(r"([\u4e00-\u9fa5]+)\s+", "", str(line))
            #            line = re.sub(r"\s+([\u4e00-\u9fa5]+)", "", str(line))
            line = re.sub(r"[\r\n\s\(\)“”\"]", "", str(line))
            res += (line + ",")
    res = res + 'ok ok ok ok********'
    return res

def sendData(data):
    # print(data)
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    url = "http://81.71.26.244:8086/changeContent"
    pyload = {"content": data}
    response = requests.post(url, data=json.dumps(pyload), headers=headers).text
    print(response)

def run_shortcut():
    proxies = {'http': 'http://localhost:10809', 'https': 'http://localhost:10809'}
    url = "https://api.pushcut.io/8s_ozO4VmXmJklpB3P51S/execute?shortcut=Audio%20texte"
    response = requests.post(url, proxies=proxies, verify=False).text
    print(response)

def run_qq_adb():
    change_deal()
    time.sleep(1)
    print('手机qq朗读')
    # current_milli_time = lambda: int(round(time.time() * 1000))
    # print(subprocess.call("adb shell input tap 452 174", shell=True))
    # text_url= "adb shell input text 'http://192.169.5.16:5500/temp.html?" + str(current_milli_time()) +"'"
    # print(subprocess.call(text_url, shell=True))
    # print(subprocess.call("adb shell input tap 952 191", shell=True))
    # print(subprocess.call("adb shell input tap 864 179", shell=True))
    print(subprocess.call("adb shell input tap 1006 149", shell=True))
    print(subprocess.call("adb shell input tap 533 1887", shell=True))
    
from PyQt5.QtWidgets import *

app = QApplication([])
clipboard = app.clipboard()

# 当剪切板变动会执行该方法
def change_deal():
    data = clipboard.mimeData()
	
	# 获取剪切板内容格式
    print(data.formats())
    # 如果是文本格式，把内容打印出来
    if('text/plain' in data.formats()):
        print(data.text())
        data = clear(data.text())
        sendData(data)
        # run_shortcut()

# 监听剪切板变动
# clipboard.dataChanged.connect(change_deal)
keyboard.add_hotkey('0', run_qq_adb, args=None)
app.exec_()
