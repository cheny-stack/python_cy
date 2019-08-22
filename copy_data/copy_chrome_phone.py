from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyperclip as pyperclip
import re



data = pyperclip.paste()
data = re.sub(r"[\r\n*]", "", str(data)).split("作者：", 1)[0].split("版权声明：", 1)[0]
# pyperclip.copy(data)
print(len(data))

# 打开chrome
# C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:/work/tools/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
print(driver.title)
driver.find_element_by_xpath("./*//textarea[@class='widget-airTransport-clip-input']").clear()
driver.find_element_by_xpath("./*//textarea[@class='widget-airTransport-clip-input']").send_keys(data)
driver.find_element_by_xpath("./*//button[@class='btn btn-primary widget-airTransport-blueBtn widget-airTransport-clip-push']").click()
