from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url='https://yjszs.zjut.edu.cn/gsapp/sys/dszszgxxykfwappzjut/*default/index.do#dszsxx'
browser=webdriver.Chrome()
browser.get(url=url)

def findElement(click=None,text=None,text2=None,eles=None):
    if click:
        ele=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, click)))
        return ele
    if text:
        ele=WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, text), text2))
        return ele
    if eles:
        l_ist=[]
        ele=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located(By.XPATH,eles))
        for i in ele:
            l_ist.append(i)
        return l_ist
#执行自动化点击操作
select=findElement('','//span','请选择...','')
browser.execute_script("arguments[0].click();", select)#无法找到可点击的元素！！！！！
jisuanji=findElement('','//span[@class="jqx-listitem-state-normal jqx-item jqx-rc-all"]', '计算机科学与技术学院（软件学院）','')
browser.execute_script("arguments[0].click();", jisuanji)
sousuo=findElement('//a[@class="bh-btn bh-btn-primary"]')
browser.execute_script("arguments[0].click();",sousuo)
nameList=[]
linkList=[]
for i in range(1):
    names=findElement('','','','//tr[@role="row"]/td[0]/span')
    links=findElement('','','','//tr[@role="row"]/td[3]/a')

    for each,x in zip(names,links):
        print(each.text)
        print(x.get_attribute('href'))


