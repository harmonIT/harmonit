import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import threading
import pandas
import time
lock=threading.Lock()
proxies = {
    'http': 'socks5://127.0.0.1:1081',
    'https': 'socks5://127.0.0.1:1081',
}
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "cookie": "ASP.NET_SessionId=hbrpsq3poj4vrhbvv1scmedv; GASGOO_B2B_SEARCHKEY=gfkplMQHfUJfOdEll7Nbw5WLQ47fTVvQfj2AUEDowvXTFbhPG5mniA==; Hm_lvt_8e90480b1bf68ede548c407057660718=1746583791; HMACCOUNT=9982405386288C7A; cna=a045e65f6aa94062980064fc96a9515c; GASPSP_OUTER_URLREFER=https://i.gasgoo.com/supplier/Boom.aspx?cid=9425&page=2; _gid=GA1.2.1084810197.1746586565; _ga=GA1.1.1207433812.1746583791; .Gasgoo_FromAuthCookieName=EFC97A56EB3795A5A5B597B9D82269922185EB327A41C819E77F114AB7B4567F32B1DE87C7CC6436E84EF0AF8B35828696B6F6B1B755E393F829C8A8E765F331B3A5AA4C9DE80E0857C6EAF52D1B097BCCDC69F13943237FFDA2D85E351FCA96B0C92FD8537B73439722E2E6803580476790E38E298C6A6D4FDB99BE3C8386323120E5729E658FA03BEEF218AED335D4; GASGOO_SNS_USER=UserName=6h7frOCsoTGDBNKZtdkilQ==&Password=yAovM7c4Id5ah0XlwdzK9tq1jepK4sTNUGFDHuiIJcA=&isAutoLogin=uqiAyMXroYY=; GASGOO_SNS_USERID=oEpKRPaNMNE=; GASGOO_USER=https%3a%2f%2fc2.gasgoo.com%2faccount%2fimages%2fPerson.jpg%7c%e7%9b%96%e4%b8%96%e7%bd%91%e5%8f%8b_108b47e0fcda21e9%7c11477238%7cFalse%7cFalse%7cMinghua+%e9%99%88%7cQ3D%2fzYQnIBuT7rfCJRHmEA%3d%3d%7c1746586649319%7c0%7c1743994649; GASGOO_USER_EXPIRES=2025-05-21 10:57:29.3109 +08:00; GASGOO_SNS_NIO=NIOUser=0; GASGOO_SNS_USER_SALES_LOGIN=CN; _ga_3JW0F78HZ0=GS2.1.s1746586565$o1$g1$t1746586649$j0$l0$h0; Hm_lpvt_8e90480b1bf68ede548c407057660718=1746586692; _ga_GPM5E72JNY=GS2.1.s1746586486$o2$g1$t1746586695$j0$l0$h0",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://i.gasgoo.com/supplier/boom/c-9425/index-21.html",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
links=[]
def spLink(i):
    url1=f'https://i.gasgoo.com/supplier/boom/c-9425/index-{i}.html'
    resp=requests.get(url=url1,headers=headers,proxies=proxies)
    parse=etree.HTML(resp.text)
    link=parse.xpath('//div[@class="condInfo"]/a/@href')
    with lock:
        links.extend(link)
with ThreadPoolExecutor(max_workers=2) as executor:  # max_workers可以根据需要调整
    results = executor.map(spLink, range(1, 21))#64
print(links)

companyName_list = []
people_list = []
sales_list = []
website_list = []
zhijiepeitao_list = []
jianjiepeitao_list = []
zhuyaokehu_list = []
experience_list = []
zhuyingchanpin_list = []
daibiaoren_list = []
zhuceziben_list = []
chenglishijian_list = []
gongsixingzhi_list = []
suoshuhangye_list = []
suoshudi_list = []
yingwenming_list = []
zhucidizhi_list = []
name_list=[]
def spider(i):
    resp=requests.get(url=i,headers=headers,proxies=proxies)
    parse=etree.HTML(resp.text)
    companyName=parse.xpath('//div[@class="detailContent"]/div[2]//div[@class="companyName"]/text()')
    people=parse.xpath('//div[@class="detailContent"]/div[2]/table/tbody/tr[1]/td[2]/text()')
    sales=parse.xpath('//div[@class="detailContent"]/div[2]/table/tbody/tr[2]/td[2]/text()')
    website=parse.xpath('//div[@class="detailContent"]/div[2]/table/tbody/tr[3]/td[2]/text()')
    zhijiepeitao=parse.xpath('//div[@class="detailContent"]/div[2]/table/tbody/tr[4]//tr[1]/td/text()')
    jianjiepeitao=parse.xpath('//div[@class="detailContent"]/div[2]/table/tbody/tr[4]//tr[2]/td/text()')
    zhuyaokehu=parse.xpath('//div[@class="detailContent"]/div[2]/table/tbody/tr[4]//tr[3]/td[1]/text()')
    experience=parse.xpath('//div[@class="detailContent"]/div[2]/table/tbody/tr[5]/td[2]/text()')
    zhuyingchanpin=parse.xpath('//div[@class="detailContent"]/div[2]/table/tbody/tr[6]/td[2]/text()')

    # 使用条件表达式来处理可能为空的情况
    name = parse.xpath('//div[@class="detailContent"]/div[3]//div[@class="companyName"]/text()')
    if not daibiaoren:
        name = parse.xpath('//div[@class="detailContent"]/div[4]//div[@class="companyName"]/text()')
    if not daibiaoren:
        name = parse.xpath('//div[@class="detailContent"]/div[5]//div[@class="companyName"]/text()')

    daibiaoren = parse.xpath('//div[@class="detailContent"]/div[3]/table/tbody/tr[1]/td[2]/text()')
    if not daibiaoren:
        daibiaoren = parse.xpath('//div[@class="detailContent"]/div[5]/table/tbody/tr[1]/td[2]/text()')
    if not daibiaoren:
        daibiaoren = parse.xpath('//div[@class="detailContent"]/div[4]/table/tbody/tr[1]/td[2]/text()')
    
    zhuceziben = parse.xpath('//div[@class="detailContent"]/div[3]/table/tbody/tr[1]/td[4]/text()')
    if not zhuceziben:
        zhuceziben = parse.xpath('//div[@class="detailContent"]/div[5]/table/tbody/tr[1]/td[4]/text()')
    if not zhuceziben:
        zhuceziben = parse.xpath('//div[@class="detailContent"]/div[4]/table/tbody/tr[1]/td[4]/text()')
    
    chenglishijian = parse.xpath('//div[@class="detailContent"]/div[3]/table/tbody/tr[3]/td[4]/text()')
    if not chenglishijian:
        chenglishijian = parse.xpath('//div[@class="detailContent"]/div[5]/table/tbody/tr[3]/td[4]/text()')
    if not chenglishijian:
        chenglishijian = parse.xpath('//div[@class="detailContent"]/div[4]/table/tbody/tr[3]/td[4]/text()')
    
    gongsixingzhi = parse.xpath('//div[@class="detailContent"]/div[3]/table/tbody/tr[5]/td[2]/text()')
    if not gongsixingzhi:
        gongsixingzhi = parse.xpath('//div[@class="detailContent"]/div[5]/table/tbody/tr[5]/td[2]/text()')
    if not gongsixingzhi:
        gongsixingzhi = parse.xpath('//div[@class="detailContent"]/div[4]/table/tbody/tr[5]/td[2]/text()')
    
    suoshuhangye = parse.xpath('//div[@class="detailContent"]/div[3]/table/tbody/tr[6]/td[4]/text()')
    if not suoshuhangye:
        suoshuhangye = parse.xpath('//div[@class="detailContent"]/div[5]/table/tbody/tr[6]/td[4]/text()')
    if not suoshuhangye:
        suoshuhangye = parse.xpath('//div[@class="detailContent"]/div[4]/table/tbody/tr[6]/td[4]/text()')
    
    suoshudi = parse.xpath('//div[@class="detailContent"]/div[3]/table/tbody/tr[7]/td[2]/text()')
    if not suoshudi:
        suoshudi = parse.xpath('//div[@class="detailContent"]/div[5]/table/tbody/tr[7]/td[2]/text()')
    if not suoshudi:
        suoshudi = parse.xpath('//div[@class="detailContent"]/div[4]/table/tbody/tr[7]/td[2]/text()')
    
    yingwenming = parse.xpath('//div[@class="detailContent"]/div[3]/table/tbody/tr[8]/td[4]/text()')
    if not yingwenming:
        yingwenming = parse.xpath('//div[@class="detailContent"]/div[5]/table/tbody/tr[8]/td[4]/text()')
    if not yingwenming:
        yingwenming = parse.xpath('//div[@class="detailContent"]/div[4]/table/tbody/tr[8]/td[4]/text()')
    
    zhucidizhi = parse.xpath('//div[@class="detailContent"]/div[3]/table/tbody/tr[10]/td[4]/text()')
    if not zhucidizhi:
        zhucidizhi = parse.xpath('//div[@class="detailContent"]/div[5]/table/tbody/tr[10]/td[4]/text()')
    if not zhucidizhi:
        zhucidizhi = parse.xpath('//div[@class="detailContent"]/div[4]/table/tbody/tr[10]/td[4]/text()')
    with lock:
        companyName_list.extend(companyName)
        people_list.extend(people)
        sales_list.extend(sales)
        website_list.extend(website)
        zhijiepeitao_list.extend(zhijiepeitao)
        jianjiepeitao_list.extend(jianjiepeitao)
        zhuyaokehu_list.extend(zhuyaokehu)
        experience_list.extend(experience)
        zhuyingchanpin_list.extend(zhuyingchanpin)
        daibiaoren_list.extend(daibiaoren)
        zhuceziben_list.extend(zhuceziben)
        chenglishijian_list.extend(chenglishijian)
        gongsixingzhi_list.extend(gongsixingzhi)
        suoshuhangye_list.extend(suoshuhangye)
        suoshudi_list.extend(suoshudi)
        yingwenming_list.extend(yingwenming)
        zhucidizhi_list.extend(zhucidizhi)
        name_list.extend(name)
    time.sleep(1)
with ThreadPoolExecutor(max_workers=8) as executor:  # max_workers可以根据需要调整
    results = executor.map(spider, links)#64
# 打印每个列表及其长度
print(f"companyName: {companyName_list}, Length: {len(companyName_list)}")
print(f"people: {people_list}, Length: {len(people_list)}")
print(f"sales: {sales_list}, Length: {len(sales_list)}")
print(f"website: {website_list}, Length: {len(website_list)}")
print(f"zhijiepeitao: {zhijiepeitao_list}, Length: {len(zhijiepeitao_list)}")
print(f"jianjiepeitao: {jianjiepeitao_list}, Length: {len(jianjiepeitao_list)}")
print(f"zhuyaokehu: {zhuyaokehu_list}, Length: {len(zhuyaokehu_list)}")
print(f"experience: {experience_list}, Length: {len(experience_list)}")
print(f"zhuyingchanpin: {zhuyingchanpin_list}, Length: {len(zhuyingchanpin_list)}")
print(f"daibiaoren: {daibiaoren_list}, Length: {len(daibiaoren_list)}")
print(f"zhuceziben: {zhuceziben_list}, Length: {len(zhuceziben_list)}")
print(f"chenglishijian: {chenglishijian_list}, Length: {len(chenglishijian_list)}")
print(f"gongsixingzhi: {gongsixingzhi_list}, Length: {len(gongsixingzhi_list)}")
print(f"suoshuhangye: {suoshuhangye_list}, Length: {len(suoshuhangye_list)}")
print(f"suoshudi: {suoshudi_list}, Length: {len(suoshudi_list)}")
print(f"yingwenming: {yingwenming_list}, Length: {len(yingwenming_list)}")
print(f"zhucidizhi: {zhucidizhi_list}, Length: {len(zhucidizhi_list)}")
# print(resp.status_code,resp.text[:8000])'''

pdData1={
    '业务信息/公司名称':companyName_list,
    '人员规模':people_list,
    '年销售额':sales_list,
    '公司网址':website_list,
    '直接配套':zhijiepeitao_list,
    '简介配套':jianjiepeitao_list,
    '主要客户':zhuyaokehu_list,
    '直接出口经验':experience_list,
    '主营产品':zhuyingchanpin_list,
}

df=pandas.DataFrame(pdData1)
df.to_csv('盖世汽车.csv',index=False,encoding='utf-8')
pdData2={
    '公司名称':name_list,
    '法定代表人':daibiaoren_list,
    '注册资本':zhuceziben_list,
    '成立时间':chenglishijian_list,
    '公司性质':gongsixingzhi_list,
    '所属行业':suoshuhangye_list,
    '所属地':suoshudi_list,
    '英文名':yingwenming_list,
    '注册地址':zhucidizhi_list,
}
df2=pandas.DataFrame(pdData2)
df2.to_csv('盖世汽车2.csv',index=False,encoding='utf-8')