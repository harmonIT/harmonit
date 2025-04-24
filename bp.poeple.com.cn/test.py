import requests
from lxml import etree
import time
from concurrent.futures import ThreadPoolExecutor
import threading

start = time.perf_counter()
ids=[]
for i in range(1,10):
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
end=time.perf_counter()
print(f"单线程执行时间：{end - start:.6f} 秒")

start1 = time.perf_counter()
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
    for i in range(1,21):
        spans = parse.xpath("//div[@class='jc_a']//tr[%d]//span" % i)
        #列表推导式
        id = [span.text if span.text else '0' for span in spans]  # 对每个span标签检查其text内容
        ids.append(id)


with ThreadPoolExecutor(max_workers=5) as executor:  # max_workers可以根据需要调整
    results = executor.map(fetch_and_parse, range(1, 10))
end1 = time.perf_counter()
print(f"线程池多线程执行时间：{end1 - start1:.6f} 秒")

start2 = time.perf_counter()

threads = []
for i in range(5):
    thread = threading.Thread(target=fetch_and_parse, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


