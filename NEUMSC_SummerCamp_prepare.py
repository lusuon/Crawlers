import re
import urllib

import requests
from bs4 import BeautifulSoup
from gevent import os
count = 0



def catch_picInPage(page):
    global count  # 函数中调用时需要声明为全局
    file_path = "E://MSC_temp_pic/"
    r = requests.get(page)
    soup = BeautifulSoup(r.text, 'lxml')
    container_node = soup.body.find(attrs={'class': 'main-container'})
    content_node = container_node.div.article.div.div.find(attrs={'id': 'ajax_content'})
    element_list = content_node.find_all(attrs={'id': re.compile('sch_[0-9]*')})
    img_url_list = []
    for i in element_list:
        src_node = i.table.find(attrs={'class': "myc5"})
        img_url_list.append(src_node['src'])

    for img_url in img_url_list:
        count += 1
        print("Start trying")
        try:
            urllib.request.urlretrieve(img_url,file_path+str(count)+".jpg")
            print('success')
        except Exception as e:
            print(e)
            break


if __name__ == '__main__':
    # 载入第一页
    start_page = 'http://www.guide2research.com/scientists/'
    start_request = requests.get(start_page)
    start_soup = BeautifulSoup(start_request.text, 'lxml')
    start_container_node = start_soup.body.find(attrs={'class': 'main-container'})
    start_content_node = start_container_node.div.article.div.div.find(attrs={'id': 'ajax_content'})
    nextPageTable = start_content_node.table.find_all(name='li')
    nextPageList = [start_page]
    # 载入翻页
    for i in nextPageTable:
        try:
            nextUrl = i.a.attrs['href']
            nextPageList.append(nextUrl)
        except Exception:
            print("No url")
    print(nextPageList)
    # 对每页进行抓取
    for j in nextPageList:
        catch_picInPage(j)
