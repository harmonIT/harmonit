import requests
from lxml import etree
import csv
import chardet
# from concurrent.futures import ThreadPoolExecutor
link=[]
biaotiS=[]
zhaiyaoS=[]
riqiS=[]
urls=[
    'http://www.ocpe.com.cn/new/new1/',
]
for j in urls:
    url=j
    headers={
        "cookie":"qkchtecookieinforecord=%2C183-4736%2C",
        "Host":"www.ocpe.com.cn",
        "Referer":"http://www.ocpe.com.cn/new/",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    }
    resp=requests.get(url=url,headers=headers)

    print(resp.status_code)
    # de=gzip.decompress(resp.content)#解压缩
    detect_result = chardet.detect(resp.content)#识别编码
    encoding = detect_result['encoding']
    print("Detected Encoding:", encoding)
    # print(de[:500])
    de=resp.content.decode(encoding,errors='ignore')
    parse=etree.HTML(de)#解码
    biaoti=parse.xpath('//div[@class="xwt"]/div[@class="xwt_a"]/a/text()')
    lianjie=parse.xpath('//div[@class="xwt"]/div[@class="xwt_a"]/a/@href')
    for i in lianjie:
        i='http://www.ocpe.com.cn'+i
        link.append(i)
    zhaiyao=parse.xpath('//div[@class="xwt"]/div[@class="xwt_b"]/text()')
    riqi=parse.xpath('//div[@class="xwt"]/div[@class="xwt_c"]/text()')
    for a,b,c in zip(biaoti,zhaiyao,riqi):
        biaotiS.append(a)
        zhaiyaoS.append(b)
        riqiS.append(c)

with open('新能资讯7.csv','w',encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(['标题','链接','摘要','日期'])
    for a,b,c,d in zip(biaotiS,link,zhaiyaoS,riqiS):
        writer.writerow([a,b,c,d])

