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

#data = re.sub(r"[-_\r\n\"*]", "", str(data))
data = re.sub(r"[-_\"*]", "", str(data))

# print(data)
# sys. exit(0)
data = re.sub(r"千", "于", str(data))
data = re.sub(r"([\u4e00-\u9fa5]+)\s+", lambda x: x.group(1), str(data))
data = re.sub(r"\s+([\u4e00-\u9fa5]+)", lambda x: x.group(1), str(data))
# 生成脚本文件
cmd_str = 'am broadcast -a clipper.set -e text "' + data + '"\n' \
    + '\nsleep 0.2\ninput tap 396 538\n' \
    + 'exit\n'
sh_file = open("longcommand.sh", "w", encoding='utf-8')
sh_file.write(cmd_str)
sh_file.close()
#sys.exit(0)
# 上传文件到模拟器
print(subprocess.call("adb -s 127.0.0.1:62001 push longcommand.sh /data/local/tmp", shell=True))
# 通过adb发送到android模拟器的剪切板
if len(data) > 0:
    # cmd = ['adb', '-s', '127.0.0.1:62001', 'shell']
    print(subprocess.call("adb -s 127.0.0.1:62001 shell sh /data/local/tmp/longcommand.sh", shell=True))