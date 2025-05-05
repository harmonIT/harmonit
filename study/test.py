import requests				#导入requests库

import re
#导入re模块

from bs4 import BeautifulSoup		#导入BeautifulSoup
#定义一个getHtml()函数，根据填写的url参数获取数据

def getHtml(url):
    #异常处理

    try:

         r = requests.get(url)			#使用get函数打开指定的url

         r.raise_for_status()			#如果状态不是200，则引发异常

         r.encoding = 'utf-8'			#更改编码方式
         #print("tttttt",r.text)

         return r.text				#返回页面内容

    except:

         return ""				#发生异常返回空字符


#定义数据解析函数，用于找到符合条件的数据并输出

def getcon(html):

    bsObj = BeautifulSoup(html)
    print("ffffff",bsObj)
#将html对象转化为BeautifulSoup对象
    #找到所有class为bk_show_info的div，只获取图书信息

   # divList = bsObj.find_all('div',{'class':'pcv1_module_title flex'})
    divList = bsObj.find_all('div',{'class':'index_list_box bg_fff'})
    #print("aaaaaa",divList)
    #print("qqqqqq",divList[1].section["title"])

    allbook = []
    #存储全部数据，二维列表
    book_info = []	#存储单本图书信息，一维列表

    for divs in divList:

        		


        book_name = divs.section["title"]	#获取图书名称
        print("bbbbbb",book_name)

        book_info.append(book_name)	#将图书名称存储到book_info
       

       # p_list = divs.find_all('p')		#查找单本图书的其他信息（在标签p中）
        #for p_content in p_list:

           #book_info.append(p_content.string)#将p标签中的信息存入book_info

          # allbook.append(book_info)		#将单本图书的信息存入allbook

    print("bbbbbb",book_info)
    #输出获取到的图书信息

    #for book in allbook:

       # print(book)

html = getHtml("https://www.wenjingketang.com/bookHome")	#调用获取页面内容函数

getcon(html)				#调用解析数据函数







import requests				#导入requests库

import re
#导入re模块

from bs4 import BeautifulSoup		#导入BeautifulSoup
#定义一个getHtml()函数，根据填写的url参数获取数据

def getHtml(url):
    #异常处理

    try:

         r = requests.get(url)			#使用get函数打开指定的url

         r.raise_for_status()			#如果状态不是200，则引发异常

         r.encoding = 'utf-8'			#更改编码方式
         #print("tttttt",r.text)

         return r.text				#返回页面内容

    except:

         return ""				#发生异常返回空字符


#定义数据解析函数，用于找到符合条件的数据并输出

def getcon(html):

    bsObj = BeautifulSoup(html)
    print("ffffff",bsObj)
#将html对象转化为BeautifulSoup对象
    #找到所有class为bk_show_info的div，只获取图书信息

   # divList = bsObj.find_all('div',{'class':'pcv1_module_title flex'})
    divList = bsObj.find_all('div',{'class':'index_list_box bg_fff'})
    #print("aaaaaa",divList)
    #print("qqqqqq",divList[1].section["title"])

    allbook = []
    #存储全部数据，二维列表
    book_info = []
    for divs in divList:

       			#存储单本图书信息，一维列表

        book_name = divs.section["title"]	#获取图书名称

        book_info.append(book_name)	#将图书名称存储到book_info
       

       # p_list = divs.find_all('p')		#查找单本图书的其他信息（在标签p中）
        #for p_content in p_list:

           #book_info.append(p_content.string)#将p标签中的信息存入book_info

          # allbook.append(book_info)		#将单本图书的信息存入allbook

    print("bbbbbb",book_info)
    #输出获取到的图书信息

    #for book in allbook:

       # print(book)
    return book_info

def main(Bookname):

    #html = getKeywordResult('Python程序设计教程')	#调用获取页面内容函数

    #ls = parserLinks(html)			#调用解析数据函数

    count = 1

    with open('D:\data.txt','w') as fd:		#将数据写入12-4.txt文件中

        for i in Bookname:

            fd.write('[')

            fd.write(str(count))

            fd.write(']')

            fd.write(i)				#写入文件

            fd.write('\n')

            count += 1

    print('写入文件成功！')


html = getHtml("https://www.wenjingketang.com/bookHome")	#调用获取页面内容函数

name=getcon(html)				#调用解析数据函数
main(name)

