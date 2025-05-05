import requests
from lxml import etree
import pandas
import threading

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
titles=[]
locations=[]
summarys=[]
requires=[]
for i in range(1,6):
    url=f'https://next.rikunabi.com/oc_003/page{i}.html?cur=ACgAAgBQAAAAAAAAAAAAAAACRA9LFAEDAQ8gCxgHAMK5lbcS42aioAJ6SHdrnBBjGjF6fx2kqTboUmTejEuYBbL8aZwMHxIqiANlViHuyeLjvBzFUZwZ8rVcasQIiGdQAFR81lvf2CT0LyrezHRZBxm%2FpK%2B82S8Y7BQywapHoT9ogmNxIsxuXaYTGZxaTgU%3D&cur_p={i}'
    response=requests.get(url=url,headers=headers)
    text=response.content.decode('Shift_JIS',errors='ignore')
    parse=etree.HTML(text)
    title=parse.xpath('//li[@class="rnn-jobOfferList__item rnn-jobOfferList__item--adnet rnn-group rnn-group--s  js-kininaruItem js-uilTargetCassette"]//div[@class="rnn-group rnn-group--xxs rnn-jobOfferList__item__company"]/h2[@class="rnn-textLl js-abScreen__title"]/a//text()')
    location=parse.xpath('//li[@class="rnn-jobOfferList__item rnn-jobOfferList__item--adnet rnn-group rnn-group--s  js-kininaruItem js-uilTargetCassette"]//a[@class="rnn-group rnn-group--xs rnn-jobOfferList__item__offer rnn-jobOfferList__item__offer--n5"]//div[@class="rnn-jobOfferList__item__offer__detail"]//td[@class="rnn-offerDetail__text rnn-offerDetail__text--ellipsis"]//text()')
    summary=parse.xpath('//li[@class="rnn-jobOfferList__item rnn-jobOfferList__item--adnet rnn-group rnn-group--s  js-kininaruItem js-uilTargetCassette"]//a[@class="rnn-group rnn-group--xs rnn-jobOfferList__item__offer rnn-jobOfferList__item__offer--n5"]//div[@class="rnn-jobOfferList__item__offer__detail"]//tr[@class="rnn-tableGrid rnn-offerDetail js-abScreen__workInfo"]/td[@class="rnn-offerDetail__text rnn-offerDetail__text--max2line"]//text()')
    for j in range(1,41):
        require=parse.xpath(f'//li[@class="rnn-jobOfferList__item rnn-jobOfferList__item--adnet rnn-group rnn-group--s  js-kininaruItem js-uilTargetCassette"][{j}]//div[@class="rnn-jobOfferList__item__offer__detail"]/table//tr[@class="rnn-tableGrid rnn-offerDetail js-abScreen__prefer"]/td//text()')
        if require and require[0].strip():
            requires.extend(require)
        else:
            requires.append(' ')
    # require=parse.xpath('//li[@class="rnn-jobOfferList__item rnn-jobOfferList__item--adnet rnn-group rnn-group--s  js-kininaruItem js-uilTargetCassette"]//a[@class="rnn-group rnn-group--xs rnn-jobOfferList__item__offer rnn-jobOfferList__item__offer--n5"]//div[@class="rnn-jobOfferList__item__offer__detail"]//tr[@class="rnn-tableGrid rnn-offerDetail js-abScreen__prefer"]/td/text()')
    # requires.extend(require)
    titles.extend(title)
    locations.extend(location)
    summarys.extend(summary)

#清洗数据
for i in range(len(locations)):
    locations[i] = locations[i].replace('\xa0', '').replace('\u3000', '')
    summarys[i] = summarys[i].replace('\xa0', '').replace('\u3000', '')
    requires[i] = requires[i].replace('\xa0', '').replace('\u3000', '')
# print(len(titles))
# print(len(locations))
# print(len(summarys))
# print(len(requires))
# for i in requires:
#     print(type(i),i)

#导出csv
pdData={
    '标题':titles,
    '地点':locations,
    '工作概要':summarys,
    '所需人才':requires,
}
df = pandas.DataFrame(pdData)
df.to_csv('招聘.csv', index=False, encoding='utf-8')