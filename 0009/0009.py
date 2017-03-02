# -*-coding:utf8 -*-
# author: yushan
# date: 2017-03-02


import requests
from bs4 import BeautifulSoup
# 网上随便找的新闻链接
news_url = 'http://www.jn001.com/finance/2017-02/24/content_239671.htm'
r = requests.get(news_url)
content = r.content.decode('utf-8')
soup = BeautifulSoup(content,'html.parser')
# 输出文章标题
title = soup.h1.get_text()
print "标题是:",title
links = soup.select('a[href]')
print "查找到的所有链接："
for item in links:
    href = item['href']
    a_con = item.get_text()
    if len(href) > 5 and href[:10] != 'javascript':
        print a_con,"链接为：",href