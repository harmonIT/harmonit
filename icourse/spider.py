import requests
import json
for i in range(1):
    # url='https://ke.study.163.com/course/detail/100155349?outVendor=zw_mooc_kaoyan_pckclb_26_1#course-body'
    url=f'https://ke.study.163.com/api/comment/history.jsonp?topicId=100155349&page={i}'
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'cookie': 'keoutvendor=zw_mooc_kaoyan_pckclb_26_1; utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9rZS5zdHVkeS4xNjMuY29tL2NvdXJzZS9kZXRhaWwvMTAwMTU3NDM5P291dFZlbmRvcj16d19tb29jX2thb3lhbl9wY2tjbGJfMjZfMQ==; NTESSTUDYSI=782f871da5404b7abda8179a835c3941; EDUWEBDEVICE=bba2e5ae24f448c39616241c8e6a25f8; hb_MA-A976-948FFA05E931_source=www.icourse163.org; xuetangvendor=; _ga=GA1.1.263435511.1746423989; OUTFOX_SEARCH_USER_ID_NCOO=1589282108.113234; Hm_lvt_e46790f6d676f71878ebef1153dda3e2=1746423989; HMACCOUNT=9982405386288C7A; ke_Pdt=Moc.Web; ke_inLoc=MocWebpd; _clck=1d0o3b0%7C2%7Cfvn%7C0%7C1951; EDU-YKT-MODULE_GLOBAL_PRIVACY_DIALOG=true; Hm_lpvt_e46790f6d676f71878ebef1153dda3e2=1746424013; _clsk=1nbu2hm%7C1746424013446%7C2%7C1%7Ce.clarity.ms%2Fcollect; _ga_PTGVM6PCHS=GS2.1.s1746423988$o1$g1$t1746424014$j0$l0$h0; JSESSIONID=D132966FFE1FEADDAD3B9B38170E4041',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://ke.study.163.com/course/detail/100157439?inLoc=MocWebpd&amp;Pdt=Moc.Web&amp;outVendor=zw_mooc_kaoyan_pckclb_26_1',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    resp=requests.get(url=url,headers=headers)
    jsData=json.loads(resp.text)
    name=[i['id'] for i in jsData['result']]
    content=[i['mark'] for i in jsData['result']]
    print(resp.status_code,name)