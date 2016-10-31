# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import re, sys

url = 'http://kmug.co.kr/board/zboard.php'

values = {'id' : 'sale' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
f = urllib2.urlopen(req)

soup = BeautifulSoup(f.read(), from_encoding="euc-kr")

datas = []
data = {'number': 0, 'subject': '', 'writer': '', 'write_date': '', 'hits': 0, 'link': ''}

def get_data():
    global datas, data

    for tr in soup.find_all('tr', attrs={"class": re.compile("^ctl_list[0-9]")}):
        if tr.a is None:
            pass
        else:
            data['number'] = tr.td.get_text()
            data['subject'] = tr.a.get_text().encode('utf-8').strip()
            data['link'] = tr.a['href'].replace('zboard.php', url)
            datas.append(dict(data))

    # for data in datas:
    #     print data['link'], data['subject']

    return datas

# get_data()
