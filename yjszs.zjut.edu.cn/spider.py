import requests
import json
from lxml import etree
import time
url='https://yjszs.zjut.edu.cn/gsapp/sys/dszszgxxykfwappzjut/modules/dszsxx/dszsxx_lbcx.do'
#这个data数据是关键，不能把整个data数据转化json，只对某个值转化
data={
    'querySetting': json.dumps([{"name":"XKSZDWDM","caption":"所在院系","linkOpt":"AND","builderList":"cbl_m_List","builder":"m_value_equal","value":"008","value_display":"计算机科学与技术学院（软件学院）"},{"name":"_gotoFirstPage","value":True,"linkOpt":"AND","builder":"equal"}]),
    "pageSize": 100,
    "pageNumber": 1
}

# data=json.dumps(data)
# select=requests.post(url='https://yjszs.zjut.edu.cn/gsapp/code/e97d54a1-6cad-4e1e-a0a7-9c457dd3b585.do')
# print(select.status_code,select.text)

res=requests.post(url=url,data=data)
urls=[]
# names=[]
d_ata=json.loads(res.text)
rows=d_ata['datas']['dszsxx_lbcx']['rows']
for row in rows:
    grzylj = row.get('GRZYLJ')
    urls.append(grzylj)
    # if grzylj and isinstance(grzylj, str):
    #     urls.append(grzylj)
# for name in names:
#     xm=name.get('XM')
#     names.append(xm)
for i in urls:
    if i!=None:
        resp=requests.get(url=i)
        time.sleep(2)
        resp.encoding='utf-8'
        t_ext=resp.text
        parse=etree.HTML(t_ext)
        name=parse.xpath('//h1[@class="news_title"]/text()')
        name=name[0]
        with open("%s.html"%name, "w",encoding='utf-8') as f:
            f.write(t_ext)


# print(urls)
