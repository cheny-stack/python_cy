from tcloud_tts import task_process


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import sys
import keyboard
bad_words = ['作者：', '链接：', '来源：', '著作权归']
file_size = 0

# 获取电脑剪切板内容
def clear(old_str):
        bad_words = ['版权声明：','原文链接：','作者：', '链接：', '来源：', '著作权归','版权归作者所有']
        res = ""
        lines = old_str.splitlines()
        for line in lines:
            if not any(bad_word in line for bad_word in bad_words):
    #            line = re.sub(r"千", "于", str(line))
    #            line = re.sub(r"([\u4e00-\u9fa5]+)\s+", "", str(line))
                line = re.sub(r"\s+([\u4e00-\u9fa5]+)", "", str(line))
                # line = re.sub(r"[\r\n\s\(\)“”\"]", "", str(line))
                line = re.sub(r"[#]", "", str(line))
                # res += (line)
                res += (line + "") # \n
        return res

def reading(data):
    task_process(data)

#检验是否含有中文字符
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

def buttonClicked():
    print("buttonClicked")


from PyQt5.QtWidgets import  QApplication

app = QApplication([])
clipboard = app.clipboard()

# 当剪切板变动会执行该方法
def change_deal():
    global file_size
    data = clipboard.mimeData()
	
	# 获取剪切板内容格式
    print(data.formats())
    # 如果是文本格式，把内容打印出来
    if('text/plain' in data.formats()):
        file_size = len(data.text())
        # 保存剪切板内容到文件
        data = data.text()
        data = clear(data)
        reading(data)

keyboard.add_hotkey('0', change_deal, args=None)

app.exec_()
