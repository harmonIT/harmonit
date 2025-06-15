import requests
import json
from openpyxl import Workbook
import time
# 定义请求的URL
url = 'https://read.douban.com/j/index/newly_published'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


name=[]
img=[]
for i in range(1,2):
    payload = {
    'page': i,
    'query': "\n    query getFilterWorksList($works_ids: [ID!]) {\n      worksList(worksIds: $works_ids) {\n        \n    id\n    isOrigin\n    isEssay\n    \n    title\n    cover(useSmall: false)\n    url\n    isBundle\n    coverLabel(preferVip: true)\n  \n    \n  url\n  title\n\n    \n  author {\n    name\n    url\n  }\n  origAuthor {\n    name\n    url\n  }\n  translator {\n    name\n    url\n  }\n\n    \n  abstract\n  authorHighlight\n  editorHighlight\n\n    \n    isOrigin\n    kinds {\n      \n    name @skip(if: true)\n    shortName @include(if: true)\n    id\n  \n    }\n    ... on WorksBase @include(if: true) {\n      wordCount\n      wordCountUnit\n    }\n    ... on WorksBase @include(if: false) {\n      inLibraryCount\n    }\n    ... on WorksBase @include(if: false) {\n      \n    isEssay\n    \n    ... on EssayWorks {\n      favorCount\n    }\n  \n    \n    \n    averageRating\n    ratingCount\n    url\n    isColumn\n    isFinished\n  \n  \n  \n    }\n    ... on EbookWorks @include(if: false) {\n      \n    ... on EbookWorks {\n      book {\n        url\n        averageRating\n        ratingCount\n      }\n    }\n  \n    }\n    ... on WorksBase @include(if: false) {\n      isColumn\n      isEssay\n      onSaleTime\n      ... on ColumnWorks {\n        updateTime\n      }\n    }\n    ... on WorksBase @include(if: true) {\n      isColumn\n      ... on ColumnWorks {\n        isFinished\n        finalizedCn\n      }\n    }\n    ... on EssayWorks {\n      essayActivityData {\n        \n    title\n    uri\n    tag {\n      name\n      color\n      background\n      icon2x\n      icon3x\n      iconSize {\n        height\n      }\n      iconPosition {\n        x y\n      }\n    }\n  \n      }\n    }\n    highlightTags {\n      name\n    }\n    ... on WorksBase @include(if: false) {\n      fanfiction {\n        tags {\n          id\n          name\n          url\n        }\n      }\n    }\n  \n    \n  ... on WorksBase {\n    copyrightInfo {\n      newlyAdapted\n      newlyPublished\n      adaptedName\n      publishedName\n    }\n  }\n\n    isInLibrary\n    ... on WorksBase @include(if: false) {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n    realPrice {\n      price\n      priceType\n    }\n  \n    }\n    ... on EbookWorks {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n    realPrice {\n      price\n      priceType\n    }\n  \n    }\n    ... on WorksBase @include(if: true) {\n      ... on EbookWorks {\n        id\n        isPurchased\n        isInWishlist\n      }\n    }\n    ... on WorksBase @include(if: false) {\n      fanfiction {\n        fandoms {\n          title\n          url\n        }\n      }\n    }\n    ... on WorksBase @include(if: false) {\n      fanfiction {\n        kudoCount\n      }\n    }\n  \n      }\n    }\n  ",
    'sort': "default",
    'variables': {},
    }
    response = requests.post(url, json=payload,headers=headers)
    jsData=json.loads(response.text)
    l=jsData['list']
    for j in l:
        name.append(j['title'])
        img.append(j['cover'])
    time.sleep(2)
    print('....')

wb = Workbook()
ws = wb.active
ws.title = "豆瓣阅读-纸书出版作品"
ws.append(['书名', '图片连接'])
for i in range(len(name)):
    ws.append([name[i], img[i]])
wb.save('豆瓣阅读-纸书出版作品.xlsx')

for index, i in enumerate(img):
    resp=requests.get(url=i,headers=headers)
    with open('./豆瓣阅读-纸书出版作品图片/{}.jpg'.format(name[index]),'wb') as file:
        for chunk in resp.iter_content(chunk_size=8192):
            file.write(chunk)
    time.sleep(2)
    print('----')
