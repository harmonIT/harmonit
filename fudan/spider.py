import requests
from lxml import etree
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'NSC_Xfc-DpoufouTxjudi-443=ffffffff090dee8945525d5f4f58455e445a4a423660; JSESSIONID=3584EA3E81FCD9B0C54ECF617D4F37F4; Hm_lvt_fc1056f0b298db1a6e4d85f644cb375d=1750217226; HMACCOUNT=9982405386288C7A; Hm_lpvt_fc1056f0b298db1a6e4d85f644cb375d=1750217456',
    'Host': 'news.fudan.edu.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://news.fudan.edu.cn/',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}
lists = [[] for _ in range(2)]
for i in range(1,9):
    url='https://news.fudan.edu.cn/xxyw/list{}.psp'.format(i)
    resp=requests.get(url=url,headers=headers)
    resp.encoding='utf-8'
    parse=etree.HTML(resp.text)
    title=parse.xpath('//li[@class="news i1 clearfix"]/@data-title')
    for i in title:
        lists[0].append(i)   
    content=parse.xpath('//div[@class="news_text"]/text()')
    for i in content:
        lists[1].append(i)

with open('复旦新闻.txt', 'w', encoding='utf-8') as file:
    for title, content in zip(lists[0], lists[1]):
        file.write(f"标题: {title}\n内容: {content}\n\n")
