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
con = soup.find_all('p', 'MsoNormal')
strings = '' # 正文内容
print "正文是："
for item in con:
    strings += item.span.get_text()
    strings += '\n'
print strings