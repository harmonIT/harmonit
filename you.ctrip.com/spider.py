from selenium import webdriver
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
url='https://you.ctrip.com/sight/nanjing9/19519.html?renderPlatform=#ctm_ref=www_hp_bs_lst'
browser=webdriver.Chrome()
browser.get(url=url)
# page_source=browser.page_source
#浏览器等待并找到时间排序按钮
sort_time=WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,'//span[@class="sortTag"]')))
ActionChains(browser).click(sort_time).perform()
#等待按钮生效，否则服务器未返回数据就会执行下面程序
sort_time = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="sortTag current"]'), '时间排序'))
commentDetails=[]
commentTimes=[]
averageScores=[]
toolsItems=[]
for i in range(2):
    commentDetail=WebDriverWait(browser,5).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="commentDetail"]')))#如果xpath‘//div[@class="commentDetail/text()’会选择到文本内容，而until方法需要传入element对象  
    commentDetails.append(commentDetail)
    # print(type(commentDetail.text),commentDetail.text)
    commentTime=WebDriverWait(browser,5).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="commentTime"]')))
    # commentTimes.append(EC.presence_of_element_located((By.XPATH,'//div[@class="commentTime"]/text()')))
    commentTimes.append(commentTime)
    averageScore=WebDriverWait(browser,5).until(EC.presence_of_all_elements_located((By.XPATH,'//span[@class="averageScore"]')))
    averageScores.append(averageScore)
    # print(type(averageScore.text),averageScore.text)
    toolsItem=WebDriverWait(browser,5).until(EC.presence_of_all_elements_located((By.XPATH,'//span[@class="toolsItem"]')))
    toolsItems.append(toolsItem)
    next_page=WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,'//span[@class="ant-pagination-item-comment"]')))
    ActionChains(browser).click(next_page).perform()
print('评论内容',commentDetails)
with open('xiecheng.csv','w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(['contentDetail','commentTime','averageScore','toolsItem'])
    #按列写入数据
    for commentDetail, commentTime, averageScore, toolsItem in zip(commentDetails, commentTimes, averageScores, toolsItems):
        writer.writerow([commentDetail, commentTime, averageScore, toolsItem])

browser.close()

'''postUrl='https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList?_fxpcqlniredt=09031059411794059976&x-traceID=09031059411794059976-1745486764924-63354'
headers = {
    'Content-Type': 'application/json'
}
data={
    "arg": {
        "channelType": 2,
        "collapseType": 0,
        "commentTagId": 0,
        "pageIndex": 1,
        "pageSize": 10,
        "poiId": 80549,
        "sortType": 1,
        "sourceType": 1,
        "starType": 0,
    },
    "head": {
        "cid": "09031059411794059976",
        "ctok": "",
        "cver": "1.0",
        "lang": "01",
        "sid": "8888",
        "syscode": "09",
        "auth": "",
        "xsid":"",
        "extension": []
    }
}
data=json.dumps(data)

html=requests.post(postUrl,data,headers=headers)
print(html.status_code)
html=html.text
print(html)   
html=json.loads(html)
items=html['result']['items']
for item in items:
    print(item['content'])

'''

