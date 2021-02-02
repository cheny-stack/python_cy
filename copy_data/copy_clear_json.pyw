# -*- coding: utf-8 -*
import sys

import pyperclip as pyperclip

import re
import subprocess

# 获取电脑剪切板内容
data = pyperclip.paste()
pyperclip.copy(' ')
print(data)
data = re.sub(r"[\r\n\s]", "", str(data))
print(data)
pyperclip.copy(data+" ")
