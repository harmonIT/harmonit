import requests
import json
from openpyxl import Workbook

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Cookie': 'Hm_lvt_af1fda4748dacbd3ee2e3a69c3496570=1749476011; Hm_lpvt_af1fda4748dacbd3ee2e3a69c3496570=1749476011; HMACCOUNT=9982405386288C7A',
    'Pragma': 'no-cache',
    'Sec-Ch-Ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}

url = 'https://www.shanghairanking.cn/api/pub/v1/bcmr/rank?year=2024&majorCode=050306T'
resp = requests.get(url=url, headers=headers)
resp.encoding = 'utf-8'
parse = json.loads(resp.text)
rankings = parse['data']['rankings']

grade = [i['grade'] for i in rankings][:50]
ranking = [i['ranking'] for i in rankings][:50]
univNameCn = [i['univNameCn'] for i in rankings][:50]
univTags = [i['univTags'] for i in rankings][:50]
city = [i['city'] for i in rankings][:50]
score = [i['score'] for i in rankings][:50]

wb = Workbook()
ws = wb.active
ws.title = "2024年学校排名"
ws.append(['评级', '排名', '学校名称', '学校标签', '省市', '总分'])
for i in range(50):
    ws.append([grade[i], ranking[i], univNameCn[i], str(univTags[i]), city[i], score[i]])
wb.save('中国大学专业网络与新媒体2024年学校排名.xlsx')
