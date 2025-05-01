import requests

url='https://www.dongqiudi.com/api/app/tabs/web/56.json?after=1746005308&page=3&child_tab_id=0&user_pay_type='
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'dqduid=rBUCV2gS3ttsDRzRGM1KAg==; Hm_lvt_335923ce349a3b7756120f8e8fbfa3d6=1746067167; HMACCOUNT=9982405386288C7A; Hm_lpvt_335923ce349a3b7756120f8e8fbfa3d6=1746067947',
    'Host': 'www.dongqiudi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.dongqiudi.com/articlesList/56',
    'Sec-Ch-Ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
resp=requests.get(url=url,headers=headers)
print(resp.json())