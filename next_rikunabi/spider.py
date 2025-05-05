from selenium import webdriver
from lxml import etree
import time
url='https://next.rikunabi.com/oc_003/page3.html?cur=ACgAAgBQAAAAAAAAAAAAAAACRA9LFAEDAQ8gCxgHAMK5lbcS42aioAJ6SHdrnBBjGjF6fx2kqTboUmTejEuYBbL8aZwMHxIqiANlViHuyeLjvBzFUZwZ8rVcasQIiGdQAFR81lvf2CT0LyrezHRZBxm%2FpK%2B82S8Y7BQywapHoT9ogmNxIsxuXaYTGZxaTgU%3D&cur_p=3'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'sProp3=0; TERMINAL_ID=iKipJjU0%2BZRswpfbyPeqc%2Br3AgdRObh2; __ctk__=1iq8bo8f5h41n801; _gcl_au=1.1.524842843.1746184973; __lt__cid=97b842cd-8122-4ab0-aded-96f623c3b4de; _yjsu_yjad=1746184973.cafac416-41a7-49ac-99e6-125363f8edc9; _ga=GA1.3.710847064.1746184974; _fbp=fb.1.1746184973913.154913336952248491; _mkto_trk=id:445-ZDA-122&amp;token:_mch-rikunabi.com-246583c6fc71a58c1c70b0d02e5034bd; _tt_enable_cookie=1; _ttp=01JT8BRBTGVVS8D5MCFWFP51B5_.tt.1; RNSESSIONID=43DAB19EFA2776D83813F309A4CF63D4; ARPT=537205420.13354.0000; _gid=GA1.3.916399874.1746336279; _gid=GA1.2.916399874.1746336279; ttcsid=1746336279465::TYyGQS6b3btCR_aN-NX0.2.1746336807787; ttcsid_CS2TLJJC77U61CV1SSO0=1746336279464::McvkfXp7R2djBAZXV9ZA.2.1746336808093; ttcsid_CV4F7NJC77U1D91BRQB0=1746336279466::IiZOSL1a3lmZA3J0LyI7.2.1746336808093; _uetsid=130b363028a811f0a7074fda21aa3d50; _uetvid=ca5fb2c0274711f081037dfb84f055eb; _ga_MEF2XJ3DG4=GS1.3.1746336280.2.1.1746336610.53.0.0; cto_bundle=LHRgJF9LblJ2Wmx3VktlWUklMkZiSHkzSzgzcG9iSGx6TGs2YjhUc2E3bm5oNGxxdyUyRnBxZzBEc2hxZXExb09nRlI2bWdUMXo5YTlSUkVYWGdGcW9XQUw4RjNEZ2haaFBTVnplWThRVVlOUThqekV2VDlScmswSENyazNGZDExa3lacEVMVHY5bDlQbTZZSmUyMDV3SDRUazV4UnRldDVqdCUyQlRJYnpLJTJGcGVhZkxrMzdkTSUzRA; s_sess=%20rnn_prev_pageName%3Drnext%253Arnc%253Adocs%253Acp_s00700.jsp%3B%20_rnnPrvCst%3D%3B%20s_cc%3Dtrue%3B%20s_ppv%3D100%3B; _ga_9L73HH8JJG=GS1.1.1746341062.4.0.1746341062.60.0.0; s_pers=%20s_fr%3D2025%253A05%253A02%7C1777720973863%3B%20s_fid%3D1A40E26407440DF7-26B3014B3E7071D4%7C1904107471107%3B%20s_nr%3D1746341071108-Repeat%7C1777877071108%3B%20s_lst%3D2025%253A05%253A04%7C1777877071110%3B%20s_cm%3D1%7C1746342871111%3B%20sc_poSts%3Dnm%7C1777877071112%3B; _ga=GA1.2.710847064.1746184974; _gat_UA-82885531-2=1; _ga_MEF2XJ3DG4=GS1.2.1746341071.3.0.1746341071.60.0.0',
    'Host': 'next.rikunabi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://next.rikunabi.com/oc_003/page2.html?cur=ACgAAQAoAAAAAAAAAAAAAAACRA9LFAEBAQkCt727WboMdQ7w%2BwIixkys3u6dQ2gVxRbJfC7jWZbrRpaiBs%2F18XXMzDpPg3X2aX2XOkwQCVB%2Fu%2FDHFd%2Fzjo6pZ4xb68u2dD0olkOCVUR3krGPaSM%3D&amp;cur_p=2',
    'Sec-Ch-Ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}
browser=webdriver.Chrome()
browser.get(url=url)
time.sleep(5)
parse=etree.HTML(browser.page_source)
print(browser.page_source[:3000])
title=parse.xpath('//h2[@class="rnn-textLl js-abScreen__title"]/a/text()')
print(title)
browser.quit()
