import requests
import json
import csv
import threading
#我想获取人民邮电出版社的图书信息，购买的时候可以选择更好的，适合自己的书
#打开人民邮电出版社官网：https://www.ptpress.com.cn/shopping/index
#点击更多后我开始搜索我想要购买的计算机类别的书籍，我发现无法无法获取全部的书籍信息，只能获取一页的数据
#网站采用AJAX异步加载页面，有反爬虫技术
#解决方案：按f12打开浏览器的开发者工具，发现了AJAX异步加载的接口api，用requests库发送post请求，传入动态变化的page数，就可以爬取所有页面

#创建存储信息的列表
bookNames=[]
prices=[]
authors=[]
#创建线程锁
lock=threading.Lock()
#定义爬虫函数
def spiders(pageNum):
    data={
        'bookTagId':'a15a734f-0ae9-41d7-9012-6ef9de2e71c8',
        'page': pageNum,
        'rows': 18,
        'orderStr': 'hot',
    }
    url='https://www.ptpress.com.cn/bookinfo/getBookListForEBTag'
    #post请求
    resp=requests.post(url=url,data=data)
    # print(resp.status_code,resp.text)
    jsData=json.loads(resp.text)
    bookInfoList=jsData['data']['data']

    for i in bookInfoList:
        bookName=i.get('bookName')
        price=i.get('discountPrice')
        author=i.get('author')
        with lock:
            bookNames.append(bookName)
            prices.append(price)
            authors.append(author)

#启动程序,爬取前十页书籍信息
threads=[]
for i in range(1,3):
    thread=threading.Thread(target=spiders,args=(i,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

#保存为csv文件，之后导入excel表格方便分析，选择更好的书
with open('计算机类书籍信息.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # 写入表头
    writer.writerow(['书名','价格','作者'])
    for a,b,c in zip(bookNames,prices,authors):
        writer.writerow([a,b,c])


