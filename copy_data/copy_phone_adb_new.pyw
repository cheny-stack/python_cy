# -*- coding: utf-8 -*
import sys
import re
import subprocess

# 获取电脑剪切板内容
def clear(old_str):
        bad_words = ['作者：', '链接：', '来源：', '著作权归','版权归作者所有']
        res = ""
        lines = old_str.splitlines()
        for line in lines:
            if not any(bad_word in line for bad_word in bad_words):
    #            line = re.sub(r"千", "于", str(line))
    #            line = re.sub(r"([\u4e00-\u9fa5]+)\s+", "", str(line))
    #            line = re.sub(r"\s+([\u4e00-\u9fa5]+)", "", str(line))
    #             line = re.sub(r"[\r\n\s\(\)“”\"]", "", str(line))
                res += (line + '\n')
        return res

def read(data):
    data = clear(data)
    # print(data)

    # 生成脚本文件生成脚本文件 打开开发者，显示指针位置
    cmd_str = 'am broadcast -a clipper.set -e text "' + data + '"\n' \
              + '\nsleep 0.2\ninput tap 396 538\n' \
              + 'exit\n'
    sh_file = open("longcommand.sh", "w", encoding='utf-8')
    sh_file.write(cmd_str)
    sh_file.close()
    # sys.exit(0)
    # 上传文件到模拟器
    print(subprocess.call("adb -s 127.0.0.1:62001 push longcommand.sh /data/local/tmp", shell=True))
    # 通过adb发送到android模拟器的剪切板
    if len(data) > 0:
        # cmd = ['adb', '-s', '127.0.0.1:62001', 'shell']
        print(subprocess.call("adb -s 127.0.0.1:62001 shell sh /data/local/tmp/longcommand.sh", shell=True))


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
        data = data.text()
        if(not data.startswith("__")):
            data = "__" + data
            print(data)
            read(data)

# 监听剪切板变动
clipboard.dataChanged.connect(change_deal)
app.exec_()