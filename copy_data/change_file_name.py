# -*- coding: utf-8 -*
import os



dirName = 'F:/学习/3、Applied AI with DeepLearning'
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(dirName):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]

for elem in listOfFiles:
    if elem.endswith(".srt") and "[baidu-en-zh]" in elem:
        file_dir, file_name = os.path.split(elem)
        print(file_name)
        file_name_new = file_name.replace(".en", "")
        file_name_new = file_name_new.replace("[baidu-en-zh] ", "")
        print(elem)
        print(os.path.join(file_dir, file_name_new))
        if not os.path.exists(os.path.join(file_dir, file_name_new)):
            os.rename(elem, os.path.join(file_dir, file_name_new))