# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import sys
from module.common import getPrice

url = 'http://www.ppomppu.co.kr/recent_main_article.php?type=market'

f = urllib2.urlopen(url)
soup = BeautifulSoup(f.read(), from_encoding="euc-kr")

datas = []
data = {'link': '', 'subject': '', 'comments': '', 'price': ''}

pattern = r'(\d+)만'

def get_data():
    global datas, data

    for li in soup.find('div', attrs={'class':'ppom_new'}).find_all('li', attrs={'class':''}):
        _subject = li.a.get_text().encode('utf-8').strip().split('\n')
        if ( len(_subject)==2 ):
            data['link'] = 'http://www.ppomppu.co.kr' + li.a['href']
            data['subject'] = _subject[0]
            data['comments'] = _subject[1]
            if ( getPrice(data['subject'], pattern) != None ):
                data['price'] = getPrice(data['subject'], pattern)
            else:
                # TODO getPrice From Contents
                data['price'] = ''
        else:
            pass
        datas.append(dict(data))

    for data in datas:
        print data['price']

    return datas

get_data()
