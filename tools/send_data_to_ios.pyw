# -*- coding: utf-8 -*
import requests
import json
import pyperclip as pyperclip
import re

# 获取电脑剪切板内容
data = pyperclip.paste()


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


data = clear(data)

# print(data)
headers = {
    "Content-Type": "application/json; charset=UTF-8"
}
url = "http://81.71.26.244:8086/changeContent"
pyload = {"content": data}
response = requests.post(url, data=json.dumps(pyload), headers=headers).text
print(response)
