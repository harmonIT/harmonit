from selenium import webdriver
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
url='https://you.ctrip.com/sight/nanjing9/19519.html?renderPlatform=#ctm_ref=www_hp_bs_lst'
browser=webdriver.Chrome()
browser.get(url=url)
browser.maximize_window()#页面不在可视范围内无法点击元素？？？？
#浏览器等待并找到时间排序按钮
try:
    sort_time = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="sortTag"]')))
    sort_time.click()  # 直接使用 .click() 方法
except :
    print("元素未能在指定时间内点击")

# 等待按钮生效
try:
    sort_time = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="sortTag current"]'), '时间排序'))
except :
    print("排序按钮未能在指定时间内生效")
commentDetails=[]
commentTimes=[]
averageScores=[]
toolsItems=[]
def get_ele_list(xpath,ele_list):  
    eles=browser.find_elements(By.XPATH,xpath)
    for ele in eles:
        ele_list.append(ele.text)
#循环到第三页会卡很久，并且会丢失几次循环，似乎内部循环完了？还是调用函数的问题？
for i in range(1,30):
    #等待点击后的页面加载完成??这个等待机制很鸡肋，不如直接sleep(1)
    # WebDriverWait(browser,10).until(EC.text_to_be_present_in_element((By.XPATH,'//li[contains(@class, "ant-pagination-item-active")]/a'),str(i)))
    time.sleep(2)
    get_ele_list('//div[@class="commentTime"]',commentTimes)
    get_ele_list('//div[@class="commentDetail"]',commentDetails)
    get_ele_list('//span[@class="averageScore"]',averageScores)
    get_ele_list('//span[@class="toolsItem"]',toolsItems)

    next_page=browser.find_element(By.XPATH,'//li[@class=" ant-pagination-next"]')
    ActionChains(browser).click(next_page).perform()
# print('评论内容',commentDetails)
# with open('xiecheng.txt','w',encoding='utf-8') as f:
#     f.write(str(commentDetails))
#     f.write(str(commentTimes))
#     f.write(str(averageScores))
#     f.write(str(toolsItems))
with open('xiecheng.csv','w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(['评论内容','评论时间','平均评分','点赞数'])
    #按列写入数据
    for commentDetail, commentTime, averageScore, toolsItem in zip(commentDetails, commentTimes, averageScores, toolsItems):
        writer.writerow([commentDetail, commentTime, averageScore, toolsItem])

browser.quit()


