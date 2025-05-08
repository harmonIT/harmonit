import requests
from lxml import etree
import pandas
import threading
lock=threading.Lock()
titles=[]
commentNums=[]
quguos=[]
summarys=[]
threads=[]
strategys=[]
ranks=[]
stars=[]
beijings=[]
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "cookie": "QN1=0000f5002e186e4bd1c848b3; viewpoi=710603; _i=ueHd8ZkXXXVX1zLXdEOupBro5ERX; QN269=5C67AA00264211F0A8D95A4019A70869; fid=fe3e64ec-27a9-47c5-8a81-d56a1dc3fbb4; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN205=organic; QN277=organic; csrfToken=m4qMS5DMhZUdMhWrqyjtMSpvD9xrTNra; _vi=lqaf-iLOOgGbqByssBKSZq9qlxUyP9FfN6Q8RxsztNWmml4fyGPqNg65VXRjlq_4XpXyhfrWGYgAGPjxJkhuGmePLoYAp51Mj9w3iNLu3vibeweStJ2AIRhXgvrlPz7UHhMkLLhNRB-3xQxRc0Xm3Swnc767pGSKG21EFnZaYgAw; Hm_lvt_c56a2b5278263a647778d304009eafc=1746072691,1746488969; HMACCOUNT=9982405386288C7A; viewdist=299914-6; uld=1-299914-7-1746489221; JSESSIONID=EF2B95C5D68C93669A7FC1D0851732F8; QN267=01569806243b94d3edc; ariaDefaultTheme=undefined; Hm_lpvt_c56a2b5278263aa647778d304009eafc=1746489223; SECKEY_ABVK=nnCGhRUSoUlogMOGRAWQ9yiyCkjHiuCzAFSip2Musnsl2tWRizdzm9noI8uHrCDkmz7gOpEzk5mTVSxa37TXpQ%3D%3D; QN271=4d36d6a3-263a-478a-8eb4-18b997754b5a; BMAP_SECKEY=nnCGhRUSoUlogMOGRAWQ9yiyCkjHiuCzAFSip2MusnvrOUj6tosSrsVEb6Ud7jKxQDF9p4AWDxmyhYKQiqV6ea_nl_fp6sUVXiqaUnXN8PCYhrqhSnFM-4boLMQdAx8I5eDDLwRY1eLOWn3jbiOtRqJSITZK3468ZSdxCc2DAK_wD7aWv1zqTpEtYwpnP8qYegKWJSTycVyBQP5KdC1LBw",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://travel.qunar.com/p-cs299914-beijing-jingdian",
    "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
def sp(item):
    url=f'https://travel.qunar.com/p-cs299914-beijing-jingdian-1-{item}'
    resp=requests.get(url=url,headers=headers)
    parse=etree.HTML(resp.text)
    title=parse.xpath('//span[@class="cn_tit"]/text()')
    commentNum=parse.xpath('//div[@class="countbox"]/div[2]/text()')
    # 对每个标签检查其text内容
    for i in range(len(title)):
        i=i+1
        summary = parse.xpath("//div[@class='desbox'][%d]"%i)
        summary = [s.text if s.text else '' for s in summary] 
        with lock: 
            summarys.extend(summary)
    quguo=parse.xpath('//div[@class="ct"]/div[2]/span/span/text()')
    strategy=parse.xpath('//div[@class="strategy_sum"]//text()')
    rank=parse.xpath('//span[@class="ranking_sum"]/span/text()')
    for i in range(len(title)):
        i=i+1
        rank = parse.xpath('//span[@class="ranking_sum"][%d]'%i)#确保选到title长度的所有标签
        rank_text = [s.xpath('string()').strip() if s.text else '' for s in rank] 
        with lock: 
            ranks.extend(rank_text)
    star=parse.xpath('//span[@class="total_star"]/span/@style')
    for i in star:
        start_index = i.find('width:') + len('width:')  # 找到'width:'后面的位置
        if start_index != -1:  # 确保找到了'width:'
            width_value = i[start_index:i.find('%', start_index)]  # 获取'width:'后面的内容，直到下一个';'
            with lock:
                stars.append(width_value)
    for i in range(len(title)):
        beijing='北京'
        with lock:
            beijings.append(beijing)
    with lock:
        titles.extend(title)
        commentNums.extend(commentNum)
        quguos.extend(quguo)
        strategys.extend(strategy)

for i in range(1,4):
    thread=threading.Thread(target=sp,args=(i,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
# print(len(strategys),strategys)
# print(len(ranks),ranks)
# print(len(stars),stars)
pdData={
    '标题':titles,
    '评论数量':commentNums,
    '简介':summarys,
    '去过的驴友/%':quguos,
    '攻略数量':strategys,
    '排名':ranks,
    '评分':stars,
    '省份':beijings
}
df=pandas.DataFrame(pdData)
df.to_csv('去哪儿.csv',index=False,encoding='utf-8')
# print(resp.status_code,resp.text[:8000])

