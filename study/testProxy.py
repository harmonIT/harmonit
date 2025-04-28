import requests

url='https://www.youtube.com'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
}
proxies = {
    'http': 'socks5://127.0.0.1:1081',
    'https': 'socks5://127.0.0.1:1081',
}
resp=requests.get(url=url,headers=headers,proxies=proxies)
print(resp.status_code)
print(resp.text[:200])