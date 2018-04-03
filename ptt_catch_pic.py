# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:57:51 2018

@author: Jackson Ma
"""
#ptt上的imgur是iframe，没法直接获取，需要Selenium的switch_to.frame() 
from selenium import webdriver
import requests 
from bs4 import BeautifulSoup
import re

browser = webdriver.PhantomJS()
Found=0
order_num =1

def Get_pic(order_num):
    try:
        content_imgur= browser.find_element_by_tag_name('img')
        img_src=content_imgur.get_attribute('src') #src为tag下的属性，注意
        response = requests.get(img_src) 
        with open(str(order_num)+'.jpg', 'wb') as f:
            f.write(response.content)
            f.close()
    except Exception:
        print("No pic,skip")
    else:
        print('Success,catch',str(order_num),'catched')
        
#以FB评论框的iframe作为锚定点，避免NoSuchFrame异常抛出
def catch_page_img(page): 
    global order_num 
    global Found
    count=0
    target_page='https://pttweb.tw'+str(page)
    browser.get(target_page)
    while True:
        browser.switch_to.frame(count)
        try :
            browser.find_element_by_id('facebook') 
            print('This page is finished.')
            count=0
            break
        except Exception:
            Get_pic(order_num)
            browser.switch_to.default_content()
            count+=1
            order_num+=1
            
def find_in_page(bbs):
    print('start find_in_page')
    global Found
    try:
       bbs_page=requests.get(url=bbs,headers=headers)
       bbs_page_soup=BeautifulSoup(bbs_page.content, 'lxml')
       find=bbs_page_soup.find(text=re.compile('君名二創漫畫翻譯')).parent #获取找到文本所在的节点
       Found=1
       print('found')
       return (find['href'])
    except AttributeError:
        Found=0
        print('Not found in this page,continue')
       

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}


'''
    #对于 main（） 如果从页面开始搜索时用该段代码
    
    ptt_c_chat=requests.get(url='https://pttweb.tw/c_chat/',headers=headers)#response对象无法用bs解析，要传入content
    soup=BeautifulSoup(ptt_c_chat.content, 'lxml')
    prev_button=soup.find(rel='prev')#tag类型，获取值时用[]
    
    prev_page_num=prev_button['href']
    result = int(re.search('[\d]{4,}', prev_page_num).group())
    pages_num=int(input('How many pages you want to search backward from the last page?'))
    
    '''

def main():
    i=0
    start=int(input('Enter the page you want to start:'))
    end_page=int(input('Enter the page you want to stop:'))
    with open("catch_pic.log",'a',encoding='utf-8') as f: 
        log_str='Start at: '+str(start)+' End at: '+str(end_page)
        f.write(log_str)
    while True:
        if start-i < end_page :
            print('Reach the end')
            break
        bbs='https://pttweb.tw/c_chat/?page='+str(start-i) 
        print('start finding in page',str(start-i))
        find_in_page(bbs)
        if Found==1:
            catch_page_img(find_in_page(bbs))#此时尚未进入详情页，需修改函数
        print('page',str(start-i),'done')
        i+=1

main()        
#last time 14674