# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import re, sys

url = 'http://www.clien.net/cs2/bbs/board.php'

values = {'bo_table' : 'sold' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
f = urllib2.urlopen(req)

soup = BeautifulSoup(f.read(), from_encoding="utf-8")

datas = []
data = {'number': 0, 'subject': '', 'writer': '', 'write_date': '', 'hits': 0, 'link': ''}


def get_data():
    global datas, data

    for tr in soup.find_all('tr', attrs={"class": "mytr"}):
        data['number'] = tr.td.get_text()
        data['link'] = tr.find('td', {'class':'post_subject'}).a['href'].replace('../bbs/board.php', url)
        data['subject'] = tr.find('td', {'class':'post_subject'}).a.get_text().encode('utf-8').strip()
        datas.append(dict(data))

    for data in datas:
        print data['link'], data['subject']
    return datas

print get_data()