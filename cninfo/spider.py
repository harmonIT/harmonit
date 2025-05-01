import requests
import json
url='http://www.cninfo.com.cn/new/hisAnnouncement/query'
data={
"pageNum": 1,
"pageSize": 30,
"column": "szse",
"tabName": "fulltext",
"plate": "",
"stock": json.dumps("300208,9900018895"),
"searchkey": "",
"secid": "",
"category": "category_ndbg_szsh",
"trade": "",
"seDate": "2024-11-01~2025-05-01",
"sortName": "",
"sortType": "",
"isHLtitle": True,

}
resp=requests.post(url=url,data=data)
jsData=json.loads(resp.text)
announcements=jsData['announcements'][0]['adjunctUrl']

print(resp.text)