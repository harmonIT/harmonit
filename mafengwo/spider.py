import requests
import json
import redis
r = redis.Redis(host='127.0.0.1')
url='https://pagelet.mafengwo.cn/note/pagelet/recommendNoteApi?callback=jQuery18107688088137122294_1752626203337&params=%7B%22type%22%3A0%2C%22objid%22%3A0%2C%22page%22%3A2%2C%22ajax%22%3A1%2C%22retina%22%3A1%7D&_=1752626213651'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Cookie': 'PHPSESSID=9i1sls4l3ba7kf2j6i02tgvv56; mfw_uuid=6675a26a-4e29-b562-c5d9-f840a1e6bfa0; uva=s%3A92%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1752539754%3Bs%3A10%3A%22last_refer%22%3Bs%3A24%3A%22https%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1752539754%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=6875a26a-4e29-b562-c5d9-f840a1e6bfa0; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1752559755; HMACCOUNT=9982405386288C7A; r=google; rp=a%3A2%3A%7Bs%3A1%3A%22p%22%3Bs%3A18%3A%22www.google.com.hk%2F%22%3Bs%3A1%3A%22t%22%3Bi%3A1752541752%3B%7D; oad_n=a%3A5%3A%7Bs%3A5%3A%22refer%22%3Bs%3A25%3A%22https%3A%2F%2Fwww.google.com.hk%22%3Bs%3A2%3A%22hp%22%3Bs%3A17%3A%22www.google.com.hk%22%3Bs%3A3%3A%22oid%22%3Bi%3A1075%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222025-07-15+09%3A09%3A12%22%3B%7D; mfwothchid=referrer%7Cwww.google.com.hk; omc_chl=; __omc_r=www.google.com.hk; mfwc=referrer%7Cwww.google.com.hk; mfwa=1752539754954.18687.2.1752539754954.1752626202651; mfwlv=1752626202; mfwvn=2; mfwb=cd6cf202eabf.2.google; mfwlt=1752626203; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1752626204',
    'Pragma': 'no-cache',
    'Referer': 'https://www.mafengwo.cn/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}
# resp=requests.get(url=url,headers=headers)
# r.set('mafenwo',resp.text)
rh=r.get('mafenwo').decode('utf-8')


