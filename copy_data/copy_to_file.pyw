# -*- coding: utf-8 -*
import time

import pyperclip as pyperclip
import re

from msedge.selenium_tools import Edge, EdgeOptions

from selenium.webdriver import ActionChains  # 鼠标右键操作模拟

import pyautogui  # 右键菜单元素选择



# 获取电脑剪切板内容
from selenium.webdriver.common.keys import Keys

data = pyperclip.paste()



data = re.sub(r"[-_\r\n\"*]", "", str(data))

# print(data)
# sys. exit(0)
data = re.sub(r"千", "于", str(data))
data = re.sub(r"([\u4e00-\u9fa5]+)\s+", lambda x: x.group(1), str(data))
data = re.sub(r"\s+([\u4e00-\u9fa5]+)", lambda x: x.group(1), str(data))
filename = "temp.txt"
with open(filename, 'a') as out:
    out.truncate(0)
    out.write(data + '\n')

# Launch Microsoft Edge (EdgeHTML)
options = EdgeOptions()
options.use_chromium = True
options.add_argument("--log-level=3")
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe",options = options)

# driver.get('https://www.trulia.com/')
driver.refresh()
time.sleep(0.5)
actions = ActionChains(driver)  # 实例化ActionChains类
# actions.key_down(Keys.CONTROL)
actions.context_click()
#
# actions.click(element)
# time.sleep(0.5)
# actions.context_click(element)
# time.sleep(0.5)
# time.sleep(0.5)
# actions.send_keys(Keys.ARROW_DOWN)
# time.sleep(0.5)
# actions.send_keys(Keys.ARROW_DOWN)
# time.sleep(0.5)
# actions.send_keys(Keys.ARROW_DOWN)
# time.sleep(0.5)
# actions.send_keys(Keys.RETURN)
# time.sleep(0.5)
actions.perform()