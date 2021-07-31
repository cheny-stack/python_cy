# -*- coding: utf-8 -*
from keyboard import add_hotkey
import time


# 快捷截图
def test_a():
    print("截图")
    time.sleep(0.1)
    keyboard.press_and_release("F1")
    time.sleep(0.5)
    keyboard.press_and_release("R")


keyboard.add_hotkey('f2', test_a)
keyboard.wait()