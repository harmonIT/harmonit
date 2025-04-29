import requests
import json
import threading
import pandas
lock=threading.Lock()
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "cookie": "MALL_SHOPCAR=6aac8832-64cd-4835-b44b-4b230c5bc92d; isHttps=1; _ecs_tracker_sid=e44269a1cad12755; _ecs_tracker_cid=9288e2e2e6763c7a; _ecs_tracker_chn=wap; pageId=90005; agbrowser_id=75b336375438e26e85420e0ca329773d; ORDER_SCREEN={\"pageId\":\"90005\",\"prodId\":\"0002974720\"}; _csrf=bb35918ef31652ced613cd65d1a36e52; zg_did=%7B%22did%22%3A%20%22196800f2e084f-00aab2e6b99cd5-26011c51-144000-196800f2e09516%22%7D; zg_002714230c264ddda7d94375a4d23e40=%7B%22sid%22%3A%201745905200653%2C%22updated%22%3A%201745907201859%2C%22info%22%3A%201745905200656%2C%22superProperty%22%3A%20%22%7B%5C%22app_id%5C%22%3A%20%5C%22vcpcx2dfh8g6k4y3%5C%22%2C%5C%22user_id%5C%22%3A%20%5C%22TRAVEL_USER%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.google.com%22%7D",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://buy.shanrongmall.com/shop/indexTouch.jhtml?shopId=020698",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
prodNameList=[]
saleAmtSumList=[]
prodOriginPriceList=[]
prodPriceList=[]
def sp(i):
    url=f'https://buy.shanrongmall.com/searchproducts/mTouchSearchAjax.jhtml?storeId=020698&p={i}&ispsz=0&sap=1&cp=1&query=*'
    resp=requests.get(url=url,headers=headers)
    print(resp.status_code)
    jsonData=json.loads(resp.text)
    with lock:
        prodNameList.extend([i['prodName'] for i in jsonData['productlist']])
        saleAmtSumList.extend([i['saleAmtSum'] for i in jsonData['productlist']])
        prodOriginPriceList.extend([i['prodOriginPrice'] for i in jsonData['productlist']])
        prodPriceList.extend([i['prodPrice'] for i in jsonData['productlist']])
threads=[]
for i in range(9,13):
    thread=threading.Thread(target=sp,args=(i,))
    threads.append(thread)
    thread.start()
for i in threads:
    i.join()
pdData={
    '商品名称': prodNameList,
    '销量': saleAmtSumList,
    '折前价格': prodOriginPriceList,
    '折后价格': prodPriceList,
}  
df = pandas.DataFrame(pdData)
df.to_csv('良品铺子2.csv', index=False, encoding='utf-8')
