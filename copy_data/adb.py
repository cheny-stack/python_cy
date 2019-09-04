import subprocess


def sh(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p.stdout.read())


cmd = ['adb', 'shell']
procId = subprocess.Popen(cmd, stdin = subprocess.PIPE)
str ='"启动服务后，您可以通过广播意图来调用限幅器服务。意图的动作可以是“获取”或“设置”。设置剪贴板值时，将字符串作为Extra参数传递"'
cmd ='am broadcast -a clipper.set -e text '+str+'\nexit\n'
procId.communicate(cmd.encode('utf-8'))
procId.poll()