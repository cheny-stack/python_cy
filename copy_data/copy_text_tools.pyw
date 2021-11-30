# -*- coding: utf-8 -*
import sys
print("1")
import pyperclip as pyperclip
import re
import subprocess
print("1")
# 获取电脑剪切板内容
data = pyperclip.paste()

print("1")
def clear(old_str):
    p1 = re.compile(r'[(](.*?)[)]', re.S)  # 最小匹配
    res = ""
    lines = old_str.splitlines()
    for line in lines:
        #

        line += "\n"
        res += line
    return res


data = clear(data)

print(data)

sh_file = open("copy_text_tools.txt", "w", encoding='utf-8')
sh_file.write(data)
sh_file.close()
