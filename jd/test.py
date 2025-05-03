from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
url='https://www.ptpress.com.cn/shopping/search?tag=search&orderStr=hot&level1=75424c57-6dd7-4d1f-b6b9-8e95773c0593'
browser=webdriver.Chrome()
browser.maximize_window()
browser.get(url=url)
time.sleep(3)
# def data_is_not_none(driver):
#     while True:
#         jsonData = browser.execute_script("return window.data;")
#         if jsonData is not None and jsonData != 'undefined':
#             break
#     return True

    # return driver.execute_script("return window.data !== undefined && window.data !== null;")
with open('spider.js', 'r', encoding='utf-8') as file:
    js_code = file.read()
    browser.execute_script(js_code)
    #这地方是无法获取到数据的，也就是python和JavaScript无法交互

    jsonData = browser.execute_script("return window.data")
    print(jsonData)
while True:
    time.sleep(10)