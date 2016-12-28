# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import sys

url = 'http://corearoadbike.com/board/board.php'

values = ['Menu01Top6', 'Menu30Top6', 'Menu31Top6', 'Menu02Top6', 'Menu08Top6', 'Menu32Top6']

def set_bs(menu_id):
    _values = {'t_id' : menu_id,  'category' : '판매'}
    _data = urllib.urlencode(_values)
    _req = urllib2.Request(url, _data)
    _f = urllib2.urlopen(_req)

    soup = BeautifulSoup(_f.read())
    return soup.find_all('td', attrs={'class': 'list_title_B'})

datas = []
data = {'link': '', 'subject': ''}

def get_data():
    global datas, data, values

    for _values in values:
        for _data in set_bs(_values):
            data['link'] = _data.a['href'].replace('./board.php', url)
            data['subject'] = _data.a.get_text()
            datas.append(dict(data))

    # for data in datas:
    #     print data['link'], data['subject']

    return datas

# get_data()