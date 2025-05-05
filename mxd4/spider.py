import requests
import brotli
import base64
from urllib.parse import unquote
import chardet
import json
url = 'https://api.mxd4.com:8085/wz/code/search?type=skill,Consume&key=%E9%AA%91%E5%AE%A0&version=209&isnew=0&_=1745976305800'  # 替换为您的API地址
url2='https://api.mxd4.com:8085/wz/code/search?type=skill,Consume&key=%E9%AA%91%E5%AE%A0&version=209&isnew=0&_=1745976305800'
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding':'identity',
    'authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjdhZWViMWQ0LTM5YzctNDY1Zi1hN2I2LWUyYmQ1MmVjNDliNyJ9.B5-35fisMcNmuvSciD8ZoI_h6uJDXdlSJEa_FwIrG2Hkzv98-EhwbMXrtsYLdR_ZBO2Grmdn6NkfFZZ4CvzZtg',
    'cache-control': 'no-cache',
    'connection': 'keep-alive',
    'content-type': 'application/json',
    'host': 'api.mxd4.com:8085',
    'origin': 'https://mxd4.com',
    'pragma': 'no-cache',
    'referer': 'https://mxd4.com/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
headers2 = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'access-control-request-headers': 'authorization,content-type',
    'access-control-request-method': 'GET',
    'cache-control': 'no-cache',
    'connection': 'keep-alive',
    'host': 'api.mxd4.com:8085',
    'origin': 'https://mxd4.com',
    'pragma': 'no-cache',
    'referer': 'https://mxd4.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
response2=requests.options(url=url2,headers=headers2)
response = requests.get(url=url, headers=headers)
# response.encoding='utf-8'
# print(response.status_code,response.text[:1000])
print(response.headers,response2.status_code)
data='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'        
# 解码Base64数据并使用UTF-8进行解码
decoded_bytes = base64.b64decode(data)
decoded_str = unquote(decoded_bytes)
print(decoded_str[:2000])





'''detect_result = chardet.detect(response.content)#识别编码
encoding = detect_result['encoding']
print("Detected Encoding:", encoding)
de=response.content.decode('utf-8',errors='ignore')
print('解码字符=',de[:1000])'''



'''# 解码url编码
response_json = response.json()

# 检查data字段是否为Base64编码
data_url_encoded = response_json.get('data', '')

try:
    data_decoded = unquote(data_url_encoded)
    print(data_decoded[:700])
except Exception as e:
    print(f"URL解码失败: {e}")
    print(data_url_encoded[:700])'''


'''#解码base64
response_json = response.json()

# 检查data字段是否为Base64编码
data_base64 = response_json.get('data', '')
try:
    # 尝试解码Base64
    data_decoded = base64.b64decode(data_base64)
    print(data_decoded.decode('utf-8'))
except Exception as e:
    print(f"Base64解码失败: {e}")
    print(data_base64)'''


'''# 如果用br压缩，解压缩
if response.headers.get('Content-Encoding') == 'br':
    # 使用brotli解码
    response_data = brotli.decompress(response.content)
    print(response_data.decode('utf-8'))
else:
    print(response.text[:1000])'''
'''# 假设 compressed_data 是一个字节流
dctx = zstd.ZstdDecompressor()
reader = dctx.stream_reader(response.content)
data = reader.read()'''

