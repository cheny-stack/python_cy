# -*- coding: utf-8 -*
from keyboard import add_hotkey, wait
import time

import pyautogui
import time


def gng(file_name):
    my_screenshot = pyautogui.screenshot(region=(252, 214, 1741, 977))

    my_screenshot.save(file_name)


# 快捷截图
def test_a():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file_name = 'C:/Users/47895/iCloudDrive/截图/' + timestr + '.png'
    print("截图:" + file_name)
    gng(file_name)


add_hotkey('f2', test_a)
wait()
