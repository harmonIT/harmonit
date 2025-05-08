
import requests
import pandas
from lxml import etree
import redis
import re
import threading
lock=threading.Lock()
_redis=redis.Redis(host='127.0.0.1',port=6379,db=0)
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "Hm_lvt_50758913e6f0dfc9deacbfebce3637e4=1746335736; Hm_lpvt_50758913e6f0dfc9deacbfebce3637e4=1746676718; JSESSIONID=2AB72C31F42EB2A9696FB619CE0A8319; Hm_lvt_50758913e6f0dfc9deacbfebce3637e4=1746335736,1746500060,1746676459; HMACCOUNT=9982405386288C7A; Hm_lpvt_50758913e6f0dfc9deacbfebce3637e4=1746676462",
    "Host": "openstd.samr.gov.cn",
    "Pragma": "no-cache",
    "Sec-Ch-Ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
names=[]
codes=[]
statuss=[]
day1s=[]
day2s=[]
links=[]
for i in range(1,2):
    url=f'https://openstd.samr.gov.cn/bzgk/gb/std_list_type?page={i}&pageSize=50&p.p1=2&p.p90=circulation_date&p.p91=desc'
    resp=requests.get(url=url,headers=headers)
    parse=etree.HTML(resp.text)
    code=parse.xpath('//table[@class="table result_list table-striped table-hover"]/tbody[2]/tr/td[2]/a/text()')
    name=parse.xpath('//table[@class="table result_list table-striped table-hover"]/tbody[2]/tr/td[4]/a/text()')
    status=parse.xpath('//table[@class="table result_list table-striped table-hover"]/tbody[2]/tr/td[5]/span/text()')
    day1=parse.xpath('//table[@class="table result_list table-striped table-hover"]/tbody[2]/tr/td[6]/text()')
    day2=parse.xpath('//table[@class="table result_list table-striped table-hover"]/tbody[2]/tr/td[7]/text()')
    link_id=parse.xpath('//table[@class="table result_list table-striped table-hover"]/tbody[2]/tr/td[8]/button/@onclick')
    for i in link_id:
        id=re.split(r'\'*\'',i)[1]
        link='https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno='+str(id)
        with lock:
            links.append(link)
            _redis.rpush('link', link)#rpush方法是将字符串推入redis的列表中
            
    with lock:
        codes.extend(code)
        names.extend(name)
        day1s.extend(day1)
        day2s.extend(day2)
        statuss.extend(status)
    
pdData={
    '标准号':codes,
    '标准名称':names,
    '发布日期':day1s,
    '实施日期':day2s,
    '状态':statuss,
    '查看详情':links,
}
df=pandas.DataFrame(pdData)
df.to_csv('标准.csv',index=False,encoding='utf-8')
    # print(resp.text[:5000])
