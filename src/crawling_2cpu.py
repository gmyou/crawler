# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import re

url = 'http://www.2cpu.co.kr/bbs/board.php'

values = {'bo_table' : 'sell' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
f = urllib2.urlopen(req) 

soup = BeautifulSoup(f.read())

for link in soup.find_all('tr', attrs={"class": re.compile("^bg")}):
    no = link.select('td.num')
    print no[0].get_text()
    sbj = link.select('td.subject')
    if (sbj):
        print sbj[0].select('a')[0].get_text()
        print sbj[0].select('a')[0]['href']
        #print sbj[0].select('a')[0]['title']
    name = link.select('td.name')
    print name[0].get_text()
    hit = link.select('td.hit')
    print hit[0].get_text()
    date = link.select('td.datetime')
    print date[0].get_text()
    print
