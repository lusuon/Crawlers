# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:30:02 2018

@author: Jackson Ma
"""
import re
import sys
import requests
import shutil
from bs4 import BeautifulSoup
from lxml import etree



headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
url_target='https://pttweb.tw/c_chat/m-1484733503-a-59b.html'

page=requests.get(url=url_target,headers=headers)#生成的page为reponse对象
ptt_soup=BeautifulSoup(page.text, 'lxml')#创建一个soup对象
#threats=ptt_soup.find_all(attrs={"href":re.compile('[c_chat]+/[^"]*')})
print(re.findall('[c_chat]+/[^"]*',str(page.content)))

with open('test.txt','w') as f:
    for i in re.findall('/[^"]*',str(page.content)):
        f.write(i)


#正则：[c_chat]+/[^"]*

'''
def fetch(url_target,i): #i为for循环次数作计数
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    page=requests.get(url=url_target,headers=headers)#生成的page为reponse对象
    ptt_soup=BeautifulSoup(page.text, 'lxml')#创建一个soup对象
    content=ptt_soup.find(class_='bbs-screen bbs-content').text #此处为字符串
    start_position=0
    if content.find('本文開始'):
        start_position=content.find('本文開始')
    end_position=content.find('發信站')
    out=content[(start_position)+4:end_position] 
    time=ptt_soup.find(class_="table-sm borderless").text
    time_start_position=time.find('時間')
    file_time=time[time_start_position+4:time_start_position+14]
    with open("["+str(i)+"]-"+file_time+".txt",'a',encoding='utf-8') as f: #读写模式用引号括起，自动生成文件名用变量+'.txt'
        f.write(out)
        f.close
for i in range(length()):#连接个数，用list长度决定
    i=1
    url= "https://pttweb.tw/"+[i]
    fetch(url,i)
'''
    
    
    
    
    





'''
#未完工的xpath解析
html=etree.HTML(page.text)#将reponse对象的文本变为html
result = etree.tostring(html) #此处直接解析html地址,而非reponse对象
print(result.decode('utf-8'))

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//*')
print(result)
'''
