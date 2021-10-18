# -*- coding: utf-8 -*
import requests
import json
import pyperclip as pyperclip
import re


data = pyperclip.paste()
# 获取剪切板内容格式
print(data)
p1 = re.compile(r'\{(.*?)\}', re.S)  #最小匹配
all = re.findall(p1, data);
print(re.findall(p1, data))

if(len(all) >0):
    data = all[0]
    print(data)
    data = "@NacosValue(value = \"${{{}}}\", autoRefreshed = true)".format(data)
    print(data)
    pyperclip.copy(data)