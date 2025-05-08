import scrapy
from scrapyProj.items import ScrapyprojItem
import pandas
class SecondPageSpider(scrapy.Spider):
    name = 'second_spider'
    allowed_domains = ['openstd.samr.gov.cn']
    start_urls = ['https://openstd.samr.gov.cn/bzgk/gb/std_list_type?r=0.004168611642061948&page=2&pageSize=10&p.p1=2&p.p90=circulation_date&p.p91=desc']
    #self是类的实例
    def __init__(self, name = None, **kwargs):
        super(SecondPageSpider,self).__init__(name, **kwargs)
        self.data=[]
    def parse(self, response):
        for tr in response.xpath('//table[@class="table result_list table-striped table-hover"]/tbody[2]/tr'):
            item=ScrapyprojItem()
            item['num']=tr.xpath('td[2]//text()')
            item['bl']=tr.xpath('td[3]//text()')
            item['name']=tr.xpath('td[4]//text()')
            item['status']=tr.xpath('td[5]//text()')
            item['day1']=tr.xpath('td[6]//text()')
            item['day2']=tr.xpath('td[7]//text()')
            # onclick_value=tr.xpath('td[8]/button/@onclick')
            # if onclick_value:
            #     # 提取ID
            #     import re
            #     match = re.search(r"showInfo$'([^']+)'$", onclick_value)
            #     if match:
            #         id = match.group(1)
            #         # 生成详情链接
            #         item['link'] = f'https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno={id}'
            # print(f'打印的内容：{item}')
            # self.data.append(item)
            yield item
    
    def save(self,reason):
        df=pandas.DataFrame(self.data)
        df.to_csv('数据.csv',index=False,encoding='utf-8')
