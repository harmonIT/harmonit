import requests
import redis
from lxml import etree
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
url='https://movie.douban.com/subject/36742579/comments?limit=20&status=P&sort=new_score'
proxies = {
    'http': 'socks5://127.0.0.1:1081',
    'https': 'socks5://127.0.0.1:1081',
}
# response=requests.get(url=url,headers=headers)
# print(response.text[:5000])
r = redis.Redis(host='127.0.0.1')
# r.set('douban',response.text)
text=r.get('douban')
parse=etree.HTML(text)
comment=parse.xpath('//span[@class="short"]/text()')
print(comment[0:5])
#只能爬取一页内容，第二页的响应内容在开发者工具中显示乱码
