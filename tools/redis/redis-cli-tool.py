#!/usr/bin/python
# encoding:utf-8

import pyperclip as pyperclip
import redis
import sys

data = pyperclip.paste()

print("复制数据：" + data)
datas = data.split("@@")

if(len(datas) != 2):
    print("复制格式错误，请按\"key@@value\" 格式复制，其中key为:\"登录账号_登录密码\"，示例:  13110051005_admin123@@7AB1E17598EF8A8141943DF6EA3AEE4B5F556156C0D1DD3D655DBDFB67F40840BCDF0E9768694BB9 ")
    sys.exit(0)

key = datas[0]
value = "\""+ datas[1] + "\""


r = redis.Redis(host='192.169.7.52',port=6379,password='')
print("设置redis值key:{0}  value{1}".format(key, value))
r.setex(name=key, value = value , time = 3600)

print("获取设置后的值:{0}".format(r.get(key).decode('utf8')))

