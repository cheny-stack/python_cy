# -*- coding: utf-8 -*
import time
import pyperclip as pyperclip

note_path = "C:/Users/montnets/iCloudDrive/Documents/myNote.txt"

# 获取电脑剪切板内容
data = pyperclip.paste()
dateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
data = dateTime + "\n" + data + "\n\n"
print(data)

# Open the file in append & read mode ('a+')
with open(note_path, "a+") as file_object:
    # Move read cursor to the start of file.
    file_object.seek(0)
    # If file is not empty then append '\n'
    data_read = file_object.read(100)
    if len(data_read) > 0:
        file_object.write("\n")
    # Append text at the end of file
    file_object.write(data)
