import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import sys
import keyboard

bad_words = ['作者：', '链接：', '来源：', '著作权归']
file_size = 0

# 命令行运行 /Applications/Microsoft\ Edge.app/Contents/MacOS/Microsoft\ Edge  --remote-debugging-port=9222

# 使用网页驱动来运行chrome浏览器
chrome_options = webdriver.EdgeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
 
driver = webdriver.Edge("/Users/cheny/tools/edgedriver_mac64/msedgedriver",options=chrome_options)
all_windows = driver.window_handles
print("所有窗口:")
print(all_windows)
read_window = None
for handle in all_windows:
    driver.switch_to.window(handle)
    try:
        textarea = driver.find_element_by_xpath('//*[@id="input-5"]')
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
        bad_words = ['作者：', '链接：', '来源：', '著作权归','版权归作者所有']
        res = ""
        lines = old_str.splitlines()
        for line in lines:
            if not any(bad_word in line for bad_word in bad_words):
    #            line = re.sub(r"千", "于", str(line))
    #            line = re.sub(r"([\u4e00-\u9fa5]+)\s+", "", str(line))
    #            line = re.sub(r"\s+([\u4e00-\u9fa5]+)", "", str(line))
                line = re.sub(r"[\r\n\s\(\)“”\"]", "", str(line))
                # res += (line)
                res += (line + "\n")
        return res

def reading(data):
    textarea = driver.find_element_by_xpath('//*[@id="input-5"]')
    textarea.send_keys(Keys.COMMAND + "a")
    textarea.send_keys(Keys.DELETE)
    textarea.send_keys(data)
    btn = driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div[1]/div[2]/div/div[2]/button[1]')
    print(btn)
    btn.click()

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
    if('text/plain' in data.formats()):
        file_size = len(data.text())
        # 保存剪切板内容到文件
        data = data.text()
        data = clear(data)
        reading(data)

keyboard.add_hotkey('0', change_deal, args=None)
app.exec_()