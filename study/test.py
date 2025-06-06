import requests
url='https://baidu.com'
proxies = {
    'http': 'http://151.101.2.216',
    'https': 'http://151.101.2.216',
}
resp=requests.get(url=url,proxies=proxies)
print(resp.text[:1000])