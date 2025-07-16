import requests
from lxml import etree

# url='https://kns.cnki.net/kcms2/article/abstract?v=oWJgMrFo8udGUq78km7T_9_xFjDaudLSPgzR9gTPwMJQx990czvdiguJ2Nl34GHRGWFagPf65EyEmCHiV8HiN6XOkY4pArBW48fVm5wWpucjAKXyhDLklIb6S73y9_H7NhRZjr51lqzf2nscUSeIVHxM6hARlZV71IMCg3TLfjIK1N4T5uDcMg==&uniplatform=NZKPT&language=CHS'
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "Cache-Control": "no-cache",
#     "Connection": "keep-alive",
#     "Cookie": "cangjieStatus_NZKPT2=false; Ecp_ClientId=e250715094200151577; SID_sug=018104; SID_kns_new=kns15018107; KNS2COOKIE=1752543768.527.76237.250333|b25e41a932fd162af3b8c5cff4059fc3; dblang=both; knsLeftGroupSelectItem=; SID_restapi=018132; Ecp_IpLoginFail=250716113.78.236.86; tfstk=gRjnFU0-yw8QMGF9WGtQRUKGKrz9AHtWO_nJw3dz7CR6vUddUQblT6YyyJORs7fPsDpyYyTyU6CW2wKURUAPhTeCvQIl50XfFMeB2JtCd3tzMSEAq96BVa0ardPOQ8JWqpzLRC1Cd3tz6M4NzdBCOtOLO_-zIhJ2F4-yzekaIKpX4D8rYVlw1C-r4URy7FJkKpoe4_WaILOwa38FahyMFbRa8BsPbGPkA56o1BROjpYHgO4jq0SZDeAVLCmzgGv3OIWes0okiGPBCOXLtm69AiCDH6EZxsXFu_7V_lmH5wWGqEsSTR-yzM6w6MPjDO-hWZLhSWok6Mpku38iU0WMYC5P4nrqsd_NpaSCtYmydMIvrITgU0TJbiLVu6D7hO-eU_Tf2SiBTTWfcZK0qc-Hzgrn7qSfi09aeGuSPeJ6IIK5YgmZQo_LeR2iu8TeCpOYIR0SPeJ6IIegIqyW8d9BM",
#     "Host": "kns.cnki.net",
#     "Pragma": "no-cache",
#     "Referer": "https://kns.cnki.net/kcms2/article/abstract?v=oWJgMrFo8udGUq78km7T_9_xFjDaudLSPgzR9gTPwMJQx990czvdiguJ2Nl34GHRGWFagPf65EyEmCHiV8HiN6XOkY4pArBW48fVm5wWpucjAKXyhDLklIb6S73y9_H7NhRZjr51lqzf2nscUSeIVHxM6hARlZV71IMCg3TLfjIK1N4T5uDcMg==&uniplatform=NZKPT&language=CHS",
#     "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"Windows"',
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "same-origin",
#     "sec-fetch-user": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
# }

# resp=requests.get(url=url,headers=headers)
# print(resp.status_code,resp.text)
# parse=etree.HTML(resp.text)
# wx_tit=parse.xpath('//div[@class="wx-tit"]/h1/text()')
# print(wx_tit)

url='https://kns.cnki.net/kns8s/brief/grid'
payload={
  "boolSearch": True,
  "QueryJson": {"Platform":"","Resource":"PATENT","Classid":"VUDIXAIY","Products":"","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":0,"Items":[{"Field":"SU","Value":"冰雪","Operator":"TOPRANK","Logic":0,"Title":"主题"}],"ChildItems":[]}]},"ExScope":1,"SearchType":2,"Rlang":"Both","KuaKuCode":"","Expands":{},"SearchFrom":1},
    "pageNum": 1,
  "pageSize": 20,
  "dstyle": "listmode",
  "boolSortSearch": False,
  "aside": "主题：冰雪",
  "searchFrom": "资源范围：专利",
  "subject": "",
  "language":"",
  "uniplatform": "",
  "CurPage": 1,
}
headers2={
  "accept": "*/*",
  "accept-encoding": "gzip, deflate, br, zstd",
  "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
  "cache-control": "no-cache",
  "connection": "keep-alive",
  "content-length": "847",
  "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
  "cookie": "Ecp_ClientId=e250715094200151577; SID_sug=018104; SID_kns_new=kns15018107; KNS2COOKIE=1752543768.527.76237.250333|b25e41a932fd162af3b8c5cff4059fc3; knsLeftGroupSelectItem=; SID_restapi=018132; Ecp_IpLoginFail=250716113.78.236.86; knsadv-searchtype=%7B%22BLZOG7CK%22%3A%22gradeSearch%2CmajorSearch%22%2C%22MPMFIG1A%22%3A%22gradeSearch%2CmajorSearch%2CsentenceSearch%22%2C%22T2VC03OH%22%3A%22gradeSearch%2CmajorSearch%22%2C%22JQIRZIYA%22%3A%22gradeSearch%2CmajorSearch%2CsentenceSearch%22%2C%22S81HNSV3%22%3A%22gradeSearch%22%2C%22YSTT4HG0%22%3A%22gradeSearch%2CmajorSearch%2CauthorSearch%2CsentenceSearch%22%2C%22ML4DRIDX%22%3A%22gradeSearch%2CmajorSearch%22%2C%22WQ0UVIAA%22%3A%22gradeSearch%2CmajorSearch%22%2C%22VUDIXAIY%22%3A%22gradeSearch%2CmajorSearch%22%2C%22NN3FJMUV%22%3A%22gradeSearch%2CmajorSearch%2CauthorSearch%2CsentenceSearch%22%2C%22LSTPFY1C%22%3A%22gradeSearch%2CmajorSearch%2CsentenceSentence%22%2C%22HHCPM1F8%22%3A%22gradeSearch%2CmajorSearch%22%2C%22OORPU5FE%22%3A%22gradeSearch%2CmajorSearch%22%2C%22WD0FTY92%22%3A%22gradeSearch%2CmajorSearch%2CauthorSearch%2CsentenceSearch%22%2C%22BPBAFJ5S%22%3A%22gradeSearch%2CmajorSearch%2CauthorSearch%2CsentenceSearch%22%2C%22EMRPGLPA%22%3A%22gradeSearch%2CmajorSearch%22%2C%22PWFIRAGL%22%3A%22gradeSearch%2CmajorSearch%2CsentenceSearch%22%2C%22U8J8LYLV%22%3A%22gradeSearch%2CmajorSearch%22%2C%22R79MZMCB%22%3A%22gradeSearch%22%2C%22J708GVCE%22%3A%22gradeSearch%2CmajorSearch%22%2C%22HR1YT1Z9%22%3A%22gradeSearch%2CmajorSearch%22%2C%22JUP3MUPD%22%3A%22gradeSearch%2CmajorSearch%2CauthorSearch%2CsentenceSearch%22%2C%22NLBO1Z6R%22%3A%22gradeSearch%2CmajorSearch%22%2C%22RMJLXHZ3%22%3A%22gradeSearch%2CmajorSearch%2CsentenceSearch%22%2C%221UR4K4HZ%22%3A%22gradeSearch%2CmajorSearch%2CauthorSearch%2CsentenceSearch%22%2C%22NB3BWEHK%22%3A%22gradeSearch%2CmajorSearch%22%2C%22XVLO76FD%22%3A%22gradeSearch%2CmajorSearch%22%7D; dblang=both; cnkiUserKey=132c72b6-4799-3e3c-04eb-2ac01aef615a; tfstk=gQKiAjaYkF719aGdJHss5ZCHoz3KXGsf9IEAMiCq865CXZC93sYD_CbVkA1vtjAHhSrObjZ0oIplDoQxCsr2OL5wBKhbm-S6vFEA6fsD3QImwbn-2d91fil-wlY9kCI1nsrV0SIULOscQ1H20lv1cilK_w1WRdO6FOKJgikhYTXb_i5N3ykhBTS4bZra8W5CTiWN0ZWU8TWzuPr2gpkhh65V0NRV8vXjB-gN1n-eYjjs1pU5t4YOINfyQ1J9sHlhxP9Vtor2xeX5a0C30o-hIKY0XTEok_856aCWTDEGmpWDZTAgTXj2Khtl8hlQmQAHzMf9E4ef6F5Nz9TIirfkudLWuwDZbpjGsaxHsRzcjER6mNTghY9FbBT5NNuIO9x92Zf5-WlwppfNrEAtOo59rpRhyHFL2MJy-MjPtyzyVQqfLxKUlr_Nd9fRch-0YJoWWxHnKzkf7961wvD3lr_Nd9f-Kv4rhNWCC_C..",
  "host": "kns.cnki.net",
  "origin": "https://kns.cnki.net",
  "pragma": "no-cache",
  "referer": "https://kns.cnki.net/kns8s/defaultresult/index?crossids=YSTT4HG0%2CLSTPFY1C%2CJUP3MUPD%2CMPMFIG1A%2CWQ0UVIAA%2CBLZOG7CK%2CPWFIRAGL%2CEMRPGLPA%2CNLBO1Z6R%2CNN3FJMUV&korder=SU&kw=%E4%B8%93%E5%88%A9",
  "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-origin",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
  "x-requested-with": "XMLHttpRequest"
}

response=requests.post(url=url,json=payload,headers=headers2)
print(response.status_code,response.text)

#200 <div id="briefBox"><p class="no-content" value="">抱歉，暂无数据，请稍后重试。</p></div>
#???