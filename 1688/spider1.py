from selenium import webdriver
from lxml import etree
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import re
import pandas
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Referer': 'http://alibaba.com.cn/',
        'Sec-Ch-Ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }
#数据处理
def clean(data):
    # 定义匹配模式
    pattern = re.compile(r'30天成交(\d+(\.\d+)?)万?件')
    # 处理数据
    processed_data = []
    for item in data:
        match = pattern.search(item)
        if match:
            # 提取数字部分
            num_str = match.group(1)
            # 判断是否有“万”
            if '万' in item:
                # 转换为浮点数并乘以10000
                num = float(num_str) * 10000
            else:
                # 直接转换为整数
                num = int(num_str)
            processed_data.append(int(num))  # 确保结果为整数
        else:
            # 如果没有匹配，直接提取数字
            num_str = re.search(r'\d+', item).group(0)
            # 转换为整数
            processed_data.append(int(num_str))
    return processed_data

titles=[]
sales=[]
firstPrices=[]
secondPrices=[]
prices=[]
phone_numbers=[]
shops=[]
def main():
    url='https://food.1688.com/?spm=a260k.dacugeneral.home2019category.18.555435e4kKZ5NW'
    # urlLogin='https://login.taobao.com/?redirect_url=https%3A%2F%2Flogin.1688.com%2Fmember%2Fjump.htm%3Ftarget%3Dhttps%253A%252F%252Flogin.1688.com%252Fmember%252FmarketSigninJump.htm%253FDone%253Dhttps%25253A%25252F%25252Fdetail.1688.com%25252Foffer%25252F650971882289.html%25253Fspm%25253Da261y.7663282.3002526303362591.2.24f61345XVSJQd%252526sk%25253Dorder&style=tao_custom&from=1688web'
    browser=webdriver.Chrome()
    # browser.get(url=urlLogin)
    # time.sleep(10)
    browser.get(url=url)
    parse1=etree.HTML(browser.page_source)
    title=parse1.xpath('//div[@class="offer-title"]/text()')
    titles.extend(title)
    allLink=parse1.xpath('//a[@class="offer"]/@href')
    sale=parse1.xpath('//div[@class="alife-bc-uc-textLine offer-vol single-line"]/text()')
    sale=clean(sale)
    sales.extend(sale)
    price=parse1.xpath('//span[@class="price-num"]//text()')
    for p in price:
        prices.append(float(p))
    for i in range(2):
        browser.get(url=allLink[i])
        try:
            daifa=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="od-pc-offer-tab-item"]')))
            daifa=daifa.get_attribute('href')
        except Exception as e:
            print('未找到代发元素')
            continue
        firstPrice=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="price-text"]')))
        firstPrice=firstPrice.text
        firstPrices.append(firstPrice)
        shop=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="hd_0_container_0"]//span')))
        shop=shop.text
        shops.append(shop)
        phoneLink=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//li[@class="contactinfo"]/a')))
        browser.execute_script("arguments[0].click();", phoneLink)
        window_handles = browser.window_handles
        browser.switch_to.window(window_handles[-1])#切换到最新页面
        phone=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="module-wrapper"]')))
        phone=str(phone.text)
        start_index = phone.find('手机：')
        phone_number = phone[start_index + len('手机：'): start_index + len('手机：') + 11]
        phone_numbers.append(phone_number)
        try:
            browser.get(url=daifa)
            # secondPrice=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="price-text"]')))
            secondPrice=browser.find_element(By.XPATH,'//span[@class="price-text"]')
            secondPrice=secondPrice.text
            secondPrices.append(float(secondPrice))
        except:
            print("代发价格获取失败")
            secondPrices.append(' ')
    print(shops)
    pdData={
        '商铺名称': shops,
        '商铺电话': phone_numbers,
        '单价': firstPrices,
        '批发价': secondPrices,
    }  
    df = pandas.DataFrame(pdData)
    df.to_csv('食品饮料.csv', index=False, encoding='utf-8')
    
    priceDict = dict(zip(prices, sales))
    sorted_dict = {k: priceDict[k] for k in sorted(priceDict)}
    plt.plot(list(sorted_dict.keys()), list(sorted_dict.values()), marker='o')
    # 添加标题和标签
    plt.title('Data Analysis')
    plt.xlabel('price')
    plt.ylabel('sale')
    plt.show()


    
    while True:
        time.sleep(2)

if __name__ == '__main__':
     main()