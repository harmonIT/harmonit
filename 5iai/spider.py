import requests
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'DEFAULT_ENTERPRISE_IMG=company.jpg; APP_HEADER_NAME=%E6%B3%B0%E8%BF%AA%E5%86%85%E6%8E%A8; APP_TITLE=%E6%B3%B0%E8%BF%AA%E5%86%85%E6%8E%A8; APP_RESOURCE_SCOPE_NAME=%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83; APP_HELP_DOC_URL=http://45.116.35.168:8083/eb; REGISTER_URL=http://www.5iai.com:444/oauth/register; sysTime=2025/6/18%2011:06:33',
    'Host': 'www.5iai.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.5iai.com/',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
lists = [[] for _ in range(13)]
for i in range(1,2):
    url='https://www.5iai.com/api/resume/baseInfo/public/es?pageSize=10&pageNumber={}&function=&skills=&workplace=&keyword='.format(i)
    resp=requests.get(url=url,headers=headers)
    jsData=json.loads(resp.text)
    con=jsData['data']['content']
    for j in con:
        lists[0].append(j['id'])
    for i in con:
        lists[1].append(j['updateTime'])

url='https://www.5iai.com/#/moreResume/detail/1926996185164414976'
browser=webdriver.Chrome()
browser.get(url=url)
name_ = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="el-col el-col-20"]/h1/text()')))
gender_ = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//p[@class="tit"]/span[1]/span/text()')))
status_ = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//p[@class="tit"]/span[4]/text()')))
nianling = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//p[@class="tit"]/span[2]/text()')))
zhuzhi = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//p[@class="tit"]/span[3]/text()')))
qiwangzhineng = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//b[@class="expectPosition"]/text()')))
xinzifanwei= WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="el-col el-col-12"][2]/p[1]/b/text()')))
ziwopingjia = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//p[@class="intro"]/text()')))
qiuzhiyixiang = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="el-col el-col-20"]/h1/text()')))
gongzuojingli = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="el-col el-col-20"]/h1/text()')))
xiangmujingyan = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="el-col el-col-20"]/h1/text()')))
jiaoyujingli= WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="el-col el-col-20"]/h1/text()')))
    

