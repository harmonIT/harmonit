import requests
from lxml import etree
import time
from concurrent.futures import ThreadPoolExecutor
import threading

start1 = time.perf_counter()
ids=[]
lock=threading.Lock()
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
    for j in range(1,21):
        spans = parse.xpath("//div[@class='jc_a']//tr[%d]//span" % j)
        #列表推导式
        id = [span.text if span.text else '0' for span in spans]  # 对每个span标签检查其text内容
        
        ids.append(id)
end1=time.perf_counter()
print(f"单线程执行时间：{end1 - start1:.6f} 秒")

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
    for i in range(1,21):
        spans = parse.xpath("//div[@class='jc_a']//tr[%d]//span" % i)
        #列表推导式
        id = [span.text if span.text else '0' for span in spans]  # 对每个span标签检查其text内容
        with lock:
            ids.append(id)
with ThreadPoolExecutor(max_workers=9) as executor:  # max_workers可以根据需要调整
    results = executor.map(fetch_and_parse, range(1, 10),chunksize=9)
end2 = time.perf_counter()
print(f"ThreadPoolExecutor多线程执行时间：{end2 - start2:.6f} 秒")



start3=time.perf_counter()
threads = []
for i in range(9):
    thread = threading.Thread(target=fetch_and_parse, args=(i,))
    threads.append(thread)
    thread.start()
#join()方法是添加主线程，相当于把threads列表所在的线程作为主线程，
#对for i in range(10)里面创建的子线程一个一个启用，启用期间主线程不会执行操作，等待所有子线程执行完毕后，主线程再执行代码
#如果不加这个join()方法，还可能会出现主线程结束，子线程没有执行完毕的情况
for thread in threads:
    thread.join()
end3=time.perf_counter()
# print(ids)
print(f"Treading多线程执行时间：{end3 - start3:.6f} 秒")

#输出结果：
'''1 200
2 200
3 200
4 200
5 200
6 200
7 200
8 200
9 200
单线程执行时间：4.855380 秒
5 200
7 200
3 200
6 200
8 200
1 200
9 200
4 200
2 200
ThreadPoolExecutor多线程执行时间：0.772810 秒
3 200
5 200
4 200
8 200
2 200
9 200
6 200
3 200
5 200
4 200
8 200
2 200
3 200
5 200
4 200
3 200
5 200
3 200
3 200
5 200
4 200
8 200
2 200
9 200
6 200
Treading多线程执行时间：0.810824 秒'''

#总结：threading库比较原始，不太好控制，单纯for循环控制的线程也比较慢，使用ThreadPoolExecutor线程池管理器会更高校一点，操作简单