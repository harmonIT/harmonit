import requests
from lxml import etree
import time
import csv
ids=[]
#多线程爬取
#ip代理池

for i in range(1,92):
    url='http://bp.people.com.cn/skygb/sk/index.php/index/seach/{}?pznum=&xmtype=0&xktype=0&xmname=&lxtime=0&xmleader=&zyzw=0&gzdw=&dwtype=211%E5%A4%A7%E5%AD%A6%E3%80%81985%E5%A4%A7%E5%AD%A6&szdq=0&ssxt=%E9%AB%98%E7%AD%89%E9%99%A2%E6%A0%A1%E3%80%81%E5%85%B6%E4%BB%96%E5%AD%A6%E6%A0%A1&cgname=&cgxs=0&cglevel=0&jxdata=0&jxnum=&cbs=&cbdate=0&zz=&hj='.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
        'Cookie':'__jsluid_h=0747bd93184b21d2a421a868c173327b',
        'Referer':url,
        'host':'bp.people.com.cn',
    }

    response = requests.get(url=url,headers=headers)
    print(i,response.status_code)
    parse=etree.HTML(response.text)
    for i in range(1,21):
        spans = parse.xpath("//div[@class='jc_a']//tr[%d]//span" % i)
        #列表推导式
        id = [span.text if span.text else '0' for span in spans]  # 对每个span标签检查其text内容
        ids.append(id)
    time.sleep(1)

with open('goujiashekejijin.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # 写入表头
    writer.writerow(['项目批准号', '项目类别', '学科分类', '项目名称', '立项时间', '项目负责人', '专业职务', '工作单位', '单位类别', '所属省市', '所属系统', '成果名称', '成果形式', '成果等级'])
    # 写入数据
    writer.writerows(ids)

