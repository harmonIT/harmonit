from selenium import webdriver
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url='https://you.ctrip.com/sight/nanjing9/19519.html?renderPlatform=#ctm_ref=www_hp_bs_lst'
browser=webdriver.Chrome()
browser.get(url=url)
browser.maximize_window()
#页面不在可视范围内无法点击元素！！！无论是使用ActionChains还是使用.click()方法都无法点击元素！！！
#浏览器等待并找到时间排序按钮
try:
    sort_time = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="sortTag"]')))
    browser.execute_script("arguments[0].click();", sort_time)
except Exception as e:
    print("错误：",e)
# 等待按钮生效
WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="sortTag current"]'), '时间排序'))

commentDetails=[]
commentTimes=[]
averageScores=[]
toolsItems=[]
def get_ele_list(xpath,ele_list):  
    eles=browser.find_elements(By.XPATH,xpath)
    for ele in eles:
        ele_list.append(ele.get_attribute('textContent'))
for i in range(1,5):
    WebDriverWait(browser,10).until(EC.text_to_be_present_in_element((By.XPATH,'//li[contains(@class, "ant-pagination-item-active")]/a'),str(i)))
    get_ele_list('//div[@class="commentTime"]',commentTimes)
    get_ele_list('//div[@class="commentDetail"]',commentDetails)
    get_ele_list('//span[@class="averageScore"]',averageScores)
    get_ele_list('//span[@class="toolsItem"]',toolsItems)
    #执行点击操作，如何做可以不执行点击操作，直接获取数据？用浏览器执行post请求
    next_page=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//li[@class=" ant-pagination-next"]')))
    browser.execute_script("arguments[0].click();", next_page)
    # next_page=browser.find_element(By.XPATH,'//li[@class=" ant-pagination-next"]')
    # ActionChains(browser).move_to_element(next_page).perform()
    # ActionChains(browser).click(next_page).perform()
#数据清洗
def clean_ip_location(list):
    cleaned_texts = []
    for i in list:
        start_index = i.find("IP")
        if start_index != -1:
            cleaned_texts.append(i[:start_index])
    return cleaned_texts
commentTimes=clean_ip_location(commentTimes)
with open('xiecheng.csv','w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(['评论内容','评论时间','平均评分','点赞数'])
    #按列写入数据
    for commentDetail, commentTime, averageScore, toolsItem in zip(commentDetails, commentTimes, averageScores, toolsItems):
        writer.writerow([commentDetail, commentTime, averageScore, toolsItem])

browser.quit()


