import requests
import json
import threading
urlList=[
    'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?page=7&pageSize=15&city=100010000&position=&query=&expectInfo=&multiSubway=&multiBusinessDistrict=&jobType=&salary=&experience=&degree=&industry=&scale=&stage=&scene=1&_=1745895657600',
    'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?page=8&pageSize=15&city=100010000&position=&query=&expectInfo=&multiSubway=&multiBusinessDistrict=&jobType=&salary=&experience=&degree=&industry=&scale=&stage=&scene=1&_=1745895273912',
]
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.zhipin.com/web/geek/jobs?city=100010000",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
}

def Ma(url):
    resp=requests.get(url=url,headers=headers)
    print(resp.status_code,resp.text)
    # jsonData=json.loads(resp.text)
    # jobList=jsonData.get('jobList')
    # print(jobList[0])

Ma(urlList[0])
thread=threading.Thread(target=Ma,args=(urlList[1],))
thread.start()
thread.join()

