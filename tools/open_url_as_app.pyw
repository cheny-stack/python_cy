import sys
import time
from PyQt5.QtWidgets import *
# Python code to find the URL from an input string
# Using the regular expression
import re
import subprocess
import os

def Find(string):
      
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]

app = QApplication([])
clipboard = app.clipboard()

data = clipboard.mimeData()

if('text/plain' in data.formats()):
    data = data.text()
    print(data)
    urls =  Find(data)
    if(len(urls) > 0):
        print("Urls: ", urls)
        url = urls[0]
        print(url)
        cmd = '\"C:\Program Files\Google\Chrome\Application\chrome_proxy.exe\" --profile-directory=Default --app=%s'
        cmd =cmd%(url)
        print("cmd:" + cmd)
        subprocess.call(cmd + ' &', shell=True)
        # print(os.system('cmd /k '+ cmd + ' &'))   
        sys.exit()
    else:
        print("未找到链接")
    

else:
     print("未找到链接")

  
