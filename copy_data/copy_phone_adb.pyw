import time

import pyperclip as pyperclip
import re
import subprocess

# https://github.com/majido/clipper/releases/download/v1.2.1/clipper.apk

data = pyperclip.paste()
data = re.sub(r"[-_\r\n\"*]", "", str(data)).split("作者：", 1)[0].split("版权声明：", 1)[0]
data = re.sub(r"[丨 ]", "", str(data))
if len(data) > 0:
    cmd = ['adb', 'shell']
    procId = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    cmd = 'am broadcast -a clipper.set -e text "' + data + '"\n sleep 0.2\ninput tap 396 538 \nexit\n'
    procId.communicate(cmd.encode('utf-8'))
    procId.poll()
    # 点击确定按钮
    # time.sleep(1)
    # cmd = ['adb', 'shell']
    # procId = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    # cmd = 'input tap 396 538' + '\nexit\n'
    # procId.communicate(cmd.encode('utf-8'))
    # procId.poll()
