# -*- coding: utf-8 -*-
import getpass
import os
import json
import re
import pysrt
from bs4 import BeautifulSoup
import time
import datetime
srt_file = "temp.srt"
from subprocess import run



 
def get_time(time_int):
    # 使用正则表达式处理时间格式化问题
    if time_int == 0:
        return '00:00:00,000'
    p = re.compile(r'(\d*)(\d{3})\d{3}')
    pl = p.findall(str(time_int))[0]
    if pl[0] == '':
        hms = '00:00:00'
    else:
        h = 0
        m = 0
        s = int(pl[0])
        while s >= 60:
            m += 1
            s -= 60
        while m >= 60:
            h += 1
            m -= 60
        while h >= 24:
            exit('暂不支持超过24小时的字幕文件转换')
        hms = ':'.join((str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)))
    return ','.join((hms, pl[1]))
 
 
def format_time(start, end):
    # 拼接时间格式化后的字符串
    return ' --> '.join((get_time(start), get_time(end)))
 
 
def main():
    # 取得电脑的用户名
    username = getpass.getuser()
    # 拼接取得json文件夹所在地址
    json_root_path = 'C:/Users/' + username + '/AppData/Local/JianyingPro/User Data/Projects/com.lveditor.draft/'
    # 拿到最后一次打开的json文件（内含字幕信息）
    if os.path.exists(json_root_path):
        with open(os.path.join(json_root_path, 'root_meta_info.json'), 'r', encoding='utf-8') as f:
            json_path = (json.load(f)['all_draft_store'][0]['draft_fold_path'])
    # 打开json文件并将其转换为srt文件
    if os.path.exists(json_path):
        with open(os.path.join(json_path, 'draft_content.json'), 'r', encoding='utf-8') as f:
            j = json.load(f)
            l1 = []
            l2 = []
            for i in j['tracks'][1]['segments']:
                start_time = int(i['target_timerange']['start'])
                end_time = int(i['target_timerange']['start'] + i['target_timerange']['duration'])
                l1.append(format_time(start_time, end_time))
            for i in j['materials']['texts']:
                l2.append(i['content'])
            idx = 0
            # 可以在此处自定义新建的srt字幕路径及文件名
            with open(srt_file, 'w', encoding='utf-8') as srt:
                while idx < len(l1):
                    srt.write(str(idx + 1) + '\n')
                    srt.write(l1[idx] + '\n')
                    srt.write(l2[idx] + '\n')
                    srt.write('\n')
                    idx += 1
            subs = pysrt.open(srt_file)
            res = ''
            for sub in subs:
                soup = BeautifulSoup(sub.text,'html.parser')
                print(soup.text)
                res +=  soup.text  + '\n'
            dt    = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            res_file = "/temp/"+ dt + 'temp.txt'
            with open(res_file, 'w', encoding='utf-8') as the_file:
                the_file.write(res)
            run(["notepad",res_file])
            
 
if __name__ == '__main__':
    main()
