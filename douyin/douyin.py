import requests
from lxml import etree
import time
import csv
ids=[]

for i in range(1,2):
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
        id=parse.xpath("//div[@class='jc_a']//tr[%d]//span/text()"%i)
        if not parse.xpath("//div[@class='jc_a']//tr[%d]//td[3]//span/text()"%i):
            id.insert(2,'0')
        if not parse.xpath("//div[@class='jc_a']//tr[%d]//td[11]//span/text()"%i):
            id.insert(10,'0')
        if not parse.xpath("//div[@class='jc_a']//tr[%d]//td[12]//span/text()"%i):
            id.insert(11,'0')
        if not parse.xpath("//div[@class='jc_a']//tr[%d]//td[13]//span/text()"%i):
            id.insert(12,'0')
        ids.append(id)
    time.sleep(1)
# print(ids)
with open('goujiashekejijin.txt','w',encoding='utf-8') as f:
    f.write(str(ids))


with open('goujiashekejijin.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # 写入表头
    writer.writerow(['项目批准号', '项目类别', '学科分类', '项目名称', '立项时间', '项目负责人', '专业职务', '工作单位', '单位类别', '所属省市', '所属系统', '成果名称', '成果形式', '成果等级'])
    # 写入数据
    writer.writerows(ids)

# workbook=xlwt.Workbook(encoding='utf-8')
# worksheet=workbook.add_sheet('Example one',cell_overwrite_ok=True)
# list=['项目批准号','项目类别','学科分类','项目名称','立项时间','项目负责人','专业职务','工作单位','单位类别','所属省市','所属系统','成果名称','成果形式','成果等级']
# try:
#     for i in range(14):
#         worksheet.write(0,i,list[i])
#     for i in range(1,len(ids)):
#         worksheet.write(i,0,ids[i-1][0])
#     for i in range(1,len(ids)):
#         worksheet.write(i,1,ids[i-1][1])
#     for i in range(1,len(ids)):
#         worksheet.write(i,2,ids[i-1][2])
#     for i in range(1,len(ids)):
#         worksheet.write(i,3,ids[i-1][3])
#     for i in range(1,len(ids)):
#         worksheet.write(i,4,ids[i-1][4])
#     for i in range(1,len(ids)):
#         worksheet.write(i,5,ids[i-1][5])
#     for i in range(1,len(ids)):
#         worksheet.write(i,6,ids[i-1][6])
#     for i in range(1,len(ids)):
#         worksheet.write(i,7,ids[i-1][7])
#     for i in range(1,len(ids)):
#         worksheet.write(i,8,ids[i-1][8])
#     for i in range(1,len(ids)):
#         worksheet.write(i,9,ids[i-1][9])
#     for i in range(1,len(ids)):
#         worksheet.write(i,10,ids[i-1][10])
#     for i in range(1,len(ids)):
#         worksheet.write(i,11,ids[i-1][11])
#     for i in range(1,len(ids)):
#         worksheet.write(i,12,ids[i-1][12])
#     for i in range(1,len(ids)):
#         worksheet.write(i,13,ids[i-1][13])
    
# except:
#     workbook.save('goujiashekejijin.xls')
#     print('error')

