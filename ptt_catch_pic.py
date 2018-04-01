# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:57:51 2018

@author: Jackson Ma
"""
#ptt上的imgur是iframe，没法直接获取，需要Selenium的switch_to.frame() 
from selenium import webdriver
import requests 
from bs4 import BeautifulSoup

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
        print('Success')
        
#以FB评论框的iframe作为锚定点，避免NoSuchFrame异常抛出
def catch_page_img(): 
    global order_num 
    count=0
    while True:
        browser.switch_to.frame(count)
        #iframe_html_id=
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

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
ptt_c_chat=requests.get(url='https://pttweb.tw/c_chat/',headers=headers)#response对象无法用bs解析，要传入content
soup=BeautifulSoup(ptt_c_chat.content, 'lxml')
print(soup.find(rel='prev'))


'''
browser = webdriver.PhantomJS()
browser.get('')#等待解析的详情页


order_num = 1
'''


'''

#Get_pic函数的参数用于获取批量命名的ID 
def Get_pic(order_num):
    content_imgur= browser.find_element_by_tag_name('img')
    img_src=content_imgur.get_attribute('src') #src为tag下的属性，注意
    response = requests.get(img_src) 
    with open(str(order_num)+'.jpg', 'wb') as f:
        f.write(response.content)
        f.close()

循环结尾使i（命名用参数）自增加
'''