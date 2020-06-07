# -*- coding: utf-8 -*
import hashlib
import mimetypes
import os
import time
from PIL import Image, ImageGrab

import pyperclip as pyperclip
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore
import evernote.edam.type.ttypes as Types

dateTime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
image_name = "screenshot_" + dateTime + ".png"
# 获取电脑剪切板图片
image_path = "C:/Users/montnets/iCloudDrive/图片库/" + image_name
image = ImageGrab.grabclipboard()
if isinstance(image, Image.Image):
    print("Image: size : %s, mode: %s" % (image.size, image.mode))
    image.save(image_path)
else:
    print("没有截图")
    exit()

dateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
