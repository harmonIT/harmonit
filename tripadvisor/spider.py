import requests
import json
import threading
import pandas
lock=threading.Lock()
titleList=[]
idList=[]
coList=[]
url='https://api.tripadvisor.cn/restapi/soa2/20997/getList'
def sp(i):
    data={"frontPage": "USER_REVIEWS", "locationId": 6589242, "pageInfo": { "num": i, "size": 10 }, "selected": { "airlineIds": [], "airlineLevel": [], "airlineSeatIds": [], "langs": ["zhCN"], "ratings": [], "seasons": [], "tripTypes": [] } }
    data=json.dumps(data)
    resp=requests.post(url=url,data=data)
    print(resp.status_code)
    jsonData=json.loads(resp.text)
    with lock:
        titleList.extend([i['content'] for i in jsonData['details']])
        idList.extend([i['userReviewId'] for i in jsonData['details']])
        coList.extend([i['submitTime'] for i in jsonData['details']])
threads=[]
for i in range(1,8):
    thread=threading.Thread(target=sp,args=(i,))
    threads.append(thread)
    thread.start()
for i in threads:
    i.join()

# print(idList)
pdData={
    '评论用户id': idList,
    '评论内容': titleList,
    '评论提交时间': coList,
}  
df = pandas.DataFrame(pdData)
df.to_csv('tripadvisor.csv', index=False, encoding='utf-8')
