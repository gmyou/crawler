# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import sys

url = 'http://www.2cpu.co.kr/sell'

values = {'bo_table' : 'sell' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
f = urllib2.urlopen(req)

soup = BeautifulSoup(f.read())
trs = soup.find('table', attrs={'class': 'table table-condensed table-hover'}).find_all('tr', attrs={'class': ''})

datas = []
data = {'number': 0, 'subject': '', 'writer': '', 'write_date': '', 'hits': 0, 'link': ''}


pattern = r'(\d+)만원?'
priceCheck = re.compile(pattern)
def getPrice(string):
    if ( bool(priceCheck.search(string)) ):
        match = priceCheck.search(string)
        return match.group()

def get_data():
    global datas, data

    for tr in trs[5:]:
        values = tr.get_text().split('\n')
        i = 0
        for value in values:
            if (value!=''):
                if (i==0): data['number'] = value
                if (i==1): data['subject'] = value.encode('utf-8').strip()
                if (i==2): data['writer'] = value
                if (i==3): data['write_date'] = value
                if (i==4): data['hits'] = value
                if (i>4): pass
                i += 1
        data['link'] = tr.a['href'].replace('../sell', url)

        ''' TODO getPrice
        1. Authorization
        2. Crawling data['link']
        3. getPrice
        4. input data['price']
        '''
        datas.append(dict(data))

    # for data in datas:
    #     print data['link'], data['subject']

    return datas

# print get_data()
