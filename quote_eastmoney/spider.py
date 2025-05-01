import requests
import json
import threading
import pandas
lock=threading.Lock()
lists=[[] for _ in range(16)]
def sp(num):
    url=f'https://push2.eastmoney.com/api/qt/clist/get?np=1&fltt=1&invt=2&cb=jQuery371008049624345479434_1746072370503&fs=m%3A0%2Bt%3A6%2Cm%3A0%2Bt%3A80%2Cm%3A1%2Bt%3A2%2Cm%3A1%2Bt%3A23%2Cm%3A0%2Bt%3A81%2Bs%3A2048&fields=f12%2Cf13%2Cf14%2Cf1%2Cf2%2Cf4%2Cf3%2Cf152%2Cf5%2Cf6%2Cf7%2Cf15%2Cf18%2Cf16%2Cf17%2Cf10%2Cf8%2Cf9%2Cf23&fid=f3&pn={num}&pz=20&po=1&dect=1&ut=fa5fd1943c7b386f172d6893dbfba10b&wbp2u=%7C0%7C0%7C0%7Cweb&_=1746072370509'
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "fullscreengg=1; fullscreengg2=1; qgqp_b_id=186fecb4dcc9eacdcf0bb80b41f0ef1b; st_si=40739339354884; st_asi=delete; st_pvi=30572022778758; st_sp=2025-05-01%2012%3A05%3A33; st_inirUrl=; st_sn=3; st_psi=2025050112061154-113200301321-5946378664",
        "Host": "push2.eastmoney.com",
        "Pragma": "no-cache",
        "Referer": "https://quote.eastmoney.com/center/gridlist.html",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    }

    resp=requests.get(url=url,headers=headers)
    print(resp.status_code)
    start = resp.text.find('{')
    end = resp.text.rfind('}') + 1
    cleaned_text = resp.text[start:end]
    jsData=json.loads(cleaned_text)
    diff=jsData['data']['diff']
    for i in range(len(diff)):
        daima = f"{int(diff[i]['f12']):06d}"
        name=diff[i]['f14']
        zuixinjia=float(diff[i]['f2']/100)
        zhangdiefu=float(diff[i]['f3']/100)
        zhangdiee=float(diff[i]['f4']/100)
        chengjiaoliang=float(diff[i]['f5']/100)
        chengjiaoe=float(diff[i]['f6']/100000000)
        zhenfu=float(diff[i]['f7']/100)
        zuigao=float(diff[i]['f15']/100)
        zuidi=float(diff[i]['f16']/100)
        jinkai=float(diff[i]['f17']/100)
        zuoshou=float(diff[i]['f18']/100)
        liangbi=float(diff[i]['f10']/100)
        huanshoulv=float(diff[i]['f8']/100)
        shiyinglv=float(diff[i]['f9']/100)
        shijinglv=float(diff[i]['f23']/100)

        with lock:
            lists[0].append(daima)
            lists[1].append(name)
            lists[2].append(zuixinjia)
            lists[3].append(zhangdiefu)
            lists[4].append(zhangdiee)
            lists[5].append(chengjiaoliang)
            lists[6].append(chengjiaoe)
            lists[7].append(zhenfu)
            lists[8].append(zuigao)
            lists[9].append(zuidi)
            lists[10].append(jinkai)
            lists[11].append(zuoshou)
            lists[12].append(liangbi)
            lists[13].append(huanshoulv)
            lists[14].append(shiyinglv)
            lists[15].append(shijinglv)

threads=[]
for i in range(1,11):
    thread=threading.Thread(target=sp,args=(i,))
    threads.append(thread)
    thread.start()
for i in threads:
    i.join()
pdData={
    '股票代码':lists[0],
    '名称':lists[1],
    '最新价/元':lists[2],
    '涨跌幅/%':lists[3],
    '涨跌额/元':lists[4],
    '成交量/万':lists[5],
    '成交额/亿':lists[6],
    '振幅/%':lists[7],
    '最高/元':lists[8],
    '最低/元':lists[9],
    '今开/元':lists[10],
    '昨收/元':lists[11],
    '量比':lists[12],
    '换手率/%':lists[13],
    '市盈率':lists[14],
    '市净率':lists[15],
}
df = pandas.DataFrame(pdData)
df.to_csv('东方财富.csv', index=False, encoding='utf-8')

for i in lists:
    print(i)
