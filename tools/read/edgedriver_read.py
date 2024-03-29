import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import sys
import keyboard
import pyautogui
bad_words = ['作者：', '链接：', '来源：', '著作权归']
file_size = 0

def drag_select():
    pyautogui.moveTo(10, 112)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(871, 636, 1)
    pyautogui.mouseUp(button='left')
    time.sleep(0.5)
    change_deal()

# 命令行运行 msedge --remote-debugging-port=9222 https://b-ccy.oss-cn-beijing.aliyuncs.com/my/dist/index.html

# 使用网页驱动来运行chrome浏览器
chrome_options = webdriver.EdgeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
 
driver = webdriver.Edge("C:/chenyun/tools/edgedriver/msedgedriver.exe",options=chrome_options)
all_windows = driver.window_handles
print("所有窗口:")
print(all_windows)
read_window = None
for handle in all_windows:
    driver.switch_to.window(handle)
    try:
        textarea = driver.find_elements(By.XPATH, '//*[@id="input-5"]')
        read_window = handle
    except:
        print('窗口错误')
if(handle == None):
    print("没有找到朗读窗口")
    sys.exit(0)

driver.switch_to.window(read_window)
# 设置速度
# 激活下拉框
# driver.find_element_by_xpath('//*[@id="app"]/div[1]/main/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div[1]/div[1]/div[1]').click()
# time.sleep(1)
# # 提取此下拉框中的所有元素
# lis=driver.find_elements_by_xpath('//*[@id="list-8"]/div')
# # 判断需要的元素在哪里，点击
# for li in lis:
#     text = li.find_element_by_tag_name('div').text
#     print("语音：" + text)
#     if "Microsoft Xiaoxiao Online (Natural) - Chinese (Mainland) (zh-CN)" == text:
#         li.click()
#         break

# 获取电脑剪切板内容
def clear(old_str):
        bad_words = ['版权声明：','原文链接：','作者：', '链接：', '来源：', '著作权归','版权归作者所有']
        res = ""
        lines = old_str.splitlines()
        for line in lines:
            if not any(bad_word in line for bad_word in bad_words):
    #            line = re.sub(r"千", "于", str(line))
    #            line = re.sub(r"([\u4e00-\u9fa5]+)\s+", "", str(line))
                line = re.sub(r"\s+([\u4e00-\u9fa5]+)", "", str(line))
                # line = re.sub(r"[\r\n\s\(\)“”\"]", "", str(line))
                line = re.sub(r"[#]", "", str(line))
                # res += (line)
                res += (line + "") # \n
        return res

def reading(data):
    textarea = driver.find_element(By.XPATH, '//*[@id="input-5"]')
    textarea.send_keys(Keys.CONTROL + "a")
    textarea.send_keys(Keys.DELETE)
    textarea.send_keys(data)
    btn = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div/div[1]/div[2]/div/div[2]/button[1]')
    pause = driver.find_elements(By.XPATH,"//*[contains(text(),'停止')]")
    if len(pause) > 0:
        print("暂停")
        btn.click()
    print("朗读")
    btn.click()

#检验是否含有中文字符
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

def buttonClicked():
    print("buttonClicked")


from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5 import QtCore

app = QApplication([])
clipboard = app.clipboard()

# 当剪切板变动会执行该方法
def change_deal():
    global file_size
    data = clipboard.mimeData()
	
	# 获取剪切板内容格式
    print(data.formats())
    # 如果是文本格式，把内容打印出来
    if('text/plain' in data.formats()):
        file_size = len(data.text())
        # 保存剪切板内容到文件
        data = data.text()
        data = clear(data)
        reading(data)

keyboard.add_hotkey('0', change_deal, args=None)
# keyboard.add_hotkey('9', drag_select, args=None)

# window = QMainWindow()
# btn1 = QPushButton("朗读剪切板", window)
# btn1.move(30, 50)
# btn1.clicked.connect(change_deal) 
# window.statusBar()
# window.setGeometry(300, 300, 160, 150)
# window.setWindowTitle('朗读工具')
# window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
# window.show()  
app.exec_()