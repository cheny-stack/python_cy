import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import sys
import keyboard

bad_words = ['作者：', '链接：', '来源：', '著作权归']
file_size = 0
file_name = "temp.html"

# 命令行运行 msedge --remote-debugging-port=9222 file:///C:/work/Python/PycharmProjects/python_cy/tools/read/temp.html

# 使用网页驱动来运行chrome浏览器
chrome_options = webdriver.EdgeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Edge("C:/chenyun/tools/edgedriver/msedgedriver.exe", options=chrome_options)
all_windows = driver.window_handles
print("所有窗口:")
print(all_windows)


# 获取电脑剪切板内容
def write_file(data):
    bad_words = ['作者：', '链接：', '来源：', '著作权归', '版权归作者所有']
    lines = data.splitlines()
    with open(file_name, 'w', encoding='utf-8') as newfile:
        for line in lines:
            if not any(bad_word in line for bad_word in bad_words):
                line = re.sub(r"[\r\n\s\(\)“”\"]", "", str(line))
                # res += (line)
                # res += (line + "\n")
                newfile.write(line)

import pyautogui

def reading():
    print("开始朗读")
    # 定位到要悬停的元素
    driver.refresh()
    body = driver.find_element(By.XPATH, '/html/body')
    action = ActionChains(driver)
    action.move_to_element(body).key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()

    # 对定位到的元素执行悬停操作
    action.context_click(body).perform()
    time.sleep(2)
    action.send_keys(Keys.ARROW_DOWN).perform()
    # ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    # ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.RETURN).perform()



from PyQt5.QtWidgets import *

app = QApplication([])
clipboard = app.clipboard()


# 当剪切板变动会执行该方法
def change_deal():
    global file_size
    data = clipboard.mimeData()
    # 获取剪切板内容格式
    print(data.formats())
    # 如果是文本格式，把内容打印出来
    if 'text/plain' in data.formats():
        file_size = len(data.text())
        # 保存剪切板内容到文件
        data = data.text()
        write_file(data)
        reading()


keyboard.add_hotkey('0', change_deal, args=None)
app.exec_()
