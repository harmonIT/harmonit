import requests
import csv
import re
import time
import random
from tqdm import tqdm
from fake_useragent import UserAgent
import pandas as pd

# 随机生成 User-Agent
def get_random_useragent():
    ua = UserAgent()
    return ua.random

# 用于更新 headers
def update_headers(cookie):
    headers = {
        "User-Agent": get_random_useragent(),  # 使用随机UA避免被封
        "Cookie": cookie
    }
    return headers

shop_id = "l77r3adKGBjj0tfC"
for i in tqdm(range(1,3)):
    url = f"https://www.dianping.com/shop/{shop_id}/review_all/p{i}"
    cookie="GSI=#rf_syztwlb@210720a#sl_zdjlwxbdsb@211011l#rf_tsmbyrk@220309b#rf_syjgwlb@220829a; _lxsdk_cuid=19662022a7cc8-068ed00e04054d-26011c51-144000-19662022a7cc8; _lxsdk=19662022a7cc8-068ed00e04054d-26011c51-144000-19662022a7cc8; _hc.v=80fc0aa0-b45e-b86c-4d2b-6371ca42ff51.1745401032; s_ViewType=10; WEBDFPID=8v84732y45v454y90xv18wyw1v8647xu803379732wv9795834366544-1745487446631-1745401045333ECWUKIEfd79fef3d01d5e9aadc18ccd4d0c95073976; qruuid=f17f6977-6efd-434d-babd-07ccded59e12; dper=0202d4230b94d166f569143f122d84588a93cee42f1f55cc4d4ce469d84985dee3611067b5993b4af29744def6fbeb9bd261bf9cbcf8cc42913f000000009228000077411a09b648e7d137011a92c60aada9614f93d5fd1f8ebc5c2ad6d751cd51de2284bf69ee0428568be34b5b2bca5c16; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1745401194; HMACCOUNT=9982405386288C7A; fspop=test; __CACHE@is_login=true; logan_custom_report=; cy=9; cye=chongqing; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1745477152; __CACHE@referer=https://www.dianping.com/chongqing/ch10/g110; logan_session_token=xz74tcfswgres86uryyl; _lxsdk_s=196668660ec-d8e-31a-91b%7C%7C146"
    headers=update_headers(cookie)
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    print(response.status_code,response.text)
    time.sleep(3)
