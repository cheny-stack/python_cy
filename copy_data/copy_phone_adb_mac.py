# -*- coding: utf-8 -*
import sys

import pyperclip as pyperclip
import re
import subprocess

# 获取电脑剪切板内容
data = pyperclip.paste()
# 过滤一些特殊字符和文章声明
data = re.sub(r"\n作者.*\n", "\n", str(data))
data = re.sub(r"\n版权声明.*\n", "\n", str(data))
data = re.sub(r"\n链接.*\n", "\n", str(data))
data = re.sub(r"\n来源.*\n", "\n", str(data))
data = re.sub(r"\n著作权归.*\n", "\n", str(data))

data = re.sub(r"[-_\r\n\"*]", "", str(data))

print(data)
sys. exit(0)
data = re.sub(r"千", "于", str(data))
data = re.sub(r"([\u4e00-\u9fa5]+)\s+", lambda x: x.group(1), str(data))
data = re.sub(r"\s+([\u4e00-\u9fa5]+)", lambda x: x.group(1), str(data))
# 通过adb发送到android模拟器的剪切板
if len(data) > 0:
    # cmd = ['adb', '-s', '127.0.0.1:62001', 'shell']
    cmd = ['adb', 'shell']
    procId = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    cmd = 'am broadcast -a clipper.set -e text "' + data + '"\n' \
          + 'input tap 311 132 \n' \
          + 'sleep 0.2 \n' \
          + 'input tap 465 687 \n' \
          + 'input tap 729 1672 \n' \
          + 'input tap 72 143 \n' \
          + 'input tap 50 137 \n' \
          + 'input tap 914 1077 \n' \
          +'exit\n'
    procId.communicate(cmd.encode('utf-8'))
    procId.poll()
    # 点击确定按钮
    # time.sleep(1)
    # cmd = ['adb', 'shell']
    # procId = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    # cmd = '
    # input tap 396 538' + '\nexit\n'
    # procId.communicate(cmd.encode('utf-8'))
    # procId.poll()
