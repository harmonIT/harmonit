import requests
import json
import csv
# data={
#     'searchStr':json.dumps('大学生就业指导'),
#     'page': 1,
#     'rows': 18,
#     'orderStr': json.dumps('hot'),
# }
data={
    'searchStr':'大学生就业指导',
    'page': 1,
    'rows': 18,
    'orderStr': 'hot',
}

url='https://www.ptpress.com.cn/bookinfo/getBookListForEBTag'
resp=requests.post(url=url,data=data)
# print(resp.status_code,resp.text)
jsData=json.loads(resp.text)
bookInfoList=jsData['data']['data']

bookNames=[]
prices=[]
authors=[]
for i in bookInfoList:
    bookName=i.get('bookName')
    price=i.get('discountPrice')
    author=i.get('author')
    bookNames.append(bookName)
    prices.append(price)
    authors.append(author)
    print(bookName)

with open('renyou.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # 写入表头
    writer.writerow(['书名','价格','作者'])
    for a,b,c in zip(bookNames,prices,authors):
        writer.writerow([a,b,c])


