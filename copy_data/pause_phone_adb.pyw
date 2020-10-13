import pyperclip as pyperclip
import re
import subprocess

# cmd = ['adb', '-s', '127.0.0.1:62001', 'shell']
# procId = subprocess.Popen(cmd, stdin=subprocess.PIPE)
# cmd = 'input keyevent 85 \nexit\n'
# procId.communicate(cmd.encode('utf-8'))
# procId.poll()
subprocess.call("adb -s 127.0.0.1:62001 shell input keyevent 85", shell=True)