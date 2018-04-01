# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:30:02 2018

@author: Jackson Ma
Todo:
    实现检测更新:
        1.读取本地文件名中的时间
        2.与页面对应元素进行比对：抓取时间 加入list 与末项比较
"""
import re
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
url_target='https://pttweb.tw/c_chat/m-1484733503-a-59b.html'

page=requests.get(url=url_target,headers=headers)#生成的page为reponse对象
ptt_soup=BeautifulSoup(page.text, 'lxml')#创建一个soup对象
threats=ptt_soup.find(class_='table table-striped borderless').find_all('a')
links_list=[]
for i in list(threats):
    result=re.search(r"c[\S]*html",str(i))#尽量使用search(),而非match，否则难以匹配到理想结果
    if result!=None: #返回SRE_Match object对象，注意用group()将其化成字符串
        links_list.append(result.group())
     


'''
with open('test.txt','w') as f:
    for i in re.findall('/[^"]*',str(page.content,re.S)):
        f.write(i)
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
    time=ptt_soup.find(class_="post-time").text
    time_start_position=time.find('時間')
    file_time=time[time_start_position+4:time_start_position+13]
    with open("["+str(i)+"]-"+file_time+".txt",'a',encoding='utf-8') as f: #读写模式用引号括起，自动生成文件名用变量+'.txt'
        f.write(out)
        f.close
for i in range(len(links_list)):#连接个数，用list长度决定
    url="https://pttweb.tw/"+links_list[i]
    fetch(url,i)