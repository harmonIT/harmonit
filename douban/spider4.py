import requests
from bs4 import BeautifulSoup
import mysql.connector
import pandas
import time

lists = [[] for _ in range(3)]
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Cookie": "bid=ZGJE0cKresI; viewed=\"36150914\"; vwouuid_v2=D6C938985375A05C35036A4857936D2A9|96c3e2e8812ab7bbd2150081245f25e1; push_noty_num=0; push_doumail_num=0; __utmv=30149280.21107; ll=\"118178\"; pkid.100001.4cf6=4527f66c7635e0a9.1745287564.; ga=GA1.1.566773364.1744769623; ga_Y4GN1R87RG=GS2.1.s1746847551$o1$g0$t1746847555$j0$l0$h0; __utmz=30149280.1747908329.15.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ap_v=0,6.0; utma=30149280.566773364.1744769623.1749172562.1749705717.21; utmc=30149280; utmt=1; utmb=30149280.6.10.1749705717; utma=223695111.461690259.1745287564.1747225279.1749705731.3; utmc=223695111; utmz=223695111.1749705731.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; pkref.100001.4cf6=%5B%22%22%2C%22%22%2C1749705731%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; pkses.100001.4cf6=1; utmb=223695111.6.10.1749705731",
    "Pragma": "no-cache",
    "Priority": "u=0, ireferer=https://movie.douban.com/subject/36742579/",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.33"
}
def spider():
    for i in range(4):
        url='https://movie.douban.com/top250?start={}&filter='.format(i*25)
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.select('span.title:nth-child(1)')
        for i in title:
            lists[0].append(i.text)
        comments = soup.select('div.bd div span:nth-child(4)')
        for i in comments:
            lists[1].append(i.text)
        link_ = soup.select('div.pic a img')
        for i in link_:
            lists[2].append(i.attrs['src'])
        time.sleep(4)
spider()

def mysql_():
    # 将数据保存到数据库
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="douban_db"
    )
    mycursor = mydb.cursor()
    # 创建表
    # create_table_sql = """
    # CREATE TABLE IF NOT EXISTS top250_movies (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     title VARCHAR(255),
    #     comment VARCHAR(250),
    #     image_url VARCHAR(255)
    # )
    # """
    # mycursor.execute(create_table_sql)

    # 构建插入数据的SQL语句
    insert_sql = """
    INSERT INTO top250_movies (
        title,comment,image_url
    ) VALUES (%s, %s, %s)
    """
    for i in range(len(lists[0])):
        val = (
            lists[0][i], 
            lists[1][i],  
            lists[2][i]
        )
        mycursor.execute(insert_sql, val)
    mydb.commit()

    print(mycursor.rowcount, "记录插入成功。")
    # 关闭数据库连接
    mydb.close()

mysql_()

#数据可视化
pdData={
    '电影原名':lists[0],
    '评论数':lists[1],
    '图片链接':lists[2],
}
df = pandas.DataFrame(pdData)
df.to_excel('清洗后的数据.xlsx', index=False)