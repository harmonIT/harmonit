import requests
import json

urlID='https://edith.xiaohongshu.com/api/sns/web/v1/search/notes'
payloadID = {

}
headers = {

}
respID = requests.post(url=urlID, headers=headers, json=payloadID)
# print(respID.text[:5000])
jsData=json.loads(respID.text)
items=jsData['data']['items']
id_=[i['id'] for i in items]
token=[i['xsec_token'] for i in items]
#为什么用title=[i['note_card']['display_title'] for i in items]时候报错不存在note_card键？？？
#可能是列表推导式的原因？
title=[i.get('note_card',{}).get('display_title') for i in items]

urlCon='https://edith.xiaohongshu.com/api/sns/web/v1/feed'
payloadCon = {

}

headers2 = {

}

respCon=requests.post(url=urlCon,json=payloadCon)
print(respCon.status_code,respCon.text)
jsData2=json.loads(respCon.text)
items2=jsData2['data']['items']
content=[i.get('note_card',{}).get('desc') for i in items2]

urlPin='https://edith.xiaohongshu.com/api/sns/web/v2/comment/page?note_id=67ffeeac000000000d014ec6&cursor=&top_comment_id=&image_formats=jpg,webp,avif&xsec_token=ABUL2GsUwlZBt9-uqioGlDLBebRFueMMOmLTQ2G--g45U%3D'
respPin=requests.get(url=urlPin,headers=headers2)
jsData3=json.loads(respPin.text)
items3=jsData3['data']['comments']
comments=[i['content'] for i in items3]

print(respID.status_code)
print(respCon.status_code)
print(respPin.status_code)
print(id_)
print(token)
print(title)
print(content)
print(comments)


