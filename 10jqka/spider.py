import requests
from lxml import etree
import threading
import pandas
import time
#封IP！！！！
headers = {
    "Accept": "text/html, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "Hm_lvt_722143063e4892925903024537075d0d=1746083980; Hm_lpvt_722143063e4892925903024537075d0d=1746083980; HMACCOUNT=9982405386288C7A; log=; Hm_lvt_929f8b362150b1f77b477230541dbbc2=1746083981; Hm_lpvt_929f8b362150b1f77b477230541dbbc2=1746083981; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1746083981; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1746083981; v=A2IzVr2_fq5ouGLy_XKmxT6Hs-PBs2fdGLZa_6z-jCmBPQxdlEO23ehHqgh_",
    "Hexin-V": "A2IzVr2_fq5ouGLy_XKmxT6Hs-PBs2fdGLZa_6z-jCmBPQxdlEO23ehHqgh_",
    "Host": "q.10jqka.com.cn",
    "Pragma": "no-cache",
    "Referer": "https://q.10jqka.com.cn/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
lock=threading.Lock()
lists=[[] for _ in range(13)]
for num in range(11,21):
    url=f'https://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/{num}/ajax/1/'
    resp=requests.get(url=url,headers=headers)
    print(resp.status_code)
    parse=etree.HTML(resp.text)
    name=parse.xpath('//tr/td[3]/a/text()')
    code=parse.xpath('//tr/td[2]/a/text()')
    xianjia=parse.xpath('//tr/td[4]/text()')
    zhangdiefu=parse.xpath('//tr/td[5]/text()')
    zhangdie=parse.xpath('//tr/td[6]/text()')
    zhangsu=parse.xpath('//tr/td[7]/text()')
    huanshou=parse.xpath('//tr/td[8]/text()')
    liangbi=parse.xpath('//tr/td[9]/text()')
    zhenfu=parse.xpath('//tr/td[10]/text()')
    chengjaioe=parse.xpath('//tr/td[11]/text()')
    liutonggu=parse.xpath('//tr/td[12]/text()')
    liutongshizhi=parse.xpath('//tr/td[13]/text()')
    shiyinglv=parse.xpath('//tr/td[14]/text()')
    with lock:
        lists[0].extend(code)
        lists[1].extend(name)
        lists[2].extend(xianjia)
        lists[3].extend(zhangdiefu)
        lists[4].extend(zhangdie)
        lists[5].extend(zhangsu)
        lists[6].extend(huanshou)
        lists[7].extend(liangbi)
        lists[8].extend(zhenfu)
        lists[9].extend(chengjaioe)
        lists[10].extend(liutonggu)
        lists[11].extend(liutongshizhi)
        lists[12].extend(shiyinglv)
    time.sleep(5)


pdData={
    '股票代码':lists[0],
    '名称':lists[1],
    '现价':lists[2],
    '涨跌幅/%':lists[3],
    '涨跌':lists[4],
    '涨速/%':lists[5],
    '换手/%':lists[6],
    '量比':lists[7],
    '振幅/%':lists[8],
    '成交额':lists[9],
    '流通股':lists[10],
    '流通市值':lists[11],
    '市盈率':lists[12],
}
df = pandas.DataFrame(pdData)
df.to_csv('同花顺2.csv', index=False, encoding='utf-8')
