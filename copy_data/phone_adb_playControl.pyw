# -*- coding: utf-8 -*

import subprocess


print(subprocess.call("adb -s 127.0.0.1:62001 shell sh /data/local/tmp/longcommand.sh", shell=True))