# -*- coding: utf-8 -*
import requests
import json
import pyperclip as pyperclip
import re


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
            res += line
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

# 监听剪切板变动
clipboard.dataChanged.connect(change_deal)
app.exec_()
