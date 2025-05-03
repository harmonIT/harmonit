#将之前的代码用fitten code优化一下
#直接用JavaScript的谷歌插件爬取内容，可以绕过前端的js处理和加密等等
import asyncio
import aiohttp
from lxml import etree
import time

start1 = time.perf_counter()

async def fetch(session, url):
    async with session.get(url) as response:
        # print(f"请求完成 {url}")
        return await response.text()
async def parse_html(html_text):
    ids = []
    parse = etree.HTML(html_text)
    for j in range(1, 21):
        spans = parse.xpath("//div[@class='jc_a']//tr[%d]//span" % j)
        id = [span.text if span.text else '0' for span in spans]
        ids.append(id)
    return ids

async def main():
    ids = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
        'Cookie': '__jsluid_h=0747bd93184b21d2a421a868c173327b',
        'host': 'bp.people.com.cn',
    }

    urls = [
        'http://bp.people.com.cn/skygb/sk/index.php/index/seach/{}?pznum=&xmtype=0&xktype=0&xmname=&lxtime=0&xmleader=&zyzw=0&gzdw=&dwtype=211%E5%A4%A7%E5%AD%A6%E3%80%81985%E5%A4%A7%E5%AD%A6&szdq=0&ssxt=%E9%AB%98%E7%AD%89%E9%99%A2%E6%A0%A1%E3%80%81%E5%85%B6%E4%BB%96%E5%AD%A6%E6%A0%A1&cgname=&cgxs=0&cglevel=0&jxdata=0&jxnum=&cbs=&cbdate=0&zz=&hj='.format(i)
        for i in range(1, 10)
    ]

    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = []
        for url in urls:
            fetch_task = fetch(session, url)
            parse_task = asyncio.create_task(parse_html(await fetch_task))
            tasks.append(parse_task)
        
        results = await asyncio.gather(*tasks)
        for result in results:
            ids.extend(result)#将一个列表的所有元素添加到另一个列表中
asyncio.run(main())
end1 = time.perf_counter()
print(f"异步执行时间：{end1 - start1:.6f} 秒")

#异步编程相当于单线程中又开了一个协程，还是单线程执行，但是确实会快很多，
#主线程在创建子线程的时候，实现了并发的效果，那么我主线程依然是一个单线程，这时候我在主线程中使用异步编程，相当于主线程的协程，就进一步加快了代码的运行速度




