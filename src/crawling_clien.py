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
data = {'number': 0, 'link': '', 'subject': '', 'price': ''}

pattern = r'(\d+)만'
priceCheck = re.compile(pattern)
def getPrice(string):
    if ( bool(priceCheck.search(string)) ):
        match = priceCheck.search(string)
        return match.group()

def get_data():
    global datas, data

    for tr in soup.find_all('tr', attrs={"class": "mytr"}):
        data['number'] = tr.td.get_text()
        data['link'] = tr.find('td', {'class':'post_subject'}).a['href'].replace('../bbs/board.php', url)
        data['subject'] = tr.find('td', {'class':'post_subject'}).a.get_text().encode('utf-8').strip()
        if ( getPrice(data['subject']) != None ):
            data['price'] = getPrice(data['subject'])
        else:
            # TODO getPrice From Contents
            data['price'] = ''

        datas.append(dict(data))

    # for data in datas:
        # print data['price']
    return datas

# print get_data()
