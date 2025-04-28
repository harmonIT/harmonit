import time
from concurrent.futures import ProcessPoolExecutor
from lxml import etree
import requests
import threading

ids=[]
lock=threading.Lock()
start2 = time.perf_counter()
def fetch_and_parse(i):
    url = 'http://bp.people.com.cn/skygb/sk/index.php/index/seach/{}?pznum=&xmtype=0&xktype=0&xmname=&lxtime=0&xmleader=&zyzw=0&gzdw=&dwtype=211%E5%A4%A7%E5%AD%A6%E3%80%81985%E5%A4%A7%E5%AD%A6&szdq=0&ssxt=%E9%AB%98%E7%AD%89%E9%99%A2%E6%A0%A1%E3%80%81%E5%85%B6%E4%BB%96%E5%AD%A6%E6%A0%A1&cgname=&cgxs=0&cglevel=0&jxdata=0&jxnum=&cbs=&cbdate=0&zz=&hj='.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
        'Cookie': '__jsluid_h=0747bd93184b21d2a421a868c173327b',
        'Referer': url,
        'host': 'bp.people.com.cn',
    }

    response = requests.get(url=url, headers=headers)
    print(i, response.status_code)
    parse = etree.HTML(response.text)
    for j in range(1, 21):  # 修改此处循环变量名避免冲突
        spans = parse.xpath("//div[@class='jc_a']//tr[%d]//span" % j)
        # 列表推导式
        id = [span.text if span.text else '0' for span in spans]  # 对每个span标签检查其text内容
        with lock:
            ids.append(id)

with ProcessPoolExecutor(max_workers=10) as executor:  # max_workers可以根据需要调整
    executor.map(fetch_and_parse, range(1, 10))  
end2 = time.perf_counter()
print(ids)
print('多进程处理所用时间:', end2 - start2)
print('收集到的ID列表:', ids)
