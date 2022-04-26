#!/usr/bin/python
# encoding:utf-8

import pyperclip as pyperclip
import redis
import sys

data = pyperclip.paste()

print("复制数据：" + data)
datas = data.split("@@")

if(len(datas) != 2):
    print("复制格式错误，请按\"key@@value\" 格式复制，示例:  13110051005_123qwe@@5346FD8D0EE4C4CAEC5B4F1E9EC91B6A4B8777D16400DEFEAE2A3CE0D9ED722AEDA0E0CA751FAF9A")
    sys.exit(0)

key = datas[0]
value = datas[1]

r = redis.Redis(host='192.169.7.52',port=6379,password='')

print("设置redis值key:{0}  value{1}".format(key, value))
r.setex(name=key, value = str(value) , time = 3600)

print("获取设置后的值:{0}".format(r.get(key).decode('utf8')))