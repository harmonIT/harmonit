import requests
from lxml import etree
import pandas
import chardet
import time
import threading
start=time.perf_counter()
link=[]
biaotiS=[]
zhaiyaoS=[]
riqiS=[]
urls=[
    'http://www.ocpe.com.cn/new/new1/',
    'http://www.ocpe.com.cn/new/new2/index_2.html',
]
lock=threading.Lock()
def th(j):
    headers={
        "cookie":"qkchtecookieinforecord=%2C183-4736%2C",
        "Host":"www.ocpe.com.cn",
        "Referer":"http://www.ocpe.com.cn/new/",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    }
    resp=requests.get(url=j,headers=headers)

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
        with lock:
            biaotiS.append(a)
            zhaiyaoS.append(b)
            riqiS.append(c)

th(urls[0])
thread=threading.Thread(target=th,args=(urls[1],))#这里urls[1]后面需要加一个逗号，因为这个args属性需要接收一个元组，而不是列表元素
thread.start()
thread.join()

data = {
    '标题': biaotiS,
    '链接': link,
    '摘要': zhaiyaoS,
    '日期': riqiS
}
df = pandas.DataFrame(data)
df.to_csv('新能资讯pandas.csv', index=False, encoding='utf-8')
end=time.perf_counter()
print(end-start)

#单独只开一个子线程，算上线程创建和销毁的资源消耗和时间，并不能提高多少运行性能的提升！