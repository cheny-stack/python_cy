import pyperclip as pyperclip
import re
import subprocess

# https://github.com/majido/clipper/releases/download/v1.2.1/clipper.apk

data = pyperclip.paste()
data = re.sub(r"[\r\n*]", "", str(data)).split("作者：", 1)[0].split("版权声明：", 1)[0]

if len(data) > 0:
    cmd = ['adb', 'shell']
    procId = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    cmd = 'am broadcast -a clipper.set -e text "' + data + '"\nexit\n'
    procId.communicate(cmd.encode('utf-8'))
    procId.poll()
