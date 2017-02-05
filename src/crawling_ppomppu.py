# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import sys

url = 'http://www.ppomppu.co.kr/recent_main_article.php?type=market'

f = urllib2.urlopen(url)
soup = BeautifulSoup(f.read(), from_encoding="euc-kr")

datas = []
data = {'link': '', 'subject': '', 'comments': ''}

def get_data():
    global datas, data

    for li in soup.find('div', attrs={'class':'ppom_new'}).find_all('li', attrs={'class':''}):
        data['link'] = 'http://www.ppomppu.co.kr/' + li.a['href']
        _subject = li.a.get_text().encode('utf-8').strip().split('\n')
        data['subject'] = _subject[0]
        data['comments'] = _subject[1]
        datas.append(dict(data))

    # for data in datas:
        # print data['link'], data['subject']

    return datas

# get_data()